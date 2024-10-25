using System;

string[] fizzbuzz(int n){
    string[] arr = new string[n];
    for(int i = 1; i<=n; i++){
        if( i % 3 == 0 && i % 5==0){
            arr[i-1] = "fizzbuzz";
        }
        else if(i % 3 == 0 ){
            arr[i-1] = "fizz";
        }
        else if (i % 5 == 0){
            arr[i-1] = "buzz";
        }else{
            arr[i-1] = i.ToString();
        }
    }
    return arr;
}

int n = 15;
string[] result = fizzbuzz(n);
Console.WriteLine(string.Join(", ", result));