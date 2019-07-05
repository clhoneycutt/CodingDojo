namespace iron_ninja
{
    class SpiceHound : Ninja
    {
        public override bool IsFull
        {
            get
            {
                if (calorieIntake > 1200)
                    return true;
                else
                    return false;
            }
        }

        public SpiceHound(string name)
        {
            Name = name;
        }
        
        public override void Consume(IConsumable item)
        {
            if (IsFull)
            {
                System.Console.WriteLine("I couldn't eat another bite!");
            }
            else
            {
                calorieIntake += item.Calories;
                if (item.IsSpicy)
                    calorieIntake -= 5;
                ConsumptionHistory.Add(item);
                item.GetInfo();
            }
        }
    }
}