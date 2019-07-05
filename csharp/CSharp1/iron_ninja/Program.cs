using System;

namespace iron_ninja
{
    class Program
    {
        static void Main(string[] args)
        {
            Buffet WhiteHouseVisit = new Buffet();
            SweetTooth Chris = new SweetTooth("Chris");
            SpiceHound Brandt = new SpiceHound("Brandt");

            bool Dinnertime = true;
            Console.WriteLine("It's Dinnertime!");
            Console.ReadLine();
            while (Dinnertime)
            {
                if (Chris.IsFull == false)
                    Chris.Consume(WhiteHouseVisit.Serve());
                    
                if (Brandt.IsFull == false)
                    Brandt.Consume(WhiteHouseVisit.Serve());


                if (Chris.IsFull && Brandt.IsFull)
                {
                    Dinnertime = false;
                    Console.WriteLine("Dinner is now complete.");
                }
            }

            Console.ReadLine();

            if (Chris.ConsumptionHistory.Count > Brandt.ConsumptionHistory.Count)
            {
                int calories = 0;
                foreach (IConsumable meal in Chris.ConsumptionHistory)
                {
                    calories += meal.Calories;
                }

                Console.WriteLine($"{Chris.Name} has eaten the most with {Chris.ConsumptionHistory.Count} meals and totaling {calories} calories!");
                Console.WriteLine("He has eaten the following:");

                foreach (IConsumable meal in Chris.ConsumptionHistory)
                {
                    Console.WriteLine(meal.Name);
                }
            }
            else
            {
                int calories = 0;
                foreach (IConsumable meal in Brandt.ConsumptionHistory)
                {
                    calories += meal.Calories;
                }
                Console.WriteLine($"{Brandt.Name} has eaten the most with {Brandt.ConsumptionHistory.Count} meals and totaling {calories} calories!");

                Console.WriteLine("He has eaten the following:");

                foreach (IConsumable meal in Brandt.ConsumptionHistory)
                {
                    Console.WriteLine(meal.Name);
                }
            }

        }
    }
}
