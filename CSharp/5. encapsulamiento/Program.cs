Console.WriteLine("-----Encapsulamiento-----");

// Restringir  accseso a campo de valores 
ctaAhorros cuenta= new  ctaAhorros("Elvis ", 1500.00m);
cuenta.depositar(500);
cuenta.mostrar_saldo();

public class ctaAhorros
{
    public string titular ;
    private decimal saldo ;

    public ctaAhorros(string titular , decimal saldoInicial)
    {
        this.titular = titular;
        this.saldo = saldoInicial;
    }
public void depositar(decimal monto)
{
    if (monto > 0)
        {
            saldo += monto;
        }
}
public void mostrar_saldo()
    {
        Console.WriteLine($"titular : {titular}");
        Console.WriteLine($"Saldo : {saldo:f2}");
    }
}

