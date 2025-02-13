using System;

namespace Расписание10;

public static class Program
{
    public static void Main()
    {
        int c = 10;
        string[] mon = { "Разговоры о важном 105\n", "Английский 310\n", "Русский язык 301\n", "Алгебра 303\n", "Геометрия 303\n", "История 308\n", "Физ-ра\n", "Литература 113\n" };
        string[] tue = { "Физика 209\n", "Физика 209\n", "Алгебра 303\n", "Геометрия 303\n", "Обществознание 308\n", "Литература 113\n", "Информатика 208\n" };
        string[] wed = { "\n", "Биология 309\n", "Химия 306\n", "Физика 209\n", "Физика 209\n", "Литература 113\n", "История 308\n", "Английский 310\n" };
        string[] thu = { "Разговоры о важном 105\n", "Русский 301\n", "ВиС 209\n", "Алгебра 303\n", "Физика 209\n", "Физика 209\n", "География 317\n" };
        string[] fri = { "Проект 206\n", "Обществознание 308\n", "ОБЖ 319\n", "Алгебра 303\n", "Геометрия 303\n", "Физ-ра\n", "Английский 310\n" };
        double[] call = { 8.05, 8.55, 9.50, 10.45, 11.45, 12.45, 13.35, 14.25, 15.15 };
        double[] call2 = { 8.45, 9.35, 10.30, 11.25, 12.25, 13.25, 14.15, 15.05, 15.55 };
        while (true)
        {
            DateTime date = DateTime.Now;

            String h2 = DateTime.Now.ToString("HH");
            String m2 = DateTime.Now.ToString("mm");
            int day = Convert.ToInt32(date.DayOfWeek);

            int h = Convert.ToInt32(h2);
            Double m = Convert.ToDouble(m2);
            Double hm = h + m / 100;

            Console.WriteLine("{0}\n", date);

            for (int i = 0; i < call.Length; i++)
            {
                if ((call[i] <= hm) & (hm <= call2[i]))
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                }
            }

            if (day == 1)
            {
                for (global::System.Int32 i = 0; i < mon.Length; i++)
                {
                    if (hm <= call2[i])
                    {
                        c = i;
                        break;
                    }
                }
                for (global::System.Int32 i = 0; i < mon.Length - c; i++)
                {
                    Console.WriteLine(mon[i + c]);
                    Console.ResetColor();
                }
            }
            else if (day == 2)
            {
                for (global::System.Int32 i = 0; i < tue.Length; i++)
                {
                    if (hm <= call2[i])
                    {
                        c = i;
                        break;
                    }
                }
                for (global::System.Int32 i = 0; i < tue.Length - c; i++)
                {
                    Console.WriteLine(tue[i + c]);
                    Console.ResetColor();
                }
            }
            else if (day == 3)
            {
                for (global::System.Int32 i = 0; i < wed.Length; i++)
                {
                    if (hm <= call2[i])
                    {
                        c = i;
                        break;
                    }
                }
                for (global::System.Int32 i = 0; i < wed.Length - c; i++)
                {
                    Console.WriteLine(wed[i + c]);
                    Console.ResetColor();
                }
            }
            else if (day == 4)
            {
                for (global::System.Int32 i = 0; i < thu.Length; i++)
                {
                    if (hm <= call2[i])
                    {
                        c = i;
                        break;
                    }
                }
                for (global::System.Int32 i = 0; i < thu.Length - c; i++)
                {
                    Console.WriteLine(thu[i + c]);
                    Console.ResetColor();
                }
            }
            else if (day == 5)
            {
                for (global::System.Int32 i = 0; i < fri.Length; i++)
                {
                    if (hm <= call2[i])
                    {
                        c = i;
                        break;
                    }
                }
                for (global::System.Int32 i = 0; i < fri.Length - c; i++)
                {
                    Console.WriteLine(fri[i + c]);
                    Console.ResetColor();
                }
            }
            Console.ReadLine();
            Console.Clear();
        }
    }
}