#include<iostream>
using namespace std;

int fib(int n){
    if(n==0) return 0;
    else if(n==1) return 1;
    else{
        return fib(n-1)+fib(n-2);
    }
}
int main(){
    int n;
    cout<<"Enter n: ";
    cin>>n;
    int ch;
    cout<<"1.recursive \n 2.non recursive";
    cin>>ch;
    if(ch==1){
        for (int i=0;i<n;i++)
        {
            cout<<fib(i)<<" ";
        }
    }
    else if(ch==2){
        int a=0;
        int b=1;
        for(int i=0;i<n;i++){
            cout<<a<<" ";
            c=a+b;
            a=b;
            b=c;
           
        }

    }
    return 0;
}