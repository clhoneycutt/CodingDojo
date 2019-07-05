namespace iron_ninja
{
    class SweetTooth : Ninja
    {
        public override bool IsFull
        {
            get
            {
                if (calorieIntake > 1500)
                    return true;
                else
                    return false;
            }
        }

        public SweetTooth(string name)
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
                if (item.IsSweet)
                    calorieIntake += 10;
                ConsumptionHistory.Add(item);
                item.GetInfo();
            }
        }
    }
}