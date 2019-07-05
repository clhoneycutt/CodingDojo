using System;

namespace humans
{
    class Ninja : Human
    {
        public Ninja(string name) : base(name)
        {
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 175;
            Health = 100;
        }

        public override int Attack(Human target){
            int damage = 5 * Intelligence;
            target.Health -= damage;
            Random rand = new Random();
            int DiceRoll = rand.Next(1,6);
            if (DiceRoll == 5)
                damage += 10;
            return target.Health;
        }

        public void Steal(Human target){
            target.Health -= 5;
            Health += 5;
        }
    }
}