
Console.WriteLine("Arreglos Unidimencionales");

// Declarando Arreglos
int [] numeros = new int [10];  // 10 Elementos
numeros[1] = 26;  // Insertar en la posision 1 el valor 26
numeros[9]= 11 ;  // Insertar en la posision 9 el valor 11

// Mostrar  el arreglo 
Console.WriteLine(string.Join("," , numeros));

// Declarando un arreglo de nombres
String[] nombres = new string[5];
nombres[0] = "Juan";
nombres[4] = "SUSANA";
Console.WriteLine(string.Join("," , nombres));

// Elemento e indice de arreglo 
Console.WriteLine($"Cantidad Elementos : {numeros.Length}");
Console.WriteLine($"Ultimo Elementos : {numeros[numeros.Length-1]}");

// El valor en un indice espesifico 
Console.WriteLine($"Nombres en la posision 4 es : {nombres[4]}");
Console.WriteLine($"Nombres en la posision 9 es : {numeros[9]}");

// Recorrer el arreglo 
for (int i=0 ; i< numeros.Length ; i++)
{
    Console.WriteLine($"Posision {i}: valor : {numeros[i]}");
}
for (int j=0 ; j < nombres.Length; j++)
{
    Console.WriteLine($"Posision {j}: valor : {nombres[j]}");
}

// Declarar arreglo bidimensional (Matriz)
 int[,] notas =
{
    {1,2,3,4} , // Arreglo 1
    {5,6,7,8} , // Arreglo 2
    {9,10,11,12} // Arreglo 3
};
// Mostrar  elemento fila 1 columa 3 (numero 8)
Console.WriteLine(notas[1,3]);

// Recorrer la matriz 
for (int filas = 0 ; filas < notas.GetLength(0); filas++)
{
    for ( int col = 0; col < notas.GetLength(1); col++)
    {
        Console.WriteLine($"Fila : {filas} , columna :{col} - valor : {notas[filas , col]}");
    }
}