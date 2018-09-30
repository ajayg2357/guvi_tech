#include<stdio.h>
#include<conio.h>
void main()
{
int n,i,x;
clrscr();
printf("enter the number");
scanf("%d",&n);
for(i=1;i<=5;i++)
{
x=i*n;
printf(" %d",x);
}
getch();
}
