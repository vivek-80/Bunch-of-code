import java.util.Scanner;
class Hour{
public static void main(String a[]){
int stH,enH,stmin,enmin,t,durat=0,minute=0,minus,plus,time;
String s2="Hour";
String s3="minute";
Scanner s1=new Scanner(System.in);
System.out.print("Enter how many times you calculate duration");
t=s1.nextInt();
for(int i=0;i<t;i++){
System.out.print("Enter the starting Hour & minute and ending hour & minute");
stH=s1.nextInt();
stmin=s1.nextInt();
enH=s1.nextInt();
enmin=s1.nextInt();
if(stH<=12 && enH<=12){
if(enH>stH){
durat=(enH-1)-stH;}
if(stH>enH && stH<=12){
durat=(12-stH)+enH;}
if(stmin>=enmin || enmin>=stmin){
minus=60-stmin;
minute=minus+enmin;
if(minute>60){
time=minute-60;
durat++;
System.out.print(+durat+" "+s2);
System.out.print(" "+time+" "+s3);
break;
}
if(stmin==enmin && enmin==stmin){
durat++;}
if(stH>enH && stH<=12){
durat--;}
System.out.print(+durat +" "+s2);
}
if(stmin==enmin && enmin==stmin){
break;}
System.out.println(" "+minute+" "+s3);
}
}
}
}
                                                                    




