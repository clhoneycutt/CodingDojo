using System.Collections.Generic;

namespace iron_ninja
{
    abstract class Ninja
    {
    public string Name;
    protected int calorieIntake;
    public List<IConsumable> ConsumptionHistory;
    public Ninja()
    {
        calorieIntake = 0;
        ConsumptionHistory = new List<IConsumable>();
    }
    public abstract bool IsFull {get;}
    public abstract void Consume(IConsumable item);        
    }
}