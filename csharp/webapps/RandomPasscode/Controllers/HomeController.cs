using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using RandomPasscode.Models;

namespace RandomPasscode.Controllers
{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            ViewBag.Code = HttpContext.Session.GetString("Code");
            return View();
        }

        [HttpGet("newpasscode")]
        public IActionResult newCode()
        {
            Random random = new Random();
            string RandomString(int length)
            {
                const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
                return new string(Enumerable.Repeat(chars, length)
                .Select(s => s[random.Next(s.Length)]).ToArray());
            }
            string passcode = RandomString(14);
            HttpContext.Session.SetString("Code", passcode);
            return RedirectToAction("Index");
        }

    }
}
