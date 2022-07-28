## Python Tutorial Notes! 
Python Tutorial from Giraffe Academy Youtube Viideo "Learn Python - Full Courses for Beginners" 

DATA TYPES

    strings: " " 
    integers: *variable name* = 50 
    boolean: *var name* = False (capitalize F)
    floats = decimal num
    lists: [element, ..., ]
    tuple: (element, ... ,) --> immutable

OPERATIONS 

    % = outputs the remainder 
    ** = raise to the power of (exponent)
    // = floor division -> returns an int 
    
SYNTAX: 

    USER INPUT: 

     *var name* = input() 
            inside the (), enter prompt

     note: for user input, python defaults the input to a string value 
     
    FUNCTIONS: 
     def *name*(*parameters*): 

    IF STATEMENTS: 
        if *variable* : 
            *code* 
        elif *variable* : 
            *code* 
        else: 
            *code* 


    COMPARISON SYNTAX and OPERATORS
        not() --> equiv to ! in C++ 
        and, or --> and, or 
        >= , <= , < , > , == , != 

    DICTIONATIRES
        *name* = {
            *key*: *value*
        }

    LOOPS 
        while *condition* : 
            *code* 

        for *var/placeholder* in *definite # of iterations* (usually range()) : 
            *code to execute until the last term*

        break -> exits out of loop entirely
        continue -> exits out of loop back to the top/start

    COMMENTS 
        # -> for this line only

        ''' 
            *can comment, on multiple lines
        '''
    
    TRY/EXCEPT (for user invalid inputs)
        try: 
            *code* 
        except *specific error*: 
            *code* 
    
    CLASSES/OBJECT 
        class *Name* 
            def __init__ (*name*, parameters)
                *name*. *parameter* = 
                ...
                
        to import a class to a new file: 
            from *file name* import *class name* 