using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ChefsNDishes.Models;
using Microsoft.EntityFrameworkCore;

namespace ChefsNDishes.Controllers
{
    public class HomeController : Controller
    {
        private MyContext dbContext;
        public HomeController(MyContext context)
        {
            dbContext = context;
        }

        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            List<Chef> AllChefs = dbContext.Chefs
            .Include(c => c.Dishes)
            .ToList();
            return View(AllChefs);
        }

        [HttpGet("new")]
        public IActionResult New()
        {
            return View();
        }

        [HttpPost("create")]
        public IActionResult Create(Chef newChef)
        {
            if(ModelState.IsValid)
            {
                dbContext.Chefs.Add(newChef);
                dbContext.SaveChanges();
                return RedirectToAction("Index");
            }

            return View("New");
        }

    }
}
