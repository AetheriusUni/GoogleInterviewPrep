import java.util.Scanner;

class stringSplosion{
    public static String stringSploder(String str)
    {
        String sploded = "";
        String part = "";
        char[] strCharArr = str.toCharArray();
        for(int i = 0; i < strCharArr.length; i++)
        {
            part+=strCharArr[i];
            sploded+=part;
        }
        return sploded;
    }

    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        System.out.println(stringSploder(s));
    }
}
