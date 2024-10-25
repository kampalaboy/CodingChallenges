using System;
using System.Collections.Generic;
using System.Linq;

int station(int[] gas, int[] cost) {
    int remaining = 0;
    int candidate = 0;

    for (int i=0; i<gas.Length; i++) {
        remaining += gas[i] - cost[i];
        if (remaining < 0){
            candidate = i+1;
            remaining = 0;
        }
    }
  int prev_remaining = gas.Take(candidate).Sum() - cost.Take(candidate).Sum();
  if (candidate == gas.Count() || remaining+prev_remaining < 0){
    return -1;
  }else{
    return candidate;
  }
}
int[] gas = {1,5,3,3,5,3,1,3,4,5};
int[] cost = {5,2,2,8,2,4,2,5,1,2};

Console.WriteLine(station(gas, cost));