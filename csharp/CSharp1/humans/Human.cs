using System;

namespace humans
{
    public class Human
    {
        public string Name;
        public int Strength;
        public int Intelligence;
        public int Dexterity;
        private int health;

        public int Health
        {
            get { return health; }
            set { health = value; }
        }

        public Human(string name)
        {   
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            Health = 100;
        }

        public Human(string name, int strength, int intelligence, int dexterity, int Health)
        {   
            Name = name;
            Strength = strength;
            Intelligence = intelligence;
            Dexterity = dexterity;
            Health = health;
        }

        public virtual int Attack(Human target){
            int damage = Strength * 5;
            target.Health -= damage;
            return target.Health;
        }

    }
}