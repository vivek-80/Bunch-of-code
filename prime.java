/* prime number */
import java.util.Scanner;
class prime{
	public static void main(String a[]){
     Scanner sc=new Scanner(System.in);
     int x=sc.nextInt();
     if(m1(x)){
     	System.out.println("prime");
     }
     else{
     	System.out.println("not prime");
     }}
     static boolean m1(int x){
     	if(x<=1){
     		return false;}
     		else{
     		     for(int i=2;i<x;i++){
                   if(x%i==0){
     		     	return false;
     		     }
     		 }
     		return true;
     	}
}}
