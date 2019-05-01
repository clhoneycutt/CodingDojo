using Microsoft.AspNetCore.Mvc;
using DojoSurveywValidations.Models;

namespace DojoSurveywValidations.Controllers
{
    public class SurveyController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View();
        }

        [HttpPost("process")]
        public IActionResult Process(User User)
        {
            if(ModelState.IsValid)
            {
                return RedirectToAction("success", User);
            }
  
            return View("Index");
        }

        [HttpGet("success")]
        public IActionResult Success(User User)
        {
            return View(User);
        }
    }
}