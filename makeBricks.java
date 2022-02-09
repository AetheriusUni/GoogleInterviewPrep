import java.util.Scanner;

/*
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return true if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

makeBricks(3, 1, 8) → true
makeBricks(3, 1, 9) → false
makeBricks(3, 2, 10) → true
*/

public class makeBricks {
    public static boolean makeBrick(int small, int big, int goal) 
    {  
        int remInches = goal;
        int maxBigNeed = goal/5;
        int minSmallReq = goal%5;
        if(big>=maxBigNeed)
        {
            remInches-=5*maxBigNeed;
        }
        else
        {
            remInches-=5*big;
        }
        if(small<minSmallReq)
        {
            return false;
        }
        else
        {
            remInches-=small;
        }
        if(remInches>0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    public static void main(String[] args)
    {   
        Scanner scan = new Scanner(System.in);  // Create a Scanner object
        int big = scan.nextInt();  // Read user input
        int small = scan.nextInt();  // Read user input
        int goal = scan.nextInt();  // Read user input
        scan.close();   // close scanner
        System.out.println("Can we make the brick goal: " + makeBrick(big, small, goal));
    }
}
