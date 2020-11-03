TRANSITION_TIME = "11:59"
HOURS_IN_DAY = 24
NEXT_DAY = "next day"
TIME_PERIOD_LENGTH = 12
MINUTES_IN_HOUR = 60
DAYS_OF_THE_WEEK = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
TIME_PERIODS_IN_DAY = {0: "AM", 1: "PM"}


def add_time(start, duration, day_of_week=None):
    number_of_days_later = 0
    period_transition = False
    new_time = ""
    end_period = ""
    start_period = 0
    number_of_days_later_string = ""
    end_day_of_the_week = ""
    if day_of_week:
        start_day_of_the_week_int = DAYS_OF_THE_WEEK[day_of_week.lower()]
        end_day_of_the_week_int = 0

    start_time_hour, start_time_minute, start_time_period_string = extract_hour_minute_and_period(start)
    duration_hours, duration_minutes = get_hour_and_minute(duration)
    for item in TIME_PERIODS_IN_DAY:
        if TIME_PERIODS_IN_DAY[item] == start_time_period_string:
            start_period = item

    number_of_days_later += duration_hours // HOURS_IN_DAY
    new_duration_hours = duration_hours % HOURS_IN_DAY
    duration_to_transition = simple_subtract_time(start.split(" ")[0], TRANSITION_TIME)
    new_duration_time = f"{new_duration_hours}:{duration_minutes}"
    if the_bigger_time(duration_to_transition, new_duration_time) == duration_to_transition:
        new_time = simple_add_time(start.split(" ")[0], new_duration_time)
    elif the_bigger_time(duration_to_transition, new_duration_time) == new_duration_time:
        period_transition = True
        new_time = simple_add_time(TRANSITION_TIME, simple_subtract_time(duration_to_transition, new_duration_time))

    end_period = start_period if not period_transition else (start_period + 1) % 2
    end_time_period_string = TIME_PERIODS_IN_DAY[end_period]

    if (not end_period == start_period) and TIME_PERIODS_IN_DAY[start_period] == TIME_PERIODS_IN_DAY[1]:
        number_of_days_later += 1

    if number_of_days_later == 1:
        number_of_days_later_string = NEXT_DAY
    elif number_of_days_later > 1:
        number_of_days_later_string = f"{number_of_days_later} days later"
    if day_of_week:
        end_day_of_the_week_int = (start_day_of_the_week_int + number_of_days_later) % 7

    if (number_of_days_later == 0) and (not day_of_week):
        f_new_time = f"{new_time} {end_time_period_string}"
    elif (number_of_days_later == 0) and day_of_week:
        f_new_time = f"{new_time} {end_time_period_string}, {day_of_week}"
    else:
        if not day_of_week:
            f_new_time = f"{new_time} {end_time_period_string} ({number_of_days_later_string})"
        else:
            for key in DAYS_OF_THE_WEEK:
                if DAYS_OF_THE_WEEK[key] == end_day_of_the_week_int:
                    end_day_of_the_week = key.capitalize()
            f_new_time = f"{new_time} {end_time_period_string}, {end_day_of_the_week} ({number_of_days_later_string})"

    return f_new_time


def the_bigger_time(time_A, time_B):
    time_A_hours, time_A_minutes = extract_hour_minute_and_period(time_A)
    time_B_hours, time_B_minutes = extract_hour_minute_and_period(time_B)
    if eval(time_A_hours) > eval(time_B_hours):
        return time_A
    elif eval(time_B_hours) > eval(time_A_hours):
        return time_B
    elif eval(time_A_hours) == eval(time_B_hours) and eval(time_A_minutes) > eval(time_B_minutes):
        return time_A
    elif eval(time_A_hours) == eval(time_B_hours) and eval(time_B_minutes) > eval(time_A_minutes):
        return time_B
    else:
        return None


def simple_add_time(start, duration):
    start_hour, start_minute = extract_hour_minute_and_period(start)
    duration_hours, duration_minutes = extract_hour_minute_and_period(duration)
    end_time_hour = ""
    end_time_minute = ""
    sum_minutes = eval(start_minute) + eval(duration_minutes)
    end_time_minute += f"{sum_minutes % MINUTES_IN_HOUR}"
    start_hour = f"{eval(start_hour) + (sum_minutes // MINUTES_IN_HOUR)}"
    sum_hour = f"{eval(start_hour) + eval(duration_hours)}"
    end_time_hour = f"{eval(sum_hour) % TIME_PERIOD_LENGTH}"
    if eval(end_time_hour) == 0:
        end_time_hour = f"{eval(end_time_hour) + TIME_PERIOD_LENGTH}"
    if eval(end_time_minute) < 10:
        end_time_minute = f"0{end_time_minute}"

    return f"{end_time_hour}:{end_time_minute}"


def extract_hour_minute_and_period(time_string):
    start_time_and_period = time_string.split(" ")
    time_hour, time_minute = get_hour_and_minute(start_time_and_period[0])
    if len(start_time_and_period) == 1:
        return f"{time_hour}", f"{time_minute}"
    else:
        time_period = start_time_and_period[1]
    return f"{time_hour}", f"{time_minute}", time_period


def get_hour_and_minute(hour_and_minute):
    hour_and_minute = hour_and_minute.split(":")
    time_hour = int(hour_and_minute[0])
    time_minute = int(hour_and_minute[1])
    return time_hour, time_minute


def simple_subtract_time(start, end):
    end_time_hour, end_time_minute, start_time_hour, start_time_minute = process_start_and_end_times(end, start)

    if int(end_time_minute) < int(start_time_minute):
        resulting_time_hour = str((int(end_time_hour) - 1) - int(start_time_hour))
        resulting_time_minute = str((eval(end_time_minute) + MINUTES_IN_HOUR) - eval(start_time_minute))
    else:
        resulting_time_minute = str(int(end_time_minute) - int(start_time_minute))
        resulting_time_hour = str(int(end_time_hour) - int(start_time_hour))

    resulting_time_hour = f"0{resulting_time_hour}" if len(resulting_time_hour) < 2 else resulting_time_hour
    resulting_time_minute = f"0{resulting_time_minute}" if len(resulting_time_minute) < 2 else resulting_time_minute
    return f"{resulting_time_hour}:{resulting_time_minute}"


def process_start_and_end_times(stop, begin):
    end_time = stop.split(":")
    start_time = begin.split(":")
    end_time_hour = end_time[0]
    end_time_minute = end_time[1]
    start_time_hour = start_time[0]
    start_time_minute = start_time[1]

    end_time_hour = f"{eval(end_time_hour) + TIME_PERIOD_LENGTH}" if start_time_hour == "12" else end_time_hour
    return end_time_hour, end_time_minute, start_time_hour, start_time_minute


if __name__ == "__main__":
    print(add_time("3:30 PM", "2:12", "Monday"))
