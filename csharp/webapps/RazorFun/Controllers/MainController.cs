using Microsoft.AspNetCore.Mvc;

namespace RazorFun.Controllers
{
    public class MainController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View();
        }
    }
}