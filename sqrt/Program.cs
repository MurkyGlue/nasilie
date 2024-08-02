namespace sqrt
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double b = Convert.ToDouble(Console.ReadLine()); //49
            int c = Convert.ToInt32(Console.ReadLine()); //2
            double s = 1.0;
            double r = 0;

            while(Convert.ToString(r).Length < 5)
            {
                if (Math.Pow(r, c) < b)
                {
                    r += s;
                }
                else if (Math.Pow(r, c) == b)
                {
                    break;
                }
                else
                {
                    r -= s;
                    s /= 10;
                }
            }

            Console.WriteLine(r);

        }
    }
}