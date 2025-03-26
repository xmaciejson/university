using System;
using System.Collections;
using System.Collections.Generic;

// Główna klasa wyrażenia - tu dodajemy nowe funkcje
abstract class Expression : IEnumerable<Expression>
{
    // Te dwie metody już były - zostawiamy je bez zmian
    public abstract int Evaluate(Dictionary<string, int> variables);
    public abstract Expression Derivate(string variable);
    
    // 1. Nowa metoda - zamienia wyrażenie na string (np. do wypisywania)
    public abstract override string ToString();
    
    // 2. Metoda do porównywania czy dwa wyrażenia są takie same
    public abstract override bool Equals(object obj);
    
    // Musi być jak mamy Equals
    public abstract override int GetHashCode();
    
    // 4. Metoda do przeglądania wyrażenia jak listy
    public abstract IEnumerator<Expression> GetEnumerator();
    
    // To musi być - techniczna rzecz
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    
    // 3. Teraz dodajemy operatory + i * żeby ładniej pisać wyrażenia
    public static Add operator +(Expression left, Expression right) => new Add(left, right);
    public static Multiply operator *(Expression left, Expression right) => new Multiply(left, right);
}

// Klasa stałej liczby - np. Const(5)
class Const : Expression
{
    private int value;
    
    // 5. Magiczna mapa która trzyma wszystkie stworzone stałe
    private static readonly Dictionary<int, Const> cache = new Dictionary<int, Const>();
    
    // Zamiast konstruktora używamy tej metody - ona sprawdza czy już mamy taką stałą
    public static Const Create(int value)
    {
        if (!cache.ContainsKey(value))
            cache[value] = new Const(value);
        return cache[value];
    }
    
    // Konstruktor jest prywatny - trzeba używać Create()
    private Const(int value) => this.value = value;
    
    // Te metody zostają bez zmian
    public override int Evaluate(Dictionary<string, int> variables) => value;
    public override Expression Derivate(string variable) => Const.Create(0);
    
    // 1. Po prostu zwracamy liczbę jako tekst
    public override string ToString() => value.ToString();
    
    // 2. Dwie stałe są równe gdy mają tę samą wartość
    public override bool Equals(object obj) => obj is Const c && value == c.value;
    
    // Wymagane przy Equals
    public override int GetHashCode() => value.GetHashCode();
    
    // 4. Jak przeglądamy stałą, to tylko ją samą zwracamy
    public override IEnumerator<Expression> GetEnumerator()
    {
        yield return this;
    }
}

// Klasa zmiennej - np. Variable("x")
class Variable : Expression
{
    private string name;
    
    // 5. Taka sama magia jak ze stałymi - jedna instancja na nazwę
    private static readonly Dictionary<string, Variable> cache = new Dictionary<string, Variable>();
    
    public static Variable Create(string name)
    {
        if (!cache.ContainsKey(name))
            cache[name] = new Variable(name);
        return cache[name];
    }
    
    private Variable(string name) => this.name = name;
    
    // Te metody bez zmian
    public override int Evaluate(Dictionary<string, int> variables) => 
        variables.TryGetValue(name, out int val) ? val : 0;
    
    public override Expression Derivate(string variable) => 
        name == variable ? Const.Create(1) : Const.Create(0);
    
    // 1. Zwracamy nazwę zmiennej
    public override string ToString() => name;
    
    // 2. Dwie zmienne są równe gdy mają tę samą nazwę
    public override bool Equals(object obj) => obj is Variable v && name == v.name;
    
    public override int GetHashCode() => name.GetHashCode();
    
    // 4. Dla zmiennej też zwracamy tylko ją samą
    public override IEnumerator<Expression> GetEnumerator()
    {
        yield return this;
    }
}

// Klasa dodawania - np. Add(lewe, prawe)
class Add : Expression
{
    public Expression Left { get; }
    public Expression Right { get; }
    
    public Add(Expression left, Expression right)
    {
        Left = left;
        Right = right;
    }
    
    // Te metody bez zmian
    public override int Evaluate(Dictionary<string, int> variables) => 
        Left.Evaluate(variables) + Right.Evaluate(variables);
    
    public override Expression Derivate(string variable) => 
        Left.Derivate(variable) + Right.Derivate(variable);
    
    // 1. Zwracamy np. "(2 + x)"
    public override string ToString() => $"({Left} + {Right})";
    
    // 2. Dwa dodawania są równe gdy ich lewe i prawe części są równe
    public override bool Equals(object obj)
    {
        if (!(obj is Add other)) return false;
        return Left.Equals(other.Left) && Right.Equals(other.Right);
    }
    
    public override int GetHashCode() => (Left, Right).GetHashCode();
    
    // 4. Najpierw zwracamy siebie, potem lewą część, potem prawą
    public override IEnumerator<Expression> GetEnumerator()
    {
        yield return this;
        foreach (var e in Left) yield return e;
        foreach (var e in Right) yield return e;
    }
}

// Klasa mnożenia - bardzo podobna do Add
class Multiply : Expression
{
    public Expression Left { get; }
    public Expression Right { get; }
    
    public Multiply(Expression left, Expression right)
    {
        Left = left;
        Right = right;
    }
    
    // Bez zmian
    public override int Evaluate(Dictionary<string, int> variables) => 
        Left.Evaluate(variables) * Right.Evaluate(variables);
    
    public override Expression Derivate(string variable) => 
        Left.Derivate(variable) * Right + Left * Right.Derivate(variable);
    
    // 1. Zwracamy np. "(2 * x)"
    public override string ToString() => $"({Left} * {Right})";
    
    // 2. Tak samo jak w Add - porównujemy lewe i prawe części
    public override bool Equals(object obj)
    {
        if (!(obj is Multiply other)) return false;
        return Left.Equals(other.Left) && Right.Equals(other.Right);
    }
    
    public override int GetHashCode() => (Left, Right).GetHashCode();
    
    // 4. Iteracja tak samo jak w Add
    public override IEnumerator<Expression> GetEnumerator()
    {
        yield return this;
        foreach (var e in Left) yield return e;
        foreach (var e in Right) yield return e;
    }
}

class Program
{
    static void Main()
    {
        // Słownik wartości zmiennych
        var vars = new Dictionary<string, int> { { "x", 3 }, { "y", 2 } };

        
        Expression expr = Const.Create(4) + (Variable.Create("x") * Const.Create(2));
        
        // 1. Wypisze się ładnie dzięki ToString
        Console.WriteLine($"Wyrażenie: {expr}");  // (4 + (x * 2))
        Console.WriteLine($"Wynik: {expr.Evaluate(vars)}"); // 10
        
        // 2. Porównywanie działa
        Expression expr2 = Variable.Create("x") + Const.Create(2);
        Expression expr3 = Variable.Create("x") + Const.Create(2);
        Console.WriteLine($"Czy takie same? {expr2.Equals(expr3)}"); // True
        
        // 4. Możemy przelecieć po całym drzewie
        Console.WriteLine("\nWszystkie części wyrażenia:");
        foreach (var e in expr)
        {
            Console.WriteLine($"- {e.GetType().Name}: {e}");
        }
        
        // 5. Sprawdzamy czy działa cache stałych
        var c1 = Const.Create(5);
        var c2 = Const.Create(5);
        Console.WriteLine($"\nCzy to ta sama stała 5? {object.ReferenceEquals(c1, c2)}"); // True
    }
}