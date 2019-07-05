using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace Dojodachi.Controllers
{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Index()
        {
            int? isAngry = HttpContext.Session.GetInt32("isAngry");
            if(isAngry == 1)
            {
                HttpContext.Session.SetInt32("isAngry", 0);
                ViewBag.isAngry = true;
            }
            else
            {
                ViewBag.isAngry = false;
            }

            int? inProgress = HttpContext.Session.GetInt32("inProgress");
            if(inProgress == null)
            {
                HttpContext.Session.SetInt32("inProgress", 1);
                HttpContext.Session.SetInt32("Fullness", 20);
                HttpContext.Session.SetInt32("Happiness", 20);
                HttpContext.Session.SetInt32("Meals", 3);
                HttpContext.Session.SetInt32("Energy", 50);
            }

            @ViewBag.Fullness = HttpContext.Session.GetInt32("Fullness");
            @ViewBag.Happiness = HttpContext.Session.GetInt32("Happiness");
            @ViewBag.Meals = HttpContext.Session.GetInt32("Meals");
            @ViewBag.Energy = HttpContext.Session.GetInt32("Energy");

            
            
            if(HttpContext.Session.GetInt32("Fullness") >= 100 && HttpContext.Session.GetInt32("Happiness") >= 100 && HttpContext.Session.GetInt32("Energy") >= 100)
            {
                HttpContext.Session.SetString("Message", "Your pet is thriving!  You have won this game! Would you like to play again? Press restart below!");
                @ViewBag.GameWon = true;    
            }
            Random randPic = new Random();
            ViewBag.randPic = randPic.Next(1,3);
            if(HttpContext.Session.GetString("Message") != null)
                ViewBag.Message = HttpContext.Session.GetString("Message");
            return View();
            
        }

        [HttpGet("feed")]
        public IActionResult Feed()
        {
            // Feeding Pet 1 meal
            if(HttpContext.Session.GetInt32("Meals") == 0)
            {
                HttpContext.Session.SetString("Message", "Uh oh, You're out of Meals!");
                return RedirectToAction("Index");
            }
            else if(HttpContext.Session.GetInt32("Fullness") == 100)
            {
                HttpContext.Session.SetString("Message", "You are too full to eat!");
                return RedirectToAction("Index");
            }
            else
            {
                int Meals = 0;
                if(HttpContext.Session.GetInt32("Meals").HasValue)
                    Meals=HttpContext.Session.GetInt32("Meals").Value;
                Meals -= 1;
                HttpContext.Session.SetInt32("Meals", Meals);
            
                // Adding fullness
                Random rand = new Random();
                
                int Fullness = 0;
                if(HttpContext.Session.GetInt32("Fullness").HasValue)
                    Fullness=HttpContext.Session.GetInt32("Fullness").Value;
                int AddedFullness = rand.Next(5,10);
                Fullness += AddedFullness;
                HttpContext.Session.SetInt32("Fullness", Fullness);
                HttpContext.Session.SetString("Message", string.Format("Your pet happily eats his food!  You have expended 5 energy and your pet has gained {0} fullness", AddedFullness.ToString()));

                return RedirectToAction("Index");
            }
        }

        [HttpGet("play")]
        public IActionResult Play()
        {
            if(HttpContext.Session.GetInt32("Energy") == 0)
            {
                HttpContext.Session.SetString("Message", "You are out of energy, time to go to sleep!");
                return RedirectToAction("Index");
            }

            else
            {
                int Energy = 0;
                if(HttpContext.Session.GetInt32("Energy").HasValue)
                    Energy = HttpContext.Session.GetInt32("Energy").Value;
                Energy -= 5;
                HttpContext.Session.SetInt32("Energy", Energy);

                Random AngerChance = new Random();


                // If Angry, no Happiness added
                if(AngerChance.Next(0,101) < 26)
                {
                    HttpContext.Session.SetInt32("isAngry", 1);
                    HttpContext.Session.SetString("Message", "Uh oh! Your pet has gotten angry! You lost 5 energy, but he does not want to play!");
                    return RedirectToAction("Index");
                }
                else
                {
                
                    // Adds a random amount of happiness between 5-10
                    Random rand = new Random();
                    HttpContext.Session.SetInt32("IsAngry", 0);
                    int Happiness = 0;
                    if(HttpContext.Session.GetInt32("Happiness").HasValue)
                        Happiness=HttpContext.Session.GetInt32("Happiness").Value;
                    int AddedHappiness = rand.Next(5,10);
                    Happiness += AddedHappiness;

                    HttpContext.Session.SetInt32("Happiness", Happiness);
                    HttpContext.Session.SetString("Message", string.Format("Your pet is having fun playing! You have expended 5 Energy and your pet has gained {0} happiness!", AddedHappiness.ToString()));
                    return RedirectToAction("Index");
                }
            }

        }

        [HttpGet("work")]
        public IActionResult Work()
        {
            if(HttpContext.Session.GetInt32("Energy") == 0)
            {
                HttpContext.Session.SetString("Message", "You are out of energy, time to go to sleep!");
                return RedirectToAction("Index");
            }
            else
            {
                int Energy = 0;
                if(HttpContext.Session.GetInt32("Energy").HasValue)
                    Energy = HttpContext.Session.GetInt32("Energy").Value;
                Energy -= 5;
                HttpContext.Session.SetInt32("Energy", Energy);

                Random AngerChance = new Random();
                if(AngerChance.Next(0,101) < 26)
                {
                    HttpContext.Session.SetInt32("isAngry", 1);
                    HttpContext.Session.SetString("Message", "Uh oh! Your pet became angry he does NOT want to do ANYTHING.  You have lost 5 energy, but your pet does not gain any meals.");                    return RedirectToAction("Index");
                }
                else
                {


                    Random randMeals = new Random();
                    HttpContext.Session.SetInt32("IsAngry", 0);
                    int Meals = 0;
                    if(HttpContext.Session.GetInt32("Meals").HasValue)
                        Meals=HttpContext.Session.GetInt32("Meals").Value;
                    int AddedMeals = randMeals.Next(1,4);
                    Meals += AddedMeals;
                    HttpContext.Session.SetInt32("Meals", Meals);
                    HttpContext.Session.SetString("Message", string.Format("Your pet gets right to work!  You expend 5 energy and gain {0} meals.", AddedMeals.ToString()));
                    return RedirectToAction("Index");
                }
            }
        }
        
        [HttpGet("sleep")]
        public IActionResult Sleep()
        {
            int Energy = 0;
            if(HttpContext.Session.GetInt32("Energy").HasValue)
                Energy=HttpContext.Session.GetInt32("Energy").Value;

            int Happiness = 0;
            if(HttpContext.Session.GetInt32("Happiness").HasValue)
                Happiness=HttpContext.Session.GetInt32("Happiness").Value;
            
            int Fullness = 0;
            if(HttpContext.Session.GetInt32("Fullness").HasValue)
                Fullness=HttpContext.Session.GetInt32("Fullness").Value;
            
            Energy += 15;
            if(Energy < 0)
                Energy = 0;
            Happiness -= 5;
            if(Happiness < 0)
                Happiness = 0;
            Fullness -= 5;
            if(Fullness < 0)
                Fullness = 0;

            HttpContext.Session.SetInt32("Energy", Energy);
            HttpContext.Session.SetInt32("Happiness", Happiness);
            HttpContext.Session.SetInt32("Fullness", Fullness);

            HttpContext.Session.SetString("Message", "Sleep tight, little pet.  Your pet gains 15 energy, but loses 5 happiness and fullness");
            return RedirectToAction("Index");
        }

        [HttpGet("restart")]
        public IActionResult Restart()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}
