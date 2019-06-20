using System;
using System.Collections.Generic;

namespace puzzles
{
    class Program
    {
        static void Main(string[] args)
        {
            // int[] Arr = RandomArray();
            // for(int idx=1;idx<10;idx++){
            //     Console.WriteLine(Arr[idx]);
            // }

            // string FlipACoin = TossCoin();
            // Console.WriteLine(FlipACoin);

            List<string> NameList = Names();


        }

        public static int[] RandomArray(){
            Random rand = new Random();
            int[] randArr = new int[10];
            for(int idx=0;idx<10;idx++){
                randArr[idx] = rand.Next(5,26);
            }
            int min = randArr[0];
            int max = randArr[0];
            int total = randArr[0];
            for(int idx=1;idx<10;idx++){
                if (randArr[idx] < min){
                    min = randArr[idx];
                }
                if (randArr[idx] > max){
                    max = randArr[idx];
                }
                total += randArr[idx];
            }
            Console.WriteLine("The smallest number is " + min + ". The largest number is " + max + ". The total of all numbers of the array is " + total + ".");

            return randArr;
        }

        public static string TossCoin(){
            Console.WriteLine("Tossing a Coin!");
            Random rand = new Random();
            int CoinToss = rand.Next(1,3);
            if (CoinToss == 1){
                Console.WriteLine("Landed on Heads!");
                return "Heads!";
            }
            else{
                Console.WriteLine("Landed on Tails!");
                return "Tails!";
            }
        }

        public static List<string> Names(){
            Random rand = new Random();
            List<string> Names = new List<string>();
            Names.Add("Todd");
            Names.Add("Tiffany");
            Names.Add("Charlie");
            Names.Add("Geneva");
            Names.Add("Sydney");

            for (int i = 0; i < Names.Count; i++) {
                string temp = Names[i];
                int randomIndex = rand.Next(i, Names.Count);
                Names[i] = Names[randomIndex];
                Names[randomIndex] = temp;
            };

            for (int i = 0; i < Names.Count; i++) {
                Console.WriteLine(Names[i]);
                if (Names[i].Length < 5){
                    Names.Remove(Names[i]);
                };
            };

            Console.WriteLine(Names.Count);

            return Names;

        }

    }
}
