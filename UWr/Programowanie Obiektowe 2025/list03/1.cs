using System;
using System.Collections.Generic;

// Abstrakcyjna klasa bazowa reprezentująca wyrażenie
abstract class Expression
{
    // Metoda abstrakcyjna do obliczania wartości wyrażenia
    public abstract int Evaluate(Dictionary<string, int> variables);

    // Metoda abstrakcyjna do obliczania pochodnej wyrażenia względem zmiennej
    public abstract Expression Derivate(string variable);
}

// Klasa reprezentująca stałą (liczbę)
class Const : Expression
{
    private int value; // Wartość stałej

    // Konstruktor inicjalizujący wartość stałej
    public Const(int value)
    {
        this.value = value;
    }

    // Metoda obliczająca wartość stałej (zawsze zwraca jej wartość)
    public override int Evaluate(Dictionary<string, int> variables)
    {
        return value;
    }

    // Metoda obliczająca pochodną stałej (pochodna stałej to zawsze 0)
    public override Expression Derivate(string variable)
    {
        return new Const(0);
    }
}

// Klasa reprezentująca zmienną
class Variable : Expression
{
    private string name; // Nazwa zmiennej

    // Konstruktor inicjalizujący nazwę zmiennej
    public Variable(string name)
    {
        this.name = name;
    }

    // Metoda obliczająca wartość zmiennej na podstawie słownika
    public override int Evaluate(Dictionary<string, int> variables)
    {
        // Jeśli zmienna istnieje w słowniku, zwróć jej wartość; w przeciwnym razie zwróć 0
        return variables.ContainsKey(name) ? variables[name] : 0;
    }

    // Metoda obliczająca pochodną zmiennej
    public override Expression Derivate(string variable)
    {
        // Pochodna zmiennej względem siebie to 1, względem innej zmiennej to 0
        return name == variable ? new Const(1) : new Const(0);
    }
}

// Klasa reprezentująca operację dodawania
class Add : Expression
{
    private Expression left, right; // Lewy i prawy operand

    // Konstruktor inicjalizujący operandy
    public Add(Expression left, Expression right)
    {
        this.left = left;
        this.right = right;
    }

    // Metoda obliczająca wartość wyrażenia jako sumę wartości lewego i prawego operandu
    public override int Evaluate(Dictionary<string, int> variables)
    {
        return left.Evaluate(variables) + right.Evaluate(variables);
    }

    // Metoda obliczająca pochodną sumy jako sumę pochodnych operandów
    public override Expression Derivate(string variable)
    {
        return new Add(left.Derivate(variable), right.Derivate(variable));
    }
}

// Klasa reprezentująca operację mnożenia
class Multiply : Expression
{
    private Expression left, right; // Lewy i prawy operand

    // Konstruktor inicjalizujący operandy
    public Multiply(Expression left, Expression right)
    {
        this.left = left;
        this.right = right;
    }

    // Metoda obliczająca wartość wyrażenia jako iloczyn wartości lewego i prawego operandu
    public override int Evaluate(Dictionary<string, int> variables)
    {
        return left.Evaluate(variables) * right.Evaluate(variables);
    }

    // Metoda obliczająca pochodną iloczynu zgodnie z regułą iloczynu
    public override Expression Derivate(string variable)
    {
        return new Add(
            new Multiply(left.Derivate(variable), right), // Pochodna lewego razy prawe
            new Multiply(left, right.Derivate(variable))  // Lewe razy pochodna prawego
        );
    }
}

// Klasa główna programu
class Program
{
    static void Main()
    {
        // Słownik przechowujący wartości zmiennych
        Dictionary<string, int> variables = new Dictionary<string, int> { { "x", 3 }, { "y", 2 } };

        // Przykład 1: Wyrażenie 4 + (x * 2)
        Expression expr1 = new Add(new Const(4), new Multiply(new Variable("x"), new Const(2)));
        Console.WriteLine("Wartość wyrażenia 1: " + expr1.Evaluate(variables)); // 4 + (3 * 2) = 10
        Console.WriteLine("Pochodna wyrażenia 1 względem x: " + expr1.Derivate("x").Evaluate(variables)); // 2

        // Przykład 2: Wyrażenie x * y
        Expression expr2 = new Multiply(new Variable("x"), new Variable("y"));
        Console.WriteLine("Wartość wyrażenia 2: " + expr2.Evaluate(variables)); // 3 * 2 = 6
        Console.WriteLine("Pochodna wyrażenia 2 względem x: " + expr2.Derivate("x").Evaluate(variables)); // 2
        Console.WriteLine("Pochodna wyrażenia 2 względem y: " + expr2.Derivate("y").Evaluate(variables)); // 3

        // Przykład 3: Wyrażenie (x * x) + 5
        Expression expr3 = new Add(new Multiply(new Variable("x"), new Variable("x")), new Const(5));
        Console.WriteLine("Wartość wyrażenia 3: " + expr3.Evaluate(variables)); // (3 * 3) + 5 = 14
        Console.WriteLine("Pochodna wyrażenia 3 względem x: " + expr3.Derivate("x").Evaluate(variables)); // 2 * 3 = 6
    }
}