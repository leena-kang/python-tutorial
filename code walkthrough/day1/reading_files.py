# python read command -> allow to read file that is stored outside of python file 

# open command --> open( file or path of file you want to open, mode )

# MODES: 
# "r" -> read ; just read/not modify file
# "w" -> write ; can change, write new info in file (overrides everyting existing in file), so use to create NEW files
# "a" -> append ; can add/append new info
# "r+" -> read and write powers

employee_file = open("empolyees.txt", "r")
    #open() -> opening a file
    #storing file into a variable

print(employee_file.readlines()[1]) 
    #accessing certain lines in external file 

employee_file.write("Toby - Human Resources")
    # adds new info in the fifle 

employee_file.close()
    #close() -> closing a file, do this whenever you open a file

