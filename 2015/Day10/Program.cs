/**  .NET Core 3.1 SDK (v3.1.410)   */
using System;

namespace Day10
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            String puzzle = "1211";
            char temp = puzzle[0];
            int cont = 0;

            String result = "";
            
            for(int i = 0; i < puzzle.Length; i++){
                if(temp.Equals(puzzle[i])){
                    cont++;
                } else {
                    result += cont + temp;
                    temp = puzzle[i];
                    cont = 0;
                }
            }

            Console.WriteLine(result);
        }
    }
}
