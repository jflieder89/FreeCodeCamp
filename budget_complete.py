import math

class Category:


    def __init__(self, name): # so it is named upon creation/initialization
        self.name = name
        self.ledger = [] # putting the ledger here instead above right below the class lines allows usage of this in methods of the same object/instance
        self.balance = 0 # start with zero balance before any deposits or withdrawals have been executed
        #test code# print(self.name)
        self.spent = 0 #having a running total of what has been spent from a category will help with the create_spend_chart function
        self.percentage_of_all_spending = 0 #have a changeable amount of percentage of total spending for create_spend_chart function later on
        #Now some prep work in order to print out correct info when print(self) is called outside the class according to the instructions:
        # self.character_length = len(str(self))
        # print(self.character_length)

        self.asterisk_count = 30 - len(self.name) #because there needs to be 30 total characters combined between object name and filler asterisks
        if self.asterisk_count % 2 == 0: #if there are an even number of characters in the object string, so there can be even asterisk amounts on either side of the object name
            self.asterisk_count_left = int(self.asterisk_count / 2)
            self.asterisk_count_right = int(self.asterisk_count / 2)
        else: #if there are an odd amount of object name letters
            self.asterisk_count_left = int(self.asterisk_count // 2) #round down after dividing by 2
            self.asterisk_count_right = self.asterisk_count_left + 1 #just throw the remaining asterisk on the right side of the name if there are an odd amount of asterisks to place due to an object string name with an odd amount of letters

        self.top_line = ''
        for asterisk in range(self.asterisk_count_left) :
            self.top_line = self.top_line + '*'
        self.top_line = self.top_line + self.name
        for asterisk in range(self.asterisk_count_right) :
            self.top_line = self.top_line + '*' # Now the top line is set up
        self.prnt = self.top_line  #this will be the string I return at the for the __str__ method for when an object is called to be printed. I'll add in the ledger entry lines below





    #to get the other lines going to be added onto the top lines for when the object is called to be printed:
    def __str__(self) :
        for dictionary in self.ledger : # iterate through ledger entries, which contain both amount pair and description pair
            #print(dictionary)
            for key in dictionary: #to iterate through the keys in the dictionary, which include both an amount pair and a description pair
                #print(key)
                if 'descr' in key : #if it is an description key. need it to be a string!! cannot have '==True' at the end as that will mess it up
                    description_left = dictionary[key] #use dictionary[key] instead of self.ledger[dictionary][key] to retrieve the value paired with the keys
                    description_left = description_left[:23] #to limit the amount of characters of the description to be 23 characters
                    # print(description_left)
                    # print(type(description_left))
                elif 'amount' in key:
                    amount_right = "{:.2f}".format(dictionary[key]) #here is the syntax I found online to get a number ot have 2 decimal places
                    amount_right = str(amount_right)
                    # print(amount_right)
                    # print(type(amount_right))
            number_of_spaces = 30 - len(description_left) - len(amount_right)
            line_to_add = description_left #get a string/line started to add onto total printing for object call
            for num in range(number_of_spaces):
                line_to_add = line_to_add + ' '
            line_to_add = line_to_add + amount_right
            #print(line_to_add)
            self.prnt = self.prnt + '\n' + line_to_add
            # print('Number of spaces: ', number_of_spaces)
            # print(key)
        self.prnt = self.prnt + '\n' + 'Total: ' + str("{:.2f}".format(self.balance)) + '\n' # to have remaining total on the bottom of the printout
        return self.prnt
            # for key, value in dictionary: #to iterate through the keys and values
            #     print(key, value)




    def check_funds(self, amount) : # define this one first because it will be referenced in the withdraw and transfer methods below
        if amount > self.balance :
            return False
        else:
            return True

    def deposit(self, *args): #the *args is the way to accept a variable amount of arguments - they are called in a loop on at a time the the order they are inputted with the method. In this case, the description may or may not be inputted so there may be either 1 or two arguments
        #test code print(len(args))
        count = 0 # use to help iterate through arguments if more than 1 argument (both amount and description) are inputted
        #test code print('before for loop: len(args) is :', len(args))
        for argument in args: # need to ditch the asterisk at this point
            #test code# print(len(args))
            if len(args) == 1: # if amount but no description is inputted
                self.deposit_amount = argument #using the first argument provided with the method call
                self.deposit_description = '' #equals empty string in case that len(args) == 1 which means no description was entered
                #test code print(self.deposit_amount)
            if len(args) > 1: # if both amount and description are inputted
                if count == 0: #to get first argument inputted as amount
                    self.deposit_amount = argument
                if count == 1: #if a second second argument inputted as description
                    self.deposit_description = argument #using the second argument provided with the method call
                    self.deposit_description = self.deposit_description.replace('"', '') #remove double quotation marks if they are part of the string
                    self.deposit_description = self.deposit_description.replace("'", '') #remove single quotation marks if they are part of the string
                #test code# print(self.deposit_description)
            count = count + 1
        #testcode print('deposit amount :', self.deposit_amount, 'deposit descr :', self.deposit_description)

        ##!! now need to put into ledger properly. !! CANNOT add amount and description together or there is trouble calling them separately later to update the balance amount
        #print('Length of ledger before :', len(self.ledger))
        deposit_ledger_entry = {'amount' + str( int(len(self.ledger) )): self.deposit_amount, 'description' + str( int(len(self.ledger) )): self.deposit_description} # to get the amounts numbered based on how many entries are already in the ledger
        self.ledger.append(deposit_ledger_entry)
        #print('Length of ledger after :', len(self.ledger))
        #print(len(self.ledger))
        # print(self.ledger)
        # print(type(self.ledger))
        # print(self.ledger[0])

        #Now to update balance when a deposit is made
        self.balance = self.balance + self.deposit_amount
        #print(self.balance)

    def withdraw(self, *args) : #going to be a lot of copy/paste from the deposit method
        count = 0 # use to help iterate through arguments if more than 1 argument (both amount and description) are inputted
        #test code print('before for loop: len(args) is :', len(args))
        for argument in args: # can ditch the asterisk at this point
            #test code# print(len(args))
            if len(args) == 1: # if amount but no description is inputted
                self.withdraw_amount = (-1) * argument #using the first argument provided with the method call. Make it negative since it's a withdrawal
                self.withdraw_description = '' #equals empty string in case that len(args) == 1 which means no description was entered
                #test code print(self.withdraw_amount)
            if len(args) > 1: # if both amount and description are inputted
                if count == 0: #to get first argument inputted as amount
                    self.withdraw_amount = (-1) * argument
                if count == 1: #if a second second argument inputted as description
                    self.withdraw_description = argument #using the second argument provided with the method call
                    self.withdraw_description = self.withdraw_description.replace('"', '') #remove double quotation marks if they are part of the string
                    self.withdraw_description = self.withdraw_description.replace("'", '') #remove single quotation marks if they are part of the string
                #test code# print(self.withdraw_description)
            count = count + 1

        #print('got here')
        #print(self.withdraw_amount)
        #Now need to have 'overdraft' check to see if withdrawal goes through
        if self.check_funds(self.withdraw_amount * (-1)) == False : #if the withdrawal amount is greater than the remaining get_balance, using check_funds method
            return False
        else:
            ##!! now need to put into ledger properly since the balance would remain non-negative after a withdrawal of this amount. !! CANNOT add amount and description together or there is trouble calling them separately later to update the balance amount
            #print(len(self.ledger))
            withdraw_ledger_entry = {'amount' + str( int(len(self.ledger) )): self.withdraw_amount, 'description' + str( int(len(self.ledger) )): self.withdraw_description} # to get the amounts numbered based on how many entries are already in the ledger
            self.ledger.append(withdraw_ledger_entry)
            #print(self.ledger)
            #Now to update balance when a deposit is made
            self.balance = self.balance + self.withdraw_amount #can keep it as addition because the amount added with be negative for all withdrawals (as long as a positive number is inputted as a method argument)
            self.spent =  self.spent + (-1 * self.withdraw_amount) #add a positive amount spent to help with create_spend_chart function
            #print(self.balance)
            #print(self.ledger)
            return True

    def get_balance(self) :
        return int(self.balance)

    def transfer(self, amount, other_category) :
        if self.check_funds(amount) == False:
            return False
        else:
            #first take care of the stuff in this category just like a withdrawal:
            self.transfer_out_amount = amount * (-1) #negative for the amount being transferred OUT of this account
            self.transfer_out_description = 'Transfer to ' + other_category.name
            #print('Length of ledger before :', len(self.ledger))
            transfer_ledger_entry_out = {'amount' + str( int(len(self.ledger) )): self.transfer_out_amount, 'description' + str( int(len(self.ledger) )): self.transfer_out_description}
            self.ledger.append(transfer_ledger_entry_out)
            #print('Length of ledger after :', len(self.ledger))
            self.balance = self.balance + self.transfer_out_amount
            #no longer include transfers into the create_spend_chart function!!! self.spent = self.spent + (-1 * self.transfer_out_amount)


            #Now take care of stuff in the ledger for the category that the transfer money is going INTO. !!MAKE SURE TO PUT IN other_category IN PLACE OF self IN ALL CASES!!
            other_category.transfer_in_amount = amount #positive for te amount being transferred INTO the other account
            other_category.transfer_in_description = 'Transfer from ' + self.name
            transfer_ledger_entry_out = {'amount' + str( int(len(other_category.ledger) )): other_category.transfer_in_amount, 'description' + str( int(len(other_category.ledger) )): other_category.transfer_in_description}
            other_category.ledger.append(transfer_ledger_entry_out)
            other_category.balance = other_category.balance + other_category.transfer_in_amount
            return True

def create_spend_chart(*categories):
    total_spending = 0 # get a running tally of all money spent from all accounts/categories
    for category in categories:
        total_spending = total_spending + category.spent
    #print(total_spending)
    for category in categories:
        category.percentage_of_all_spending =  math.trunc((category.spent / total_spending) * 10) * 10 #Get it to only tens value on left side of decimal (and ones value on the right side of the decimal), then truncate, then mulitply by 10
        #print(category.percentage_of_all_spending)

    spend_chart = 'Percentage spent by category' + '\n' #start building the actual printout for the function

    line_100 = '100| '
    line_90 = ' 90| '
    line_80 = ' 80| '
    line_70 = ' 70| '
    line_60 = ' 60| '
    line_50 = ' 50| '
    line_40 = ' 40| '
    line_30 = ' 30| '
    line_20 = ' 20| '
    line_10 = ' 10| '
    line_0 = '  0| '

    for category in categories:

        if category.percentage_of_all_spending >= 100:
            line_100 = line_100 + 'o  '
        else:
            line_100 = line_100 + '   '

        if category.percentage_of_all_spending >= 90:
            line_90 = line_90 + 'o  '
        else:
            line_90 = line_90 + '   '

        if category.percentage_of_all_spending >= 80:
            line_80 = line_80 + 'o  '
        else:
            line_80 = line_80 + '   '

        if category.percentage_of_all_spending >= 70:
            line_70 = line_70 + 'o  '
        else:
            line_70 = line_70 + '   '

        if category.percentage_of_all_spending >= 60:
            line_60 = line_60 + 'o  '
        else:
            line_60 = line_60 + '   '

        if category.percentage_of_all_spending >= 50:
            line_50 = line_50 + 'o  '
        else:
            line_50 = line_50 + '   '

        if category.percentage_of_all_spending >= 40:
            line_40 = line_40 + 'o  '
        else:
            line_40 = line_40 + '   '

        if category.percentage_of_all_spending >= 30:
            line_30 = line_30 + 'o  '
        else:
            line_30 = line_30 + '   '

        if category.percentage_of_all_spending >= 20:
            line_20 = line_20 + 'o  '
        else:
            line_20 = line_20 + '   '

        if category.percentage_of_all_spending >= 10:
            line_10 = line_10 + 'o  '
        else:
            line_10 = line_10 + '   '

        if category.percentage_of_all_spending >= 0:
            line_0 = line_0 + 'o  '
        else:
            line_0 = line_0 + '   '
    spend_chart = spend_chart + line_100 + '\n' + line_90 + '\n'+ line_80 + '\n'+ line_70 + '\n'+ line_60 + '\n'+ line_50 + '\n'+ line_40 + '\n' + line_30 + '\n'+ line_20 + '\n'+ line_10 + '\n'+ line_0 + '\n'

    line_dash = '    -'
    for category in categories:
        line_dash = line_dash + '---'
    spend_chart = spend_chart + line_dash + '\n'

    max_length = 0 #get a max length of characters for the longest category name
    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)
    #print(max_length)

    count = 0
    while count < max_length:
        line_name = '     '
        for category in categories:
            if len(category.name) > count:
                line_name = line_name + category.name[count] + '  ' #add in the appropriate letter then 2 spaces if the category name is long enough to need to be accounted for at this length
            else:
                line_name = line_name + '   ' #add in 3 spaces if the category name doesn't reach this far down
        spend_chart = spend_chart + line_name + '\n'
        count = count + 1

    return spend_chart

food = Category('food') #Need to have the quote marks to make the argument a string, otherwise it will treat the argument as an undefined variable and trip and error
food.deposit(1000, 'initial deposit')
food.deposit(500, 'prize')
food.deposit(300, 'gift')
food.withdraw(370, 'fee')
food.withdraw(100, 'taxes')
clothes = Category('clothes')
clothes.deposit(2000, 'initial deposit')
clothes.withdraw(530, 'jeans')
clothes.transfer(500, food)
utilities = Category('utilities')
utilities.deposit(1000, 'initial deposit')
utilities.withdraw(200, 'heat')
#print(food.spent)
#print(clothes.spent)
# print(food.ledger[0])
# print(food.ledger[0]['amount0'])
# print(food.ledger[0]['description0'])
# print(food.asterisk_count)
# print('Left asterisks amount is : ', food.asterisk_count_left)
# print('Right asterisks amount is : ', food.asterisk_count_right)
#print(food.top_line)
print(food)
print(clothes)

print(create_spend_chart(food, clothes, utilities))
#print(food.name)
#print(clothes.name)

# print(food.ledger[0])
# clothes = Category('clothes')
# food.transfer(100, clothes)
# food.transfer(100, clothes)
# food.transfer(100, clothes)
# print('food balance is :', food.balance)
# print('food ledger is :', food.ledger)
# print('clothes balance is :', clothes.balance)
# print('clothes ledger is :', clothes.ledger)
# print()
# food.transfer(50, clothes)
# food.transfer(25, clothes)
# print('food balance is :', food.balance)
# print('food ledger is :', food.ledger)
# print('clothes balance is :', clothes.balance)
# print('clothes ledger is :', clothes.ledger)
# #print(food.deposit(50, 'refund'))
#print(food.balance)
#print(food.withdraw(100, 'fee'))
# print(food.withdraw(100, 'burger'))
# print(food.balance)
# print(food.ledger)
# print(food.get_balance())
# print(food.check_funds(100))
# food.withdraw(100, 'fee')
#print(food.check_funds(150))
