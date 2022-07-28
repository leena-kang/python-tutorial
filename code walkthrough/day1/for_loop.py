friends = ["Kim", "Karen", "Kevin"]

# range() starts from 0 -> num 
# "index" -> can be named any variable 

for index in range(len(friends)): 
    print(friends[index])

for index in range(5): 
    if index == 0: 
        print ("first Iteration")
    else: 
        print("Not first") 