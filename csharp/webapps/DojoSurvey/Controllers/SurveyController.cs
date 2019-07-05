using Microsoft.AspNetCore.Mvc;

namespace DojoSurvey.Controllers
{
    public class SurveyController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View();
        }

        [HttpPost("process")]
        public IActionResult Process(string name, string location, string favLang, string comment)
        {
            ViewBag.Name = name;
            ViewBag.Location = location;
            ViewBag.FavLang = favLang;
            ViewBag.Comment = comment;   
            return View();
        }
    }
}