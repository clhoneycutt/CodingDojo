using System;

namespace humans
{
    public class Program
    {
        static void Main(string[] args)
        {
            Wizard Chris = new Wizard("Chris");
            Ninja Tony = new Ninja("Tony");

            Console.WriteLine($"{Chris.Name} is at {Chris.Health} health.");
            Console.WriteLine($"{Tony.Name} is at {Tony.Health} health.");
            
            
            Tony.Attack(Chris);
            Console.WriteLine($"{Tony.Name} does a jumping spin attack! {Chris.Name} has {Chris.Health} health left.");

            Chris.Attack(Tony);
            Console.WriteLine($"{Chris.Name} casts Magic Missle. {Tony.Name} has {Tony.Health} health left.");
        }
    }
}
