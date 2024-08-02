namespace sqrt
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double b = Convert.ToDouble(Console.ReadLine()); //start number
            int c = Convert.ToInt32(Console.ReadLine()); // number of degree
            double s = 1.0; //step
            double r = 0; //result

            for (int i = 0; i < 1000; i++)
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