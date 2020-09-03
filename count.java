import java.util.Scanner;
class Count{
public static void main(String a[]){
int l,r,k,i,count=0;
Scanner s1=new Scanner(System.in);
l=s1.nextInt();
r=s1.nextInt();
k=s1.nextInt();
for(i=l;i<=r;i++)
if(i%k==0)
{
 count++;
}
System.out.println(+count);
}
}


