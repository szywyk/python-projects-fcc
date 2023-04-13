def add_time(start, duration, *args):
    new_time = ""
    
    # set starting day by optional parameter
    days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    starting_day = ""
    third_parameter = False
    if len(args) > 0:
        try:
            starting_day = args[0].lower()
        except:
            pass
        else:
            if starting_day in days:
                third_parameter = True
            else:
                starting_day = ""

    # make tuples start: ('HH', 'MM', 'AM'/'PM'), duration: ('HH', 'MM')
    start_tuple = tuple(start.strip().replace(":", " ").split())
    duration_tuple = tuple(duration.strip().split(':'))

    # calculate minutes
    add_hour = False
    minute = int(start_tuple[1])
    duration_minute = int(duration_tuple[1])
    new_minute = minute + duration_minute
    if new_minute > 59:
        add_hour = True
        new_minute = new_minute - 60
    
    # calculate hours
    hour = int(start_tuple[0])
    if add_hour:
        duration_int = int(duration_tuple[0]) + 1
    else:
        duration_int = int(duration_tuple[0])
    am_pm = start_tuple[2]
    days_number = 0                              # days to add to the result

    for h in range(duration_int):
        if hour < 11:
            hour = hour + 1
        elif hour == 11:
            hour = hour + 1
            if am_pm == "PM":
                days_number = days_number + 1
                am_pm = "AM"
            else:
                am_pm = "PM"
        else:
            hour = 1

    # make new_time string
    if new_minute < 10:
        new_time = str(hour) + ":0" + str(new_minute) + " " + am_pm
    else:
        new_time = str(hour) + ":" + str(new_minute) + " " + am_pm

    # new_time string if optional parameter given
    if third_parameter:
        new_index = days.index(starting_day)
        if days_number > 6:
            days_to_add = days_number % 7   
        else:
            days_to_add = days_number
        for day in range(days_to_add):
            if new_index < 6:
                new_index = new_index + 1
            else:
                new_index = 0
        new_time = new_time + ", " + days[new_index].capitalize()

    # new_time string N days later
    if days_number == 1:
        new_time = new_time + " (next day)"
    elif days_number > 1:
        new_time = new_time + " (" + str(days_number) + " days later)"
    
    
    return new_time
