using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Survey.Models;

namespace Survey.Controllers
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
        public IActionResult Registration(SurveyForm YourSurvey)
        {

            return RedirectToAction("result", YourSurvey);
        }

        [HttpGet("result")]
        public IActionResult Result(SurveyForm YourSurvey)
        {
            return View(YourSurvey);
        }

    }
}
