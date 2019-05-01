using System.Collections.Generic;

namespace hungry_ninja
{
    class Ninja
    {
        private int calorieIntake;
        public List<Food> FoodHistory = new List<Food>();
        
        public Ninja()
        {
            calorieIntake = 0;

        }

        public bool IsFull{
            get
            {
                if (calorieIntake > 1200)
                    return true;
                else
                    return false;
            }

        }

        public void Eat(Food item)
        {
            if (IsFull){
                System.Console.WriteLine("I couldn't eat another bite!");
            }
            else{
                calorieIntake += item.Calories;
                FoodHistory.Add(item);
                if (item.IsSpicy && item.IsSweet)
                    System.Console.WriteLine(item.Name + "! Yum! The best of both worlds, sweet AND spicy. nom nom nom. It has " + item.Calories + " calories.");
                else if (item.IsSweet)
                    System.Console.WriteLine(item.Name + "! Yum! It's so sweet!  It has " + item.Calories + "calories.");
                else if (item.IsSpicy)
                    System.Console.WriteLine(item.Name + "! Yum! But it burns as it comes and as it goes. :( It's got " + item.Calories + " calories.");

                if (calorieIntake > 1200 )
                    System.Console.WriteLine("I'm so full now! I couldn't eat another bite");

            }
        }

        public void Sleep()
        {
            calorieIntake = 0;
        }
    }
}