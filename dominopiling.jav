import java.util.*;
 
public class domino {
 
    public static int domin(int m, int n) {
        int c=(m * n / 2);
        return c;
    }
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       int a = sc.nextInt();
       int b = sc.nextInt();
        System.out.println(domin( a,b));
 
 
    }
    
}