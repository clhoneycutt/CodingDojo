using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using CRUDelicious.Models;
using Microsoft.EntityFrameworkCore;

namespace CRUDelicious.Controllers
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
            List<Dish> allDishes = dbContext.Dishes.ToList();
            ViewBag.allDishes = allDishes;
            return View();
        }

        [HttpGet("new")]
        public IActionResult New()
        {
            return View();
        }

        [HttpPost("create")]
        public IActionResult Create(Dish newDish)
        {
            if(ModelState.IsValid)
            {
                dbContext.Dishes.Add(newDish);
                dbContext.SaveChanges();
                Dish justAdded = dbContext.Dishes.LastOrDefault<Dish>();
                
                return RedirectToAction("show", new {dishID = justAdded.DishID});
            };

            return RedirectToAction("Index");
        }

        [HttpGet("{dishID}/show")]
        public IActionResult Show(int dishID)
        {
            Dish thisDish = dbContext.Dishes
            .FirstOrDefault(d => d.DishID == dishID);
            return View(thisDish);
        }

        [HttpGet("{dishID}/edit")]
        public IActionResult Edit(int dishID)
        {
            Dish thisDish = dbContext.Dishes
            .FirstOrDefault(d => d.DishID == dishID);

            return View(thisDish);
        }

        [HttpPost("update")]
        public IActionResult Update(Dish updatedDish)
        {

            if(ModelState.IsValid)
            {
                Dish thisDish = dbContext.Dishes
                    .FirstOrDefault(d => d.DishID == updatedDish.DishID);

                thisDish.Chef = updatedDish.Chef;
                thisDish.Name = updatedDish.Name;
                thisDish.Calories = updatedDish.Calories;
                thisDish.Description = updatedDish.Description;
                thisDish.Tastiness = updatedDish.Tastiness;

                thisDish.UpdatedAt = DateTime.Now;

                dbContext.SaveChanges();

                return RedirectToAction("show", new {dishID = updatedDish.DishID});
            }

            return View("Edit", updatedDish);
        }

        [HttpGet("{dishID}/delete")]
        public IActionResult Delete(int dishID)
        {
            Dish goodbyeDish = dbContext.Dishes
                .FirstOrDefault(d => d.DishID == dishID);

            dbContext.Dishes.Remove(goodbyeDish);
            dbContext.SaveChanges();

            return RedirectToAction("Index");
        }

    }
}
