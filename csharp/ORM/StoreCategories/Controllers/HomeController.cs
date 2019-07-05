using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using StoreCategories.Models;

namespace StoreCategories.Controllers
{
    public class HomeController : Controller
    {
        private MyContext dbContext;
        public HomeController(MyContext context)
        {
            dbContext = context;
        }

        [HttpGet("")]
        public IActionResult Index()
        {
            if(HttpContext.Session.GetInt32("InvalidEntry") == 1)
            {
                HttpContext.Session.SetInt32("InvalidEntry", 0);
                ModelState.AddModelError("Category.Name", "Invalid Entry");
            }

            NewCategoryView NewCatView = new NewCategoryView();
            NewCatView.Categories = dbContext.Categories.ToList();

            return View(NewCatView);
        }

        [HttpGet("{CategoryID}")]
        public IActionResult Show(int CategoryID)
        {
            AddProductToCategoryView AddProdToCategoryView = new AddProductToCategoryView();        
            
            Category thisCategory = dbContext.Categories
                .Where(c => c.CategoryID == CategoryID)
                .Include(c => c.AssociatedProducts)
                .ThenInclude(assoc => assoc.Product)
                .FirstOrDefault();
            AddProdToCategoryView.Category = thisCategory;

            AddProdToCategoryView.Products = dbContext.Products
            .Include(p => p.AssociatedCategories).ToList();
            

            return View(AddProdToCategoryView); //AddProductToCategory
        }

        [HttpPost("newcategory")]
        public IActionResult NewCategory(NewCategoryView newCategory)
        {
            if(ModelState.IsValid)
            {
                dbContext.Categories.Add(newCategory.Category);
                dbContext.SaveChanges();

                Category lastAddedCategory = dbContext.Categories.LastOrDefault();
                
                return RedirectToAction("Index"); //, new {id = lastAddedCategory.CategoryID}
            }
            else
            {
                HttpContext.Session.SetInt32("InvalidEntry", 1);
                return RedirectToAction("Index");
            }
        }

        [HttpPost("{CategoryID}/AddProductToCategory")]
        public IActionResult AddProductToCategory(int categoryID, int productID)
        {
            Association newAssociation = new Association()
            {
                ProductID = productID,
                CategoryID = categoryID
            };

            dbContext.Associations.Add(newAssociation);
            dbContext.SaveChanges();
            return RedirectToAction("Show", new {CategoryID = categoryID});
        }

    }
}
