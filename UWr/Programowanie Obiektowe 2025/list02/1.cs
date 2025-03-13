using System;
using System.Text;


//ZAD 1
class IntStream
{
    protected int current;
    protected bool ended;

    public IntStream()
    {
        current = 0;
        ended = false;
    }

    public virtual int Next()
    {
        if (ended) throw new InvalidOperationException("End of stream");
        if (current == int.MaxValue) ended = true;
        return current++;
    }

    public bool Eos() => ended;

    public void Reset()
    {
        current = 0;
        ended = false;
    }
}

class FibStream : IntStream
{
    private int prev;

    public FibStream()
    {
        prev = 0;
        current = 1;
    }

    public override int Next()
    {
        if (Eos()) throw new InvalidOperationException("End of stream");
        

        int temp = current;
        current += prev;
        prev = temp;
        return prev;
    }

    public new bool Eos()
    {
        if (current > int.MaxValue - prev)
        {
            ended = true;
        }
        return ended;
    }
    public new void Reset()
    {
        prev = 0;
        current = 1;
        ended = false;
    }
}

class RandomStream : IntStream
{
    private Random rand;
    
    public RandomStream()
    {
        rand = new Random();
    }

    public override int Next()
    {
        return rand.Next();
    }

    public new bool Eos() => false;
}

class RandomWordStream
{
    private FibStream fibStream;
    private RandomStream randStream;
    private Random rand;

    public RandomWordStream()
    {
        fibStream = new FibStream();
        randStream = new RandomStream();
        rand = new Random();
    }

    public string Next()
    {
        int length = fibStream.Next();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++)
        {
            sb.Append((char)('a' + rand.Next(26)));
        }
        return sb.ToString();
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("Test IntStream:");
        IntStream intStream = new IntStream();
        for (int i = 0; i < 5; i++)
            Console.WriteLine(intStream.Next());
        intStream.Reset();
        Console.WriteLine(intStream.Next());

        Console.WriteLine("\nTest FibStream:");
        FibStream fibStream = new FibStream();
        for (int i = 0; i < 10; i++)
            Console.WriteLine(fibStream.Next());
        fibStream.Reset();
        Console.WriteLine(fibStream.Next());

        Console.WriteLine("\nTest RandomStream:");
        RandomStream randomStream = new RandomStream();
        for (int i = 0; i < 5; i++)
            Console.WriteLine(randomStream.Next());

        Console.WriteLine("\nTest RandomWordStream:");
        RandomWordStream rws = new RandomWordStream();
        for (int i = 0; i < 5; i++)
            Console.WriteLine(rws.Next());
    }
}
// KONIEC ZAD 1