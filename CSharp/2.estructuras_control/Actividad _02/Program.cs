using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Actividad__02
{
    internal class Program
    {
        static void Main(string[] args)// Funcion PRINCIPAL
        {
            for (int i = 0; i < 7; i++)
            {
                Console.Beep(1500,1000);
                RegistrarDatos();
                Console.Clear();//LIMPIAR CONSOL
                Console.ReadKey();//DETENER HASTA QUE ESCRIBAS ALGO
            }
             
        }//funcion 1
        static void RegistrarDatos() {
            Console.WriteLine("Ingrese su nombre: ");
            string nombre = Console.ReadLine();// ANA OLORTEGUI RODRIGUEZ

            Console.WriteLine("Ingrese su edad: ");
            int edad = int.Parse(Console.ReadLine());// 16 18
            DeterminarMayorEdad(edad);
        }
        //funcion2
        static void DeterminarMayorEdad(int edad) {
            if (edad >= 18)
            {
                Console.WriteLine("Eres mayor de edad");
            }
            else
            {
                Console.WriteLine("No eres mayor de edad");
            }

            Console.ReadKey();//DETENER HASTA QUE ESCRIBAS ALGO
        }
    }
}
