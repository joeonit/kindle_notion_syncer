/******************************************************************************

q-Create a C++ program that checks if a number is prime or not and displays the result.

prerequisite consepts
> prime numbers : is a natural numbers greater than 1 that is not a product of two smaller natural numbers, it starts with 2

*******************************************************************************/

#include<iostream>
using namespace std;

bool isPrime(int num) {
    // 0 and 1 are not prime numbers
    if (num <= 1) {
        return false;
    }

    // looking for a factor in the scope of i squared
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return false; // if factor is found, not a prime number
        }
    }

    return true; // no factors are found, it's a prime number
}

int main() {
    
    int number;
    cout << "Enter a number: ";
    cin >> number;

    if (isPrime(number)==true) {
        cout << number << " is a prime number" << endl;
    } else {
        cout << number << "is not a prime number" << endl;
    }

    return 0;
}


