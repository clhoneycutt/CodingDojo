using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using LoginReg.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Http;

namespace LoginReg.Controllers
{
    public class HomeController : Controller
    {
        private int? UserSession
        {
            get { return HttpContext.Session.GetInt32("UserId"); }
            set { HttpContext.Session.SetInt32("UserId", (int)value); }
        }
        private MyContext dbContext;
        public HomeController(MyContext context)
        {
            dbContext = context;
        }

        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost("register")]
        public IActionResult Register(User user)
        {
            if(ModelState.IsValid)
            {
                if(dbContext.Users.Any(u => u.Email == user.Email))
                {
                    ModelState.AddModelError("Email", "Email already in use!");
                    return View("Index");
                }
                PasswordHasher<User> Hasher = new PasswordHasher<User>();
                user.Password = Hasher.HashPassword(user, user.Password);

                dbContext.Add(user);
                dbContext.SaveChanges();

                User LastUserAdded = dbContext.Users.LastOrDefault<User>();
                UserSession = LastUserAdded.userID;
                HttpContext.Session.SetString("FirstName", user.FirstName);
                HttpContext.Session.SetString("RegOrLog","Registration");
                
                return RedirectToAction("Success");
            }
            else
            {
                return View("Index");
            }
        }

        [HttpGet("loginPage")]
        public IActionResult LoginPage()
        {
            return View("Login");
        }

        [HttpPost("login")]
        public IActionResult Login(LogUser loginAttempt)
        {
            if(ModelState.IsValid)
            {
                var userInDB = dbContext.Users.FirstOrDefault(u => u.Email == loginAttempt.Email);

                if(userInDB == null)
                {
                    ModelState.AddModelError("Email", "Invalid Email/Password.");
                    return View("loginPage");
                }
                else
                {
                    var hasher = new PasswordHasher<LogUser>();
                    var result = hasher.VerifyHashedPassword(loginAttempt, userInDB.Password, loginAttempt.Password);

                    if(result == 0)
                    {
                        ModelState.AddModelError("Email", "Invalid Email/Password");
                        return View("loginPage");
                    }

                    UserSession = userInDB.userID;
                    HttpContext.Session.SetString("FirstName", userInDB.FirstName);
                    HttpContext.Session.SetString("RegOrLog", "Login");
                    return RedirectToAction("Success");
                }
            }
            else
            {
                return View("Login");
            }
        }

        [HttpGet("success")]
        public IActionResult Success()
        {
            if(UserSession == null)
                return RedirectToAction("Index");

            ViewBag.FirstName = HttpContext.Session.GetString("FirstName");
            ViewBag.RegOrLog = HttpContext.Session.GetString("RegOrLog");
            return View();
        }

        [HttpGet("logout")]
        public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }

    }
}
