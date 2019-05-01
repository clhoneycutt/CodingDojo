using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;


using ChefsNDishes.Models;
using System.Dynamic;

namespace ChefsNDishes.Controllers
{
    [Route("dishes")]
    public class DishController : Controller
    {
        private MyContext dbContext;
        public DishController(MyContext context)
        {
            dbContext = context;
        }

        [HttpGet("")]
        public IActionResult Index()
        {
            List<Dish> AllDishes = dbContext.Dishes
            .Include(d => d.Chef)
            .ToList();
            
            return View(AllDishes);

        }

        [HttpGet("new")]
        public IActionResult New()
        {
            ViewBag.AllChefs = dbContext.Chefs.ToList();
            return View();
        }

        [HttpPost("create")]
        public IActionResult Create(Dish newDish)
        {
            if(ModelState.IsValid)
            {
                newDish.Chef = dbContext.Chefs.FirstOrDefault(c => c.ChefID == newDish.ChefID);
                dbContext.Dishes.Add(newDish);
                dbContext.SaveChanges();
                return RedirectToAction("Index");
            }

            return View("New");
        }
    }
}