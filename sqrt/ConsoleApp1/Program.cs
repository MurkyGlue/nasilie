using System;

public class MainClass
{
    public static void Main()
    {
        // put your c# code here
        switch (int.Parse(Console.ReadLine())%2){
            case 1:
                Console.WriteLine("NO");
                break;
            case 0:
                Console.WriteLine("YES");
                break;}
    }
}
