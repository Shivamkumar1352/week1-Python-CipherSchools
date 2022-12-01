# ask user for name 
# example - "Shivam"
#print count of each words
# output:
        #   S : 1
        #   h : 1
        #   i : 2
        #   v : 2
        #   a : 1
        #   m : 1


#ans:
name = input("enter a name : ")
temp = "" 
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]

