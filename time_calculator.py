# sample inputs: "11:43 PM", "24:20", "tueSday"


def add_time(input) :
    #Remove unnecessary items from input by replacing them with nothing:
    input = input.replace('"', '')
    input = input.replace("'", '')
    input = input.replace(',', '')

    #Split the original input into components:
    input_split = input.split()
    #test code# print(input_split, type(input_split))
    #test code# print(input_split[0])

    #Split the first item by the colon to separate the hours and minutes
    start_time = input_split[0].split(':')
    #test code# print(start_time)
    hours_start = int(start_time[0])
    minutes_start = int(start_time[1])
    #test code# print(hours_start, minutes_start)
    ampm_start = input_split[1].upper() #just in case lower case is entered
    #test code# print(ampm_start, type(ampm_start), dir(ampm_start))

    #to account for am and pm, go to military time of 24 hours clock for calculations
    if ampm_start == 'PM':
        hours_start_military = hours_start + 12
    else :
        hours_start_military = hours_start
    #test code# print(hours_start_military)
    time_to_add = input_split[2].split(':')
    #print(time_to_add)
    hours_to_add = int(time_to_add[0])
    minutes_to_add = int(time_to_add[1])
    #test code# print(hours_to_add, minutes_to_add)
    #test code #print(dir(input_split[3]))

    #make variables to get a starting point for the ending time
    hours_end = hours_start_military + hours_to_add
    minutes_end = minutes_start + minutes_to_add
    #test code# print(minutes_end)
    #test code# print(hours_end)

    #carry over the extra minutes to be an extra hour if minutes add up to 60 minutes or more:
    if minutes_end > 59 :
        hours_end = hours_end + 1
        minutes_end = minutes_end - 60
    #test code# print(minutes_end)
    #test code# print(hours_end)


    #now try to turn any hours_end over 24 into a day passed by:
    days_passed = 0
    #test code# print(days_passed)
    #test code# print(hours_end)
    while hours_end >= 24 : #need to be inclusive so you don't end up with 24 hours as ending hours. I'll later change 0 hours to 12 AM.
        days_passed = days_passed + 1
        hours_end = hours_end - 24
        #test code print(days_passed)
        # test code print(hours_end)

    #Now have to sort hours_end into different categories back in 12-hour time and seting of ampm_end
    if hours_end > 12 : #to cover all PM hours EXCEPT FOR 12 NOON!! That is a different case in which subtracting 12 won't work
        hours_end = hours_end - 12
        ampm_end = 'PM'
        #test code# print(hours_end)
        #test code print(ampm_end)
    elif hours_end == 12: #don't want to subtract 12, otherwise 12 PM would turn into 0 PM
        ampm_end = 'PM'
    elif hours_end == 0 : # to account for midnight, which is a one-off case
        hours_end = 12
        ampm_end = 'AM'
        #test codeprint(hours_end)
        #test code print(ampm_end)
    else : #this covers hours 1 - 11 AM
        ampm_end = 'AM'
        #test code# print(hours_end)
        #test code# print(ampm_end)

    #now turn the ending time components into strings so they can be concatenated more easily without spaces thrown in there
    hours_end = str(hours_end)
    minutes_end = str(minutes_end)

    if len(minutes_end) == 1: #to see if minutes is a single digit, in which case we need to concatenate a zero before it
        minutes_end = '0' + minutes_end
    time_end = hours_end + ':' + minutes_end + ' ' + ampm_end

    #Now get the proper string for how many days later, if at all, the ending time is. Do nothing for days_passed = 0 because nothing is needed in that case
    days_later_print = ''
    if days_passed == 1 :
        days_later_print = days_later_print = '(next day)'
    elif days_passed > 1:
        days_later_print = days_later_print + ' (' + str(days_passed) + ' days later)'

    #print the easy case of no weekend inputted:
    if len(input_split) == 3 :
        print(time_end, days_later_print)
        quit() # this ends the program so that if no weekday is inputted, then no ending weekday will be calculated and outputted.



    #the day of the week in the input is optional, so make it conditional to work with:
    #test code# print(len(input_split))
    if len(input_split) > 3 :
        starting_day_of_week = input_split[3].lower().capitalize() #the rightmost method runs last!!
    #test code# print(starting_day_of_week)
        time_end = time_end + ', ' #change this to having a comma so there's a comma between the ending time and the ending day of the week

    #need to create a custom inner (nested) function to transform one day of the week into subsequent days of the week based on how many days have passed
    def next_day(day) :
        if day == 'Sunday' :
            return 'Monday'
        elif day == 'Monday' :
            return 'Tuesday'
        elif day == 'Tuesday' :
            return 'Wednesday'
        elif day == 'Wednesday' :
            return 'Thursday'
        elif day == 'Thursday' :
            return 'Friday'
        elif day == 'Friday' :
            return 'Saturday'
        elif day == 'Saturday' :
            return 'Sunday'

    #test code #print('Starting day of week before loops :', starting_day_of_week)
    #test code# print('Days passed :', days_passed)
    #test code# print('Days passed % 7 = ', days_passed % 7)
    if days_passed % 7 == 0: #Starts and ends on the same day of the week, even if full weeks go by
        ending_day_of_week = starting_day_of_week

    starting_day_of_week_iterable = starting_day_of_week #create new variable to be able to change while still keeping original starting day of the week
    if days_passed % 7 != 0 :
        #test code# print('Range of days passed : ', range(days_passed))
        #test code # print('Range of 4 is :', range(4))
        #test code #sample = 0
        for day in range(days_passed) :
            #test code print('Starting day of week right before a loop :', starting_day_of_week_iterable)
            #test code# sample = sample + 1
            #test code # print(sample)
            (starting_day_of_week_iterable) = next_day(starting_day_of_week_iterable)
            #test code print('Starting day of week after a loop :', starting_day_of_week_iterable)
        #test code print('Starting day of week after all loops :', starting_day_of_week_iterable)

        ending_day_of_week = starting_day_of_week_iterable

    complete_print = time_end + ending_day_of_week + days_later_print
    print(complete_print)

input = input('Please enter your starting time, the time you would like to add, and optionally the starting day of the week: ')

add_time(input)
