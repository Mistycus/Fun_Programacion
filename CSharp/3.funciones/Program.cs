using System.ComponentModel;

Console.WriteLine("--funciones--");
static void saludar()
{
    Console.WriteLine("hola, Bienbenido a Fundamentos");
}

saludar ();
Console.WriteLine("---------------------------------");
Console.WriteLine("funciones sin retorno");
Console.WriteLine("---------------------------------");
menu();

static void menu()
{
    Console.WriteLine("1 registar");
    Console.WriteLine("1 buscar");
    Console.WriteLine("1 salir");
}

Console.WriteLine("---------------------------------");
Console.WriteLine("FUNCIONES CON RETORNO");
Console.WriteLine("---------------------------------");

int resultado = prodcuto(8,7);
Console.WriteLine($"{resultado},resultado*2 ={resultado*2}");
static int prodcuto(int a, int b)
{
    return a*b;
}

Console.WriteLine("---------------------------------");
Console.WriteLine("FUNCIONES CON VARIOS ARGUMENTOS");
Console.WriteLine("---------------------------------");

static double promedio(double t1 ,double t2 , double t3 ,double ep , double ef)
{
    return t1 * 0.10 + t1 * 0.10 + t2 * 0.10 +t3 * 0*10 +ep * 0.20 + ef *0.50;
}
double prom = promedio(20 , 20, 20, 14 ,12);
Console.WriteLine($"promedio obtenido es : {prom}");

Console.WriteLine("---------------------------------");
Console.WriteLine("FUNCIONES CON VARIOS PARAMETROS PREDETERMINADOS");
Console.WriteLine("---------------------------------");

static void  saludar_estudiante(string nombre , string curso ="Fundamentos de programarcioin")
{
    Console.WriteLine($"hola {nombre}, bienvenido a { curso}");

}

saludar_estudiante("Elvis");
saludar_estudiante("Elvis" , "base de datos");

Console.WriteLine("---------------------------------");
Console.WriteLine("FUNCIONES ANIDADAS");
Console.WriteLine("---------------------------------");

static double proceso_compra (double monto)
{
    double aplicar_igv(double valor)
    {
        return valor * 0.18 ;

    }
    double igv = aplicar_igv(monto);
    double total = monto + igv;
    return total;

}

double venta = proceso_compra(550);
Console.WriteLine($"total a pagar  s/ . {venta}");

Console.WriteLine("---------------------------------");
Console.WriteLine("FUNCIONES PASOS PARAMETROS DE VALOR");
Console.WriteLine("---------------------------------");

static void incrementar(int numero)
{
    numero = numero + 5;
    Console.WriteLine($"dentro de la funcion : {numero}");
}

int z=25;
incrementar(z);
Console.WriteLine($"fuera de la funcion : {z}");

Console.WriteLine("---------------------------------");
Console.WriteLine("FUNCIONES   CON PARAMETROS POR REFERENCIA");
Console.WriteLine("---------------------------------");

static void incrementar_referencia (ref int numero)
{
    numero=numero +10;
    Console.WriteLine($"dentro de la funcion : {numero}");
}

int y=30;
incrementar_referencia(ref y);
Console.WriteLine($"fuera de la funcion : {y}");