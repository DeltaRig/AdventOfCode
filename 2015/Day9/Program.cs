/**  .NET Core 3.1 SDK (v3.1.410)   */
using System;
using System.Collections.Generic;

namespace Day9 {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Hello World!");
            string[] lines = System.IO.File.ReadAllLines(@".\entrada.txt");

            String[] cidades = new string[7]; //valor olhado, poderia ser programado
            int[] menores = new int[7];
            int cont = 0;
            string cidadeTemp = "";
            int menorDaCidade = 0; //assim que chegar na primeira linha ganho novo valor

            List<int> organizaNum = new List<int>();
            

            foreach (string line in lines) {
                String[] arr = line.Split(" ");
                
                organizaNum.Add(Int32.Parse(arr[arr.Length -1]));

                if(cidadeTemp.CompareTo(arr[0]) != 0){
                    cidadeTemp = arr[0];
                    cidades[cont] = arr[0];

                    if(cont > 0){
                        menores[cont-1] = menorDaCidade;
                    }
                    cont++;

                    menorDaCidade = Int32.Parse(arr[arr.Length -1]);
                }

                if(menorDaCidade > Int32.Parse(arr[arr.Length -1])){
                    menorDaCidade = Int32.Parse(arr[arr.Length -1]);
                }

                if(lines[lines.Length -1] == line){
                    menores[cont-1] = menorDaCidade;
                }
                
        
            }

            for(int i = 0; i < cidades.Length; i++){
                Console.WriteLine("O menor caminho para sair de "+ cidades[i] + " é de " + menores[i] + "kms");
            }

            organizaNum.Sort();
            foreach(int num in organizaNum){
                Console.Write(num + " ");
            }

        }
    }
}
