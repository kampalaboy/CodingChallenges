using System;

bool isPalindrome(int n){
    int reversedNumber = 0;
    int number = n;

    while(number > 0){
        int digit = number %10;
        reversedNumber =reversedNumber *10 + digit;
        number /= 10;
    }
    if (reversedNumber == n){
        return true;
    }
    return false;
} 

Console.WriteLine(isPalindrome(2002));