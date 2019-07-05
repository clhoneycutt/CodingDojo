using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using LoginAndReg.Models;

namespace LoginAndReg.Controllers
{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost("register")]
        public IActionResult Register(IndexViewModel modelData)
        {
            RegUser User = modelData.NewUser;
            if(ModelState.IsValid)
            {
                return RedirectToAction("success");
            }

            return View("Index");
        }

        [HttpPost("login")]
        public IActionResult Login(IndexViewModel modelData)
        {
            LogUser User = modelData.User;
            if(ModelState.IsValid)
                return RedirectToAction("Success");
            return View("Index");
        }

        [HttpGet("success")]
        public IActionResult Success()
        {
            return View();
        }
    }
}
