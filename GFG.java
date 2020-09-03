import java.util.Scanner;
class GFG 
{ 
    static int multiply(){
    int n,i,pro = 1; ;
    Scanner s1=new Scanner(System.in);
    n=s1.nextInt();
    int arr[] =new int[n];
    for(i = 0; i < arr.length; i++) { 
      arr[i]=s1.nextInt();} 
        for (i = 0; i < arr.length; i++)  
            pro = pro * arr[i]; 
        return pro; 
    }
    public static void main(String[] args)  
    {
        System.out.println(multiply()); 
        } 
} 