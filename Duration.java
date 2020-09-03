import java.util.Scanner;
class Duration{
public static void main(String a[]){
Scanner s1=new Scanner(System.in);
int sh,sm,eh,em,t,m,h,e;
t=s1.nextInt();
for(int i=0;i<t;i++){
sh=s1.nextInt();
sm=s1.nextInt();
eh=s1.nextInt();
em=s1.nextInt();
if(sm<=60)
{
 m=60-sm;
 e=em+m;
 if(sm==00 && eh==00)
{
 h=sh-eh;
 h++;
 System.out.println(+e);
 System.out.println(+h);
}
}
else
{
 h=sh-eh;
 h--;
 /*System.out.println(+e);*/
 System.out.println(+h);
}
}
}
}
 

 
 
 

