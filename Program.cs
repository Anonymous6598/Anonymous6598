using System;
using System.Numerics;

namespace Calculator
{
    class Program
    {
        static double plus(double number_1, double number_2)
        {
            double result = number_1 + number_2;
            return result;
        }
        static double minus(double number_1, double number_2)
        {
            double result = number_1 - number_2;
            return result;
        }

        static double multiply(double number_1, double number_2)
        {
            double result = number_1 * number_2;
            return result;
        }

        static double square_degree(double number)
        {
            double result = number * number;
            return result;
        }

        static double divide(double number_1, double number_2)
        {
            double result = 0;
            if (number_2 == 0)
            {
                result = number_1 / number_2;
            }

            else
            {
                result = number_2 / number_1;
            }

            return result;
        }

        static double square_root(double number)
        {
            double result = 0;
            if (number < 0)
            {
                Console.WriteLine("Can't find root from negative number");
            }

            else
            {
                result = Math.Sqrt(number);
            }

            return result;
        }
        static void exit() 
        {
            Environment.Exit(1);
        }
        static void Main(String[] args)
        {
            while (true)
            {
                Console.Write("Enter operation:");
                var operation = Console.ReadLine();
                switch (operation)
                {
                    case "+":
                        Console.Write("enter first number:");
                        var number_plus_1 = Console.ReadLine();
                        Console.Write("enter second number:");
                        var number_plus_2 = Console.ReadLine();
                        Console.WriteLine(plus(Convert.ToDouble(number_plus_1), Convert.ToDouble(number_plus_2)));
                        break;
                    
                    case "-":
                        Console.Write("enter first number:");
                        var number_minus_1 = Console.ReadLine();
                        Console.Write("enter second number:");
                        var number_minus_2 = Console.ReadLine();
                        Console.WriteLine(minus(Convert.ToDouble(number_minus_1), Convert.ToDouble(number_minus_2)));
                        break;
                    
                    case "*":
                        Console.Write("enter first number:");
                        var number_multiply_1 = Console.ReadLine();
                        Console.Write("enter second number:");
                        var number_multiply_2 = Console.ReadLine();
                        Console.WriteLine(multiply(Convert.ToDouble(number_multiply_1), Convert.ToDouble(number_multiply_2)));
                        break;
                    
                    case "/":
                        Console.Write("enter first number:");
                        var number_divide_1 = Console.ReadLine();
                        Console.Write("enter second number:");
                        var number_divide_2 = Console.ReadLine();
                        Console.WriteLine(divide(Convert.ToDouble(number_divide_1), Convert.ToDouble(number_divide_2)));
                        break;

                    case "**":
                        Console.Write("enter number:");
                        var number_degree = Console.ReadLine();
                        Console.WriteLine(square_degree(Convert.ToDouble(number_degree)));
                        break;

                    case "sqrt":
                        Console.Write("enter number:");
                        var number_square_root = Console.ReadLine();
                        Console.WriteLine(square_root(Convert.ToDouble(number_square_root)));
                        break;

                    case "exit":
                        exit();
                        break;
                }
            }

        }
    }
}