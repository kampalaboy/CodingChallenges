#Can't skip over a gas[i] without incurring cost[i] to move from gas[i]:gas[i+1] 
#So if gas[i] = x and gas[i+y] where y = no.of gasStations before running out then we know journey from gas[i] to gas[i+y] is invalid
gas =  [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]
def station(gas, cost):
    remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            remaining = 0
    prev_remaining = sum(gas[:candidate])-sum(cost[:candidate])
    if candidate == len(gas) or remaining+prev_remaining<0:
        return -1
    else: 
        return candidate
        
print(station(gas,cost))