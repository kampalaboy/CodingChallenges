using System;
using System.Collections.Generic;
using System.Numerics;

Dictionary<int, bool> memo = new Dictionary<int, bool>();

bool CanSum (int target, List<int> numbers){
    if (memo.ContainsKey(target)){
        return memo[target];
    }
    if( target == 0){
        return true;
    }
    if( target < 0 ){
        return false; 
    }

    foreach (int num in numbers){
        int r = target - num;
        if (CanSum(r, numbers)) {
            memo[target] = true;
            return true;
        }
    }
    memo[target]=false;
    return false;
}

try {

List<int> numbers = new List<int>{150};
Console.WriteLine(CanSum(300,numbers));

}catch(Exception ex){

    Console.WriteLine(ex.Message);
}