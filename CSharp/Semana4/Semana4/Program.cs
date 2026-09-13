using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana4
{
    internal class Program
    {
        static int numeroPedidos = 0; //variable global
        static void Main(string[] args)
        {
            Console.WriteLine("-----MESA 1-----");
            MesaActiva();
            Console.WriteLine("-----MESA 2-----");
            MesaActiva();
            Console.Write("TOTAL DE PEDIDOS HOY:" + numeroPedidos);
        }

        static void MesaActiva()
        {
            int subtotalMesa = 0; //variable local
            string producto = ""; //variable local jugo,pan,cafe...
            Console.WriteLine("Ingrese los pedidos ('fin' para cerrar mesa):");
            producto = Console.ReadLine().ToLower(); //producto = cafe
            //pan != fin (true)
            while (producto!="fin") //for= true(N° veces) , while = true (logica > < == >= != null true)
            {
                Console.WriteLine("Producto: ");
                producto = Console.ReadLine().ToLower(); //producto = PAN
                RegistrarPedido(producto);
                numeroPedidos++; // ++ = incrementar su valor +1
            }
            void RegistrarPedido(string productoP)
            {
                string mensaje = "pedido registrado: " + productoP;//variable no local:  nace y muere en cada pedido
                subtotalMesa++;
            }

        }

    }
}
