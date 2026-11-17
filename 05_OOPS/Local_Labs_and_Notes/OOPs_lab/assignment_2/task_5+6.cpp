#include<bits/stdc++.h>
using namespace std;
inline long long factorial(int n){
  if(n==0 || n==1){
    return 1;
  }
  else{
    for(int i=n-1;i>=1;i--){
      n*=i;
    }
    return n;
  }
}
int main(){
  cout<<factorial(5)<<endl;
  cout<<factorial(493)<<endl;
}
// Although this function is marked inline, it may not be  good 
// for inlining the loop length depends on n, so for large inputs the
// function does a lot of work. If called many times, inlining could also be called the same number of times
// increase the size of the generated code. The compiler can decide whether actual inlining is beneficial
#include <iostream>
using namespace std;

inline bool isPrime(int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main()
{
    for (int i = 1; i <= 50; i++)
    {
        if (isPrime(i))
            cout << i << " ";
    }
    return 0;
}

/*
Although isPrime() is called many times in the loop,using inline may not be very beneficial because the function contains a loop itself. The compiler may choose not to inline it, as the amount of work depends on the input.
*/