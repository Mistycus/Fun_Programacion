
using System.ComponentModel;
using System.Security.Cryptography.X509Certificates;

Console.WriteLine("operacopnes con arreglos");
 Console.WriteLine("operacopnes insersion");
// inserte en posision espesifica de lista

 List<string> productos = new List<string> {"teclado", "mouse","laptop"};
        productos.Insert(1 , "parlantes");
        Console.WriteLine(string.Join(",", productos));

// insercion al final de la lista

productos.Add("refrigeradora");
Console.WriteLine(string.Join(",",productos));

// insercion  multiple 

productos.AddRange(new List<string> {"hp", "dell", "asus" , "lenovo","hp"});
Console.WriteLine(string.Join(",",productos));

 Console.WriteLine("----------operacopnes de busqueda---------");
 // Busqueda
if (productos.Contains("hp"))
{
    int posision=productos.IndexOf("hp");
    Console.WriteLine($"encontrado en la posision  : {posision} ");
}
else
{
    Console.WriteLine("producto  no encontrado ");
}

// Equivalen in 
Console.WriteLine($"contiene productos hp : {productos.Contains("hp")}");
// primera posicion 
Console.WriteLine($"hp se encuentra en la posision {productos.IndexOf("hp")}");
// cantidad de repeticiones
Console.WriteLine($"producto hp se repite : {productos.Count(x =>x == "hp")} veces");

Console.WriteLine("----------operacopnes de modificacion---------");
// modificacionen posision 
productos[5] ="Nvidia";
Console.WriteLine(string.Join(";", productos));

// modificacion masiva

List<double> notas = new List<double>{12.9,14.3,19.1,11.49};
for(int i=0 ; i < notas.Count; i++)
{
    notas[i] = notas[i] + 0.9;
}
Console.WriteLine(string.Join(",",notas));

// modificacion por segmento 
for (int j=0 ; j <=3; j++)
{
    productos[j]= productos[j].ToUpper();
}
Console.WriteLine(string.Join(",",productos));

// modificacion trasformacion Masiva
List<double> salarios = new List<double> {200,1560,2700,4000};
salarios = salarios.Select(salario => salario > 1900 ? salario * 1.1 :salario ).ToList();
Console.WriteLine(string.Join("," , salarios));

Console.WriteLine("----------operacopnes de eliminacion ---------");

// eliminar de  un valor

productos.Remove("refrigeradora");
Console.WriteLine(string.Join("," , productos));

//eliminacion por indice
productos.RemoveAt(1);
Console.WriteLine(string.Join("," , productos));

// eliminar por rango 
productos.RemoveRange(1,2);
Console.WriteLine(string.Join("," , productos));

// eliminacion por criterio

List<int> datos = new List<int> {11,11,20,18,11,20,17,16};
datos.RemoveAll(x=> x == 11);
Console.WriteLine(string.Join("," , datos));

// vaciar  la lista

salarios.Clear();
Console.WriteLine(string.Join("," , salarios));