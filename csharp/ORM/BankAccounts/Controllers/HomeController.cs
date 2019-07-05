using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using BankAccounts.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;

namespace BankAccounts.Controllers
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


        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }


        [HttpPost("register")]
        public IActionResult Register(User newUser)
        {
            if(ModelState.IsValid)
            {
                if(dbContext.Users.Any(u => u.Email == newUser.Email))
                {
                    ModelState.AddModelError("Email", "Email already in use!");
                    return View("Index");
                }
                PasswordHasher<User> Hasher = new PasswordHasher<User>();
                newUser.Password = Hasher.HashPassword(newUser, newUser.Password);

                dbContext.Add(newUser);
                dbContext.SaveChanges();

                User LastUserAdded = dbContext.Users.LastOrDefault<User>();
                UserSession = LastUserAdded.userID;
                HttpContext.Session.SetString("FirstName", newUser.FirstName);
                
                return RedirectToAction("Index", "Transaction");
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
                    return View("Login");
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
                    return RedirectToAction("Index", "Transaction");
                }
            }
            else
            {
                return View("Login");
            }
        }

        [HttpGet("logout")]
        public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index", "Home");
        }
    }
}
