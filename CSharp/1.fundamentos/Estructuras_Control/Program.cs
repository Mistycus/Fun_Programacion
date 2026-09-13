using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Estructuras_Control
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Estructuras de Control");

            // Secuencial
            string nombre;
            int edad;
            Console.WriteLine("Ingrese su Nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("Ingrese su Edad: ");
            edad = int.Parse(Console.ReadLine());

            Console.WriteLine($"Nombre: {nombre}, Edad : {edad}");



            // Condicionales
            // Simple
            if (edad < 18)
            {
                Console.WriteLine("Eres menor de edad ");
            }
            // doble
            if (edad >= 18)
            {
                Console.WriteLine("Eres mayor de edad");
            }
            else
            {
                Console.WriteLine("Eres menor de edad");
            }
            //Condicionales Multiples
            Console.WriteLine("Ingrese un numero del 1 al 3 :");
            int opcion = int.Parse(Console.ReadLine());
            switch (opcion)
            {
                case 1: Console.WriteLine("Opcion 1"); break;
                case 2: Console.WriteLine("Opcion 2"); break;
                case 3: Console.WriteLine("Opcion 3"); break;
                default: Console.WriteLine("Opcion Invalida"); break;
            }
            // Condicionales Anidado 

            if (opcion == 1)
            {
                Console.WriteLine("opcion 1");

            }
            else if (opcion == 2)
            {
                Console.WriteLine("opcion 2");
            }
            else
            {
                Console.WriteLine("opcion 3");
            }

            // Repetitivos
            // for 
            for (int i = 0; i < 10; i++)
            {
                Console.Write($"Numero : {i}");


            }
            // while
            int contador = 1;
            while (contador <= 3)
            {
                Console.WriteLine($"Intento : {contador}");
                contador++;
            }

            //do While
            int contador2 = 1;
            do
            {
                Console.WriteLine($"Intento: {contador2}");
                contador2++;
            } while (contador2 <= 3);
        }

    }
}
