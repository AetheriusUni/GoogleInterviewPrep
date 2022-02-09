import java.util.Scanner;
import java.util.Arrays;

public class evenlySpaced {

  public static boolean checkEven(int a, int b, int c) 
  {  
    int arr[] = {a, b, c};
    
    Arrays.sort(arr);
    int diff1 = arr[1]-arr[0];
    int diff2 = arr[2]-arr[1];
    
    if(diff1==diff2)
    {
      return true;
    }
    
    return false;
  }
  public static void main(String[] args)
  {
    /*int a = 2;
    int b = 4;
    int c = 6;*/
      
    Scanner scan = new Scanner(System.in);  // Create a Scanner object
    int a = scan.nextInt();  // Read user input
    int b = scan.nextInt();  // Read user input
    int c = scan.nextInt();  // Read user input
    scan.close();
      
    System.out.println("Evenly Spaced: " + checkEven(a, b, c));
  }
}
