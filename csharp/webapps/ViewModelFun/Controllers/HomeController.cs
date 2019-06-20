using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ViewModelFun.Models;

namespace ViewModelFun.Controllers
{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Message()
        {   
            Message message = new Message()
            {

            Content = "Something about something about something about something about something about something about something about something about something"
            
            };

            return View("Index", message);
        }

        [HttpGet("users")]
        public IActionResult Users()
        {
            User Chris = new User
            {
                FirstName = "Chris",
                LastName = "Honeycutt"
            };

            User Brandt = new User
            {
                FirstName = "Brandt",
                LastName = "Honeycutt"
            };

            User Aubri = new User
            {
                FirstName = "Aubri",
                LastName = "Mannasmith"
            };

            List<User> users = new List<User>()
            {
                Chris, Brandt, Aubri
            };

            return View(users);
        }

        [HttpGet("user")]
        public new IActionResult User()
        {
            User Chris = new User
            {
                FirstName = "Chris",
                LastName = "Honeycutt"
            };

            User Brandt = new User
            {
                FirstName = "Brandt",
                LastName = "Honeycutt"
            };

            User Aubri = new User
            {
                FirstName = "Aubri",
                LastName = "Mannasmith"
            };

            List<User> users = new List<User>()
            {
                Chris, Brandt, Aubri
            };

            Random rand = new Random();

            int randomUserIdx;
            randomUserIdx = rand.Next(0, 3);

            User user = new User();
            user = users[randomUserIdx];

            return View(user);
        }

        [HttpGet("numbers")]
        public IActionResult Numbers()
        {
            Random rand = new Random();            
            RandNumbers randNum = new RandNumbers
            {
                nums = new int[] {rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51), rand.Next(0,51)}
            };
            return View(randNum);
        }
    }
}
