using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using WeddingPlanner.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Http;

namespace WeddingPlanner.Controllers
{
    [Route("weddings")]
    public class WeddingController : Controller
    {
        private int? UserSession
        {
            get { return HttpContext.Session.GetInt32("UserId"); }
            set { HttpContext.Session.SetInt32("UserId", (int)value); }
        }
        private MyContext dbContext;
        public WeddingController(MyContext context)
        {
            dbContext = context;
        }

        [HttpGet("")]
        public IActionResult Index()
        {
            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            List<Wedding> allWeddings = dbContext.Weddings
                                            .Include(w => w.Guests).ToList();
            ViewBag.FirstName = HttpContext.Session.GetString("FirstName");
            ViewBag.UserSession = UserSession;
            return View(allWeddings);
        }

        [HttpGet("new")]
        public IActionResult New()
        {
            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            ViewBag.FirstName = HttpContext.Session.GetString("FirstName");
            ViewBag.UserSession = UserSession;
            return View();
        }

        [HttpPost("create")]
        public IActionResult Create(Wedding newWedding)
        {
            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            if(ModelState.IsValid)
            {
                newWedding.OrganizerID = (int)UserSession;
                dbContext.Weddings.Add(newWedding);
                dbContext.SaveChanges();
                return RedirectToAction("Index");
            }

            return RedirectToAction("New");
        }

        [HttpGet("{weddingID}")]
        public IActionResult Show(int weddingID)
        {
            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            Wedding thisWedding = dbContext.Weddings
                .Include(w => w.Guests)
                .ThenInclude(g => g.User)
                .Where(w => w.WeddingID == weddingID)
                .FirstOrDefault();
            
            ViewBag.UserSession = UserSession;
            return View(thisWedding);
        }

        [HttpGet("rsvp/{weddingID}")]
        public IActionResult RSVP(int weddingID)
        {

            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            Guest newGuest = new Guest()
            {
                WeddingID = weddingID,
                UserID = (int)UserSession
            };

            dbContext.Guests.Add(newGuest);
            dbContext.SaveChanges();

            return RedirectToAction("Index");
        }

        [HttpGet("unrsvp/{weddingID}")]
        public IActionResult UNRSVP(int weddingID)
        {

            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            Guest goodbyeGuest = dbContext.Guests.FirstOrDefault(g => g.WeddingID == weddingID && g.UserID == UserSession);

            if(goodbyeGuest == null)
                return RedirectToAction("Index");

            dbContext.Guests.Remove(goodbyeGuest);
            dbContext.SaveChanges();

            return RedirectToAction("Index");
        }

        [HttpGet("delete/{weddingID}")]
        public IActionResult Delete(int weddingID)
        {
            if(UserSession == null)
                return RedirectToAction("Index", "Home");

            Wedding goodbyeWedding = dbContext.Weddings.FirstOrDefault(w => w.WeddingID == weddingID);

            dbContext.Weddings.Remove(goodbyeWedding);
            dbContext.SaveChanges();

            return RedirectToAction("Index");
        }

    }
}