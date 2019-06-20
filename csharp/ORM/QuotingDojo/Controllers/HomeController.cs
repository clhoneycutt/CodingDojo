using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using QuotingDojo.Models;

namespace QuotingDojo.Controllers
{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {

            return View();
        }
        [Route("show")]
        [HttpGet]
        public IActionResult Show()
        {
            List<Dictionary<string, object>> AllQuotes = DbConnector.Query("SELECT * FROM entries ORDER BY id DESC");
            // To provide this data, we could use ViewBag or a View Model.  ViewBag shown here:
            ViewBag.Quotes = AllQuotes;
            return View();
        }
        // Create a User
        [Route("create")]
        [HttpPost]
        public IActionResult Create(Entry entry)
        {
            if(ModelState.IsValid)
            {

            string query = $"INSERT INTO entries (Name, Quote) VALUES ('{entry.Name}', '{entry.Quote}')";
            DbConnector.Execute(query);
            return RedirectToAction("show");
            }
            else
            {
                return RedirectToAction("Index");
            }
        }

    }
}
