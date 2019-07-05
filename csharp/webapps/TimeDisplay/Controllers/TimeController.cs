using Microsoft.AspNetCore.Mvc;

namespace RazorFun.Controllers
{
    public class TimeController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View();
        }
    }
}