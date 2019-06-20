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
    [Route("products")]
    public class ProductController : Controller
    {
        private MyContext dbContext;
        public ProductController(MyContext context)
        {
            dbContext = context;
        }

        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {

            if(HttpContext.Session.GetInt32("InvalidEntry") == 1)
            {
                HttpContext.Session.SetInt32("InvalidEntry", 0);
                ModelState.AddModelError("Product.Name", "Invalid Entry");
            }

            NewProductView NewProdView = new NewProductView();
            NewProdView.Products = dbContext.Products.ToList();
            return View(NewProdView);
        }

        [HttpGet("{ProductID}")]
        public IActionResult Show(int ProductID)
        {
            AddCategorytoProductView AddCatToProduct = new AddCategorytoProductView();
            Product thisProduct = dbContext.Products
                .Where(c => c.ProductID == ProductID)
                .Include(c => c.AssociatedCategories)
                .ThenInclude(assoc => assoc.Category)
                .FirstOrDefault();

            AddCatToProduct.Product = thisProduct;
            AddCatToProduct.Categories = dbContext.Categories
                .Include(c => c.AssociatedProducts).ToList();            
            

            return View(AddCatToProduct); //AddProductToProduct
        }

        [HttpPost("newproduct")]
        public IActionResult NewProduct(NewProductView newProductView)
        {
            if(ModelState.IsValid)
            {
                dbContext.Products.Add(newProductView.Product);
                dbContext.SaveChanges();

                Product lastAddedProduct = dbContext.Products.LastOrDefault();
                
                return RedirectToAction("Index"); //, new {id = lastAddedProduct.ProductID}
            }
            else
            {
                HttpContext.Session.SetInt32("InvalidEntry", 1);
                return RedirectToAction("Index");
            }
        }

        [HttpPost("{ProductID}/AddCategoryToProduct")]
        public IActionResult AddCategoryToProduct(int productID, int categoryID)
        {


            Association newAssociation = new Association()
            {
                ProductID = productID,
                CategoryID = categoryID
            };

            dbContext.Associations.Add(newAssociation);
            dbContext.SaveChanges();



            return RedirectToAction("Show"); //, new {id = ProductID}
        }
    }
}
