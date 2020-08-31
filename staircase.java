/*    #
     ##
    ###
   ####*/
import java.util.Scanner;
class staircase{
	public static void main(String a[]){
      Scanner s1=new Scanner(System.in);
      int x=s1.nextInt();
      staircase(x);
	}
	public static void staircase(int x){
     /*for(int i=0;i<x;i++){
      	for(int k=x-i;k>=0;k--){
         if(k==0){
         	for(int j=0;j<=i;j++){
      	  System.out.print("*");}}
      	  else{
      	  	System.out.print(" ");
      	  } 
      	}
      	 System.out.println(); 
     }*/
     for(int i=0;i<x;i++){
      	for(int k=x;k>=i;k--){
         if(k==i){
         	for(int j=0;j<=i;j++){
      	  System.out.print("#");}}
      	  else{
      	  	System.out.print(" ");
      	  } 
      	}
      	 System.out.println(); 
     }
	}
}