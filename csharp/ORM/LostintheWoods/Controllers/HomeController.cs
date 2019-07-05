using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using LostintheWoods.Models;
using LostintheWoods.Factory;

namespace LostintheWoods.Controllers
{
    public class HomeController : Controller
    {
        private readonly TrailFactory _TrailFactory;
        public HomeController(TrailFactory uFactory)
        {
            _TrailFactory = uFactory;
        }

        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            ViewBag.AllTrails = _TrailFactory.ShowAllTrails();
            return View();
        }


// ------------------------
        [HttpGet("add")]
        public IActionResult Add()
        {
            return View();
        }


// ------------------------
        [HttpPost("/create")]
        public IActionResult Create(Trail trail)
        {
            if(ModelState.IsValid)
            {
                long newTrailID = _TrailFactory.AddNewTrail(trail);
                return RedirectToAction("show", new {trailID = newTrailID});
            }
            else
            {
                return View("add");
            }
        }


// ------------------------
        [HttpGet("{trailID}/show")]
        public IActionResult Show(int trailID)
        {
            ViewBag.Trail = _TrailFactory.ShowTrail(trailID);
            if(ViewBag.Trail == null)
            {
                return RedirectToAction("Index");
            }
            else
            {
                return View();
            }
        }

        [HttpGet("{trailID}/delete")]
        public IActionResult Delete(int trailID)
        {
            _TrailFactory.DeleteTrail(trailID);
            return RedirectToAction("Index");
        }
    }
}
