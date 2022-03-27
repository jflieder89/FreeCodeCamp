import math # for remainder/modulo function
# sample lists of strings: [4 + 4]  ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(lst) :
    ##first programmed error message about exceeding 5 problems
    if len(lst) > 15:
        return print('Error: Too many problems.')
        quit()

    ##put in custom error message if two few items are added:
    if len(lst) < 3:
        print('Error: Please enter at least one full problem.')
        quit()

    ##put in a custom error message if lst is not a multiple of 3, meaning incomplete expressions were entered
    if len(lst) % 3 != 0:
        print('Error: Please enter complete expressions only. A complete expression is an operand number, then an operator, then a second operand number.')
        quit()

    number_of_items = len(lst) #number of items in the list
    number_of_expressions = int(number_of_items / 3) #get the number of problems/expressions


    ##!!After a lot of trouble, it seems way better to append each separete expression dictionary to a master list using iteration instead of create a new, separate expression dictionary with each iteration
    expressions_dict_lst = [] #create empty master list of expression dictionaries to be filled
    for n in list(range(0, number_of_expressions)): #to iterate through the expressions. # No need to modify the number_of_expressions integer since the ending variable is not inclusive in a list being iterated through
        #print(n)
        expression_dict = dict([ ("expression_number", n), ("operandA", []), ("operator", []), ("operandB", []), ("operandA_spaces", []), ("operandB_spaces", []), ("expression_length", []) ]) #create a dictionary for the expression being iterated for
        expressions_dict_lst.append(expression_dict) #Add in the dictionary to the master list

    ## !! print(expressions_dict_lst[0]["expression_number"]) ##!! Sample syntax for calling items in a dictionary from within a list!!

    ##Now need to add in all values to the master list:
    count  =  0
    for item in lst: #iterating through all of the items, whether they be numbers or operators, of the inputted list
        #test code#print('Current item is :', item)
        expression = int(count/3) # to see which expression this item is part of (to see what set of three items it is in to see what expression it is in)
        type_index = (count % 3) # to see if it is a first operand, an operator, or a second operand of the expression it is in

        if type_index == 0: #this means 'if it is an operandA', since that is the first item in an expression
            expressions_dict_lst[expression]["operandA"] =  item

            # Programed error code for non-number operands being inputted:
            try:
                item = int(item) # to turn this number from a string to a number
            except:
                return print('Error: Numbers must only contain digits.')
                quit()

            #Program error code for operand exceeding limit of 4 digits
            if len(str(item)) > 4 : # need to measure length of string. Caanot measure length of an integer
                return print('Error: Numbers cannot be more than four digits.')
                quit()

        elif type_index == 1: #this means 'if it is an operator', since that is the second item in an expression
            expressions_dict_lst[expression]["operator"] =  item

            #Programmed error message if the operator is not for addition or subtraction:
            if item != '-' and item != '+' :
                return print('Error: Operator must be ',"'+'",'or',"'-'.")
                quit()

        else: #this essentially means 'if it is an operandB', since that is the third item in an expression with modulo 3 of 2 (remainder of 2)
            expressions_dict_lst[expression]["operandB"] =  item

            # Program error code for non-number operands being inputted:
            try:
                item = int(item) # to turn this number from a string to a number
            except:
                return print('Error: Numbers must only contain digits.')
                quit()

            #Program error code for operand exceeding limit of 4 digits:

            if len(str(item)) > 4 : # need to measure length of string. Caanot measure length of an integer
                return print('Error: Numbers cannot be more than four digits.')
                quit()

            #Now establish how many characters wide the expression is. This will be the length of the longer of the two operands plus 2 to account for a space and the operator
            expressions_dict_lst[expression]["expression_length"] = max(len(expressions_dict_lst[expression]["operandA"]), len(expressions_dict_lst[expression]["operandB"])) + 2

            #Now can set spaces needed before each operand now that the total expression length is known
            expressions_dict_lst[expression]["operandA_spaces"] = expressions_dict_lst[expression]["expression_length"] - len(expressions_dict_lst[expression]["operandA"])
            expressions_dict_lst[expression]["operandB_spaces"] = expressions_dict_lst[expression]["expression_length"] - len(expressions_dict_lst[expression]["operandB"]) - 1 # -1 to account for operator on this line

        count = count + 1 #necessary to have expression and type move along with the iterations

    #Now to create print statements with proper placing and spacing
    #Note that you cannot append to a string like you can for lists. But you can add strings together!
    line1 = "" #Create empty top line list where operandAs and operandA_spaces will go
    line2 = "" #create empty second line list where operators, operandBspaces, and operandB's will go
    line3 = "" #create empty third line list for dashes under each expression/problem

    ##!! Now can start printing this thing
    for expression in range(number_of_expressions) : #to iterate through the number of expressions

        #For all expressions after the first one, need to separate the expressions by 4 spaces, added in before that expressions components:
        if expression > 0 :
            line1 = line1 + '    '
            line2 = line2 + '    '
            line3 = line3 + '    '
        #!!Need to turn operand_spaces integers into a string of of spaces:

        operandA_spaces_string_of_spaces = '' # setting up a new string empty string for each expression to be filled with the amount of spaces quantified by the operand*_spaces items in the dictionaries in the list
        #turn the spaces parameter into an integer if it's still a string so the range function can be used

        for space in range(expressions_dict_lst[expression]["operandA_spaces"]) :
            operandA_spaces_string_of_spaces = operandA_spaces_string_of_spaces + ' ' #add a new space

        expressions_dict_lst[expression]["operandA_spaces"] = operandA_spaces_string_of_spaces

        line1 = line1 + str(expressions_dict_lst[expression]["operandA_spaces"]) # add in operandAspaces first
        line1 = line1 + str(expressions_dict_lst[expression]["operandA"]) #add in operandA next

        line2 = line2 + str(expressions_dict_lst[expression]["operator"]) # add in operator

        #!!Need to turn operand_spaces integers into a string of of spaces:
        operandB_spaces_string_of_spaces = '' # setting up a new string for each expression to be filled with the amount of spaces quantified by the operand*_spaces items in the dictionaries in the list
        #turn the spaces parameter into an integer if it's still a string so the range function can be used
        #test code#print('OperandB_spaces for expression ', expression, 'is ',expressions_dict_lst[expression]["operandB_spaces"], "and it's type is ", type(expressions_dict_lst[expression]["operandB_spaces"]) )
        for space in range(expressions_dict_lst[expression]["operandB_spaces"]) :
            operandB_spaces_string_of_spaces = operandB_spaces_string_of_spaces + ' ' #add a new space
        #test code# print(operandB_spaces_string_of_spaces + "x")
        expressions_dict_lst[expression]["operandB_spaces"] = operandB_spaces_string_of_spaces
        #test code# print(expressions_dict_lst[expression]["operandB_spaces"] + 'x')
        #test code#print('OperandB_spaces for expression ', expression, 'is ',expressions_dict_lst[expression]["operandB_spaces"], "and it's type is ", type(expressions_dict_lst[expression]["operandB_spaces"]) )

        line2 = line2 + str(expressions_dict_lst[expression]["operandB_spaces"]) # add in operandB spaces
        line2 = line2 + str(expressions_dict_lst[expression]["operandB"]) # add in operandB

        ##! Need to add in number of dashes on line 3 equal to the length of the expression
        dashes_under_expression = ''
        for character in range(expressions_dict_lst[expression]["expression_length"]) :
            dashes_under_expression = dashes_under_expression + '-'
        line3 = line3 + dashes_under_expression

        #test code# print(line1, 'is the top line after the', expression, 'expression')
        #test code# print(line2, 'is the second line after the', expression, 'expression')
        #test code# print(line3, 'is the third line after the', expression, 'expression')
    print(line1)
    print(line2)
    print(line3)

    ##!!optional part to show the answers:
    line4 = '' #create empty string for answers to be inputted and eventually printed out below the expressions
    if answers_request == 'True' :
        answers_lst = [] #create an empty list of answers for my own curiosity
        for expression in range(number_of_expressions):

            #For all expressions after the first one, need to separate the expressions by 4 spaces, added in before that expressions components:
            if expression > 0 :
                line4 = line4 + '    '

            if expressions_dict_lst[expression]["operator"] == '+' :
                answer = int(expressions_dict_lst[expression]["operandA"]) + int(expressions_dict_lst[expression]["operandB"]) #turn the numbers into integers to do the math
            else : # this covers if '-' is the operator
                answer = int(expressions_dict_lst[expression]["operandA"]) - int(expressions_dict_lst[expression]["operandB"]) #turn the numbers into integers to do the math

            #Need to account for spacing of the answer from the left side of the expression:
            answer_spaces_integer = expressions_dict_lst[expression]["expression_length"] - len(str(answer)) #here is the number of spaces needed to be print to the left of the answer for it to line up
            answer_spaces_string = ''
            for digit in range(answer_spaces_integer):
                answer_spaces_string = answer_spaces_string + ' '

            answer = str(answer) #turn the answer back into a string so it is printable

            answers_lst.append(answer) ## To deal with append turning the list into non-type, I need to remember not to do this: answers_list = answers_list.append(answer). The equals sign is not needed and is syntatically wrong

            line4 = line4 + answer_spaces_string + answer
        print(line4)

    #return line1
    #return line2
    #return line3





lst = input('Enter your list of arithmetic problems: ') ##Note that this will be a string!!! Not a list!!! The input function only recognizes an input as a string, integer, or character
#test code# print('Here is the inputted list: ', lst)
#test code# print('It has type :', type(lst))
#test code# print()
##!!optional input to request to see the answers:
answers_request = input('Enter "True" without quotation marks if you would like to see the answers: ')

#Before turning this string into a list, cleaning up is required!!
lst = lst.replace("[", "")
lst = lst.replace("]", "")
lst = lst.replace("(", "")
lst = lst.replace(")", "")
lst = lst.replace("{", "")
lst = lst.replace("}", "")
lst = lst.replace("'", "")
lst = lst.replace('"', "")
lst = lst.replace(',', "")
#test code# print('Here is the cleaned up list: ', lst)
#test code# print('It has type :', type(lst))
#test code# print()

#Now can turn it into a list:
lst = lst.split()

#test code# print('Here is the cleaned up list split into an actual list: ', lst)
#test code# print('It has type :', type(lst))
#test code# print()

arithmetic_arranger(lst)
