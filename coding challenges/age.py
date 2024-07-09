def countItem(arr):
    hashi = {}
    
    for i in arr :
        name = i.get('Name')
        age = i.get('Age')

        if name and age in hashi:
            hashi[age].append(name)
        else:
            hashi[age] = [name]
    return hashi

arr =[{'Name':'K', 'Age':10},
       {'Name':'L', 'Age':10},
       {'Name':'M', 'Age':10},
       {'Name':'N','Age':20},
       {'Name':'O','Age':50},
       {'Name':'P','Age':40},
       {'Name':'Q', 'Age':50}]
print(countItem(arr))