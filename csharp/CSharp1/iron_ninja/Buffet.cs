using System;
using System.Collections.Generic;

namespace iron_ninja
{
    class Buffet
    {
        public List<IConsumable> Menu;

        public Buffet()
        {
            Menu = new List<IConsumable>()
            {
                new Food("McChicken", 350, false, false),
                new Food("McCurry", 250, true, false),
                new Drink("McFlurry", 500, false, true),
                new Food("Big Mac", 600, false, false),
                new Food("Sweet & Sour Chicken", 750, true, true)
            };
        }

        public IConsumable Serve()
        {
            Random rand = new Random();
            return Menu[rand.Next(0, Menu.Count)];
        }
    }
}