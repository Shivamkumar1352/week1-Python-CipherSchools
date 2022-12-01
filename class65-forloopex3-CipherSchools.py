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


#ans:
name = input("enter a name : ")
temp = "" 
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]

