using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using FormValidation.Models;

namespace FormValidation.Controllers
{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            return View();
        }

        [Route("success")]
        [HttpGet]
        public IActionResult Success()
        {
            return View();
        }

        [Route("registration")]
        [HttpPost]
        public IActionResult Registration(User User)
        {
            if(ModelState.IsValid)
            {

            return RedirectToAction("success");
            }
            
            else 
            {
                return View("Index");
            }
        }
    }
}
