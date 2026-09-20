Console.WriteLine("Modularidad");
// modulos --> funciones espesificas
// Calcular productos

static string leer_producto()
{
    Console.Write("Ingrese nombre de un producto : ");
    return Console.ReadLine();
}
static double leer_precio()
{
    Console.Write("Ingrese precio de un producto: ");
    return double.Parse(Console.ReadLine());
}
static double calcular_igv(double precio)
{
    return precio * 0.18;
}
static void mostrar_resultado(string nombre , double precio,double igv)
{
    double total =precio + igv;
    Console.WriteLine($"producto : {nombre}");
    Console.WriteLine($"precio : {precio}");
    Console.WriteLine($"igv : {igv}");
    Console.WriteLine($"total a pagar : {total}");
}
string nombre = leer_producto();
double precio = leer_precio();
double igv = calcular_igv(precio);
mostrar_resultado(nombre , precio ,igv);
