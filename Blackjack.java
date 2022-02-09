import java.util.Scanner;

public class Blackjack {
    
    public static int blackjack(int a, int b) 
    {
        if(a==21)
        {
            return a;
        }
        else if(b==21)
        {
            return b;
        }
        else if(a>=b&&a<21)
        {
            return a;
        }
        else if(b>=a&&b<21)
        {
            return b;
        }
        else if(a<21&&b>21)
        {
            return a;
        }
        else if(b<21&&a>21)
        {
            return b;
        }
        else
        {
            return 0;
        }
    }

    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        scan.close();

        System.out.println(blackjack(a, b));
    }
}
