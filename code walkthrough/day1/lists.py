lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# .extend() --> adds another list 
friends.extend(lucky_numbers)

# .appendd() --> adds another value into end of list
friends.append("Creed")

# .insert(index num, *value*) --> adds another value in indicated index num
friends.insert(1, "Joe")

# .remove() --> removes element in list
friends.remove("Jim")

# .clear() --> removes all elements 
friends.clear()

# .pop() --> removes last element in list
friends.pop()

# .index() --> output index num of element
friends.index("element in list")

# .count(element in list) --> outputs how many times 
friends.count("Jim")

# .sort() --> ascending or alphebetical order
friends.sort()

# .reverse() --> reverses order of list
friends.reverse()

# .copy() --> takes a copy of list 
friends2 = friends.copy()