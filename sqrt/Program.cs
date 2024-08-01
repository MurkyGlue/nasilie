namespace sqrt
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double b = Convert.ToDouble(Console.ReadLine()); //49
            int c = Convert.ToInt32(Console.ReadLine()); //2
            double s = 1.0;
            double i = 0;
            string r = "";

            for(int v = 0; v < 10; v++)
            {
                if (Math.Pow(i, c) < b)
                {
                    i += s;
                }
                else if (Math.Pow(i, c) == b)
                {
                    r += i;
                    break;
                }
                else
                {
                    i -= s;
                    r += i;
                    s /= 10;
                }
            }

            Console.WriteLine(r);

        }
    }
}