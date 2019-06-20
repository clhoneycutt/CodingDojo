using System;
using System.Collections.Generic;

namespace unboxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> boxingList = new List<object>();


            boxingList.Add(7);
            boxingList.Add(28);
            boxingList.Add(true);
            boxingList.Add("chair");

            int total = 0;

            for (var idx = 0; idx < boxingList.Count; idx++) {
                if ( boxingList[idx] is int ) {
                    int item = (int)boxingList[idx];
                    total += item;
                    Console.WriteLine(item + " is an integer");
                }
                else if ( boxingList[idx] is string) {
                    string item = boxingList[idx].ToString();
                    Console.WriteLine(item + " is a string");
                }
                else if ( boxingList[idx] is bool) {
                    bool item = (bool)boxingList[idx];
                    Console.WriteLine(item + " is a boolean");
                }
                else {
                    Console.WriteLine("You get that out of my house!");
                }
            }


            Console.WriteLine("total: " + total);
        }
    }
}
