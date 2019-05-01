using System;

namespace basic_13
{
    class Program
    {
        static void Main(string[] args)
        {
            // int[] Array = OddArray();
            // for (int idx = 0; idx < Array.Length; idx++){
            //     Console.WriteLine(Array[idx]);
            // }

            int[] testArray = { 1, 45, -30, 89, -125, 893 };
            // Console.WriteLine(GreaterThanY(testArray, 46));


            // int[] test = SquareArrayValues(testArray);
            // for (int idx=0;idx<test.Length;idx++){
            //     Console.WriteLine(test[idx]);
            // }


            // int[] test = EliminateNegatives(testArray);
            // for (int idx=0;idx<test.Length;idx++){
            //     Console.WriteLine(test[idx]);
            // }

            // int[] test = ShiftValues(testArray);
            // for (int idx=0;idx<test.Length;idx++){
            //     Console.WriteLine(test[idx]);
            // }

            object[] num = NewMethod(testArray);
            for (int idx = 0; idx < num.Length; idx++)
            {
                Console.WriteLine(num[idx]);
            }

        }

        private static object[] NewMethod(int[] testArray)
        {
            return NumToString(testArray);
        }

        public static void PrintNumbers(){
            for (int num = 1; num <= 255; num++){
                Console.WriteLine(num);
            }
        }

        public static void PrintOdds(){
            for (int num = 1; num <= 255; num++){
                if (num % 2 == 1){
                    Console.WriteLine(num);
                }
            }
        }

        public static void PrintSum(){
            int total = 0;
            for (int num = 1; num <= 255; num++){
                total += num;
                Console.WriteLine("New Number: " + num + " Sum: " + total);
            }            
        }

        public static void LoopArray(int[] numbers){
            for (int idx = 0; idx < numbers.Length; idx++){
                Console.WriteLine(numbers[idx]);
            }
        }

        public static void FindMax(int[] numbers){
            int maxNum = numbers[0];
            for (int idx = 0; idx < numbers.Length; idx++){
                if (numbers[idx] > maxNum){
                    maxNum = numbers[idx];
                }
            }
            Console.WriteLine(maxNum);
        }

        public static void GetAverage(int[] numbers){
            int total = 0;
            for (int idx = 0; idx < numbers.Length; idx++){
                total += numbers[idx];
            }
            Console.WriteLine(total/numbers.Length);
        }

        public static int[] OddArray(){
            int[] NewArray = new int[128];
            int idx = 0;
            for (int num = 1; num <= 255; num++){
                if (num % 2 != 0){
                    NewArray[idx] = num;
                    idx += 1;
                }
            }
            return NewArray;
        }

        public static int GreaterThanY(int[] numbers, int y){
            int totalAboveY = 0;
            for (int idx=0;idx<numbers.Length;idx++){
                if (numbers[idx] < y){
                    totalAboveY += 1;
                }
            }
            return totalAboveY;
        }

        public static int[] SquareArrayValues(int[] numbers){
            for (int idx=0;idx<numbers.Length;idx++){
                // int temp = numbers[idx];
                numbers[idx] *= numbers[idx];
            }
            return numbers;
        }

        public static int[] EliminateNegatives(int[] numbers){
            for (int idx=0;idx<numbers.Length;idx++){
                if (numbers[idx] < 0){
                    numbers[idx] = 0;
                }
            }
            return numbers;
        }

        public static void MinMaxAverage(int[] numbers){
            int min = numbers[0];
            int max = numbers[0];
            int total = numbers[0];
            for (int idx=1;idx<numbers.Length;idx++){
                if (numbers[idx] > max){
                    max = numbers[idx];
                }
                if (numbers[idx] < min){
                    min = numbers[idx];
                }                
                total += numbers[idx];
            }
            Console.WriteLine("Smallest Number: " + min + " Largest Number: " + max + " Average of all numbers: " + (total / numbers.Length));
        }

        public static int[] ShiftValues(int[] numbers){
            for (int idx=1;idx<numbers.Length;idx++){
                numbers[idx-1] = numbers[idx];
            }
            numbers[numbers.Length-1] = 0;
            return numbers;
        }

        public static object[] NumToString(int[] numbers){
            object[] BoxedNums = new object[numbers.Length];
            for (int idx=0;idx<numbers.Length;idx++){
                if (numbers[idx] < 0){
                    BoxedNums[idx] = "Dojo";
                }
                else{
                    BoxedNums[idx] = numbers[idx];
                }
            }
            return BoxedNums;
        }
    }
}
