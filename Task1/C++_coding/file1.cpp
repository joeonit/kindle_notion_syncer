/******************************************************************************

q-Write a C++ program to find the factorial of a given number using a recursive function.

prerequisite consepts
> recursive function : is a function that calls itself in its own definition
> factorial : !n a mathametical way to represents the multiplication of all numbers between 1 and n !3= 3x2x1

trace example
> user enters the number 3 and it stores the value in the variable num
> when it outputs the result, it makes a call to the function "fact" with n=num=3
> the function checks if n=0, which is not true, so it continues to the recursive part
> it returns 3 x fact(2) = 3 x (2 x fact(1)) = 3 x 2 x (1 x fact(0)) = 3 x 2 x 1 x fact(0)
> the value is outputed to the user "Factorial is: 6"

*******************************************************************************/

#include<iostream>
using namespace std;

int fact(int n) {
    
    // stop the Recursion when n = 0 
    if ( n == 0 ) {
        return 1;
    }
    
    // recursive part
    else {
        return n * fact(n - 1);
    }
}

int main() {
    
    int num;
    cout << "Enter a number ";
    cin >> num;


    cout << "Factorial is: " << fact(num) << endl;
    
    
    return 0;
    
    
}


