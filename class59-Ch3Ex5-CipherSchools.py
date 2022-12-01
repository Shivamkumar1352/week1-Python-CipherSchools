# ask user for name 
# example - "Apoorv"
#print count of each words
# output:
        #   A : 1
        #   P : 1
        #   o : 2
        #   o : 2
        #   r : 1
        #   v : 1
        
        
# ans :
name =input("enter your name : ")
# Apoorv
# name.count("a") , name.count(name[0]) = 1
# name.count("p") , name.count(name[1]) = 1
# name.count("o") , name.count(name[2]) = 2
# name.count("0") , name.count(name[3]) = 2
# name.count("r") , name.count(name[4]) = 1
# name.count("v") , name.count(name[5]) = 1

#output
        
i = 0
temp_var = ""
while i< len(name):
    if name[i] not in temp_var:
        temp_var +=name[i] 
        print(f"{name[i]} : {name.count(name[i])}")
        i+=1
