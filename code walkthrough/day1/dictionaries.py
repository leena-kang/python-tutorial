# dictionaries: special structure in python that stores information in KEY VAL PAIRS ("key" = word, "val" = definition)
# be sure each key is UNIQUE

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March", 
    "Apr": "April", 
    "May": "May", 
    "Jun": "June", 
    "Jul": "July", 
    "Aug": "August", 
    "Sep": "September", 
    "Oct": "October", 
    "Nov": "November",
    "Dec": "December",
}

numMonthConver = {
    1: "January",
    2: "February",
    3: "March", 
    4: "April", 
    5: "May", 
    6: "June", 
    7: "July", 
    8: "August", 
    9: "September", 
    10: "October", 
    11: "November",
    12: "December",

}
print(monthConversions["Nov"])

print(monthConversions.get("Dec"))

# .get(key, default if key doesn't match in dictionary)
print(monthConversions.get("Luv", "Not a valid key"))

print(numMonthConver.get(1))