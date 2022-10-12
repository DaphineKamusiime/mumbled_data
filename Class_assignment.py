mumbled_data = [["KATUKUNDA Rochelle","A94169","S21B23/016"],
["NAJJOBA Tracy","A95681","S21B23/034"],
["MUGANGA Charles","A96447","J22B23/032"],
["NKATA Joshua Luyombya","A94161","S21B23/008"],
["MUKISA Isaiah","A94160","S21B23/007"],["Afghanistan",93],
["Tiji",679],["Bahamas","1-242"],["Tanzania",255],
["Saint Vincent and the Grenadines","1-784"],["Ukraine",380]]#joining commom data

def linear_search(list,item):
    for i in list:##sub-lists in the entire list
        for j in i:##items in each sub-lists
            if item==j:
                return i
              
    return "not found"                   
print(linear_search(mumbled_data,7))
print(linear_search(mumbled_data,"A94160"))
print(linear_search(mumbled_data,380))
print(linear_search(mumbled_data,"Doe"))