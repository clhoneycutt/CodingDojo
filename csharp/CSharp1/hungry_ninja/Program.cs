using System;

namespace hungry_ninja
{
    class Program
    {
        static void Main(string[] args)
        {
            Buffet WhiteHouseVisit = new Buffet();
            
            Ninja Chris = new Ninja();

            Chris.Sleep();

            Food DinnerIsReady = WhiteHouseVisit.Serve();
            Chris.Eat(DinnerIsReady);
            Food Seconds = WhiteHouseVisit.Serve();
            Chris.Eat(DinnerIsReady);
            Food Thirds = WhiteHouseVisit.Serve();
            Chris.Eat(DinnerIsReady);
            Food Dessert = WhiteHouseVisit.Serve();
            Chris.Eat(DinnerIsReady);


        }
    }
}
