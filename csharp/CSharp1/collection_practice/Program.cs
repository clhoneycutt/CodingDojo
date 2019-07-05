using System.Collections.Generic;
using System;

namespace collection_practice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] intRay = {0,1,2,3,4,5,6,7,8,9};

            string[] names = {"Tim", "Martin", "Nikki", "Sara"};
            bool[] troof = {true,false,true,false,true,false,true,false,true,false};

            List<string> iceCream = new List<string>();

            iceCream.Add("Pistachio");
            iceCream.Add("Cherry Cordial");
            iceCream.Add("Cookies n Cream");
            iceCream.Add("Chocolate");
            iceCream.Add("Neopolitan");
            iceCream.Add("Chocolate Chip Cookie Dough");

            Console.WriteLine($"These are my {iceCream.Count} favorite ice cream flavors");

            Console.WriteLine($"It's exam week, so I binge eat the entire pint of {iceCream[2]}, bring on the stomach ache.");
            iceCream.Remove("Cookies n Cream");

            Console.WriteLine($"There are now {iceCream.Count} flavors in mah freezer.");

            Dictionary<string,string> favIceCream = new Dictionary<string,string>();
            Random rand = new Random();
            foreach (string name in names)
            {
                favIceCream.Add(name, iceCream[rand.Next(0,4)]);
            }

            foreach(var entry in favIceCream)
            {
                Console.WriteLine(entry.Key + "'s favorite ice cream is " + entry.Value);
            }
            
        }
    }
}
