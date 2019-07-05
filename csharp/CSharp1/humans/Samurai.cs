namespace humans
{
    class Samurai : Human
    {
        public Samurai(string name) : base(name)
        {
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            Health = 200;
        }

        public override int Attack(Human target)
        {
            if (target.Health < 50)
                target.Health = 0;
            else
                base.Attack(target);
            return target.Health;
        }

        public void Meditate(){
            Health = 200;
        }
    }
}