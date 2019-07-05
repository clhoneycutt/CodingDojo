namespace humans
{
    class Wizard : Human
    {
        public Wizard(string name) : base(name)
        {
            Name = name;
            Strength = 3;
            Intelligence = 25;
            Dexterity = 3;
            Health = 50;
        }

        public override int Attack(Human target){
            int damage = 5 * Intelligence;
            target.Health -= damage;
            Health += damage;
            return target.Health;
        }

        public int Heal(Human target){
            int HealingDone = 10 * Intelligence;
            target.Health += HealingDone;
            return HealingDone;
        }
    }
}