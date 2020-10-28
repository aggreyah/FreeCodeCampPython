def add_time(start, duration, day_of_week=None):
    new_time_same_period = False
    new_time_same_day = False
    new_time_min = add_hours_minutes(start, duration)

    new_time = ""

    return new_time


def extract_hour_minute_and_period(time_string):
    start_time_and_period = time_string.split(" ")
    time_hour, time_minute = get_hour_and_minute(start_time_and_period[0])
    if len(start_time_and_period) == 1:
        return time_hour, time_minute
    else:
        time_period = start_time_and_period[1]
    return time_hour, time_minute, time_period


def get_hour_and_minute(hour_and_minute):
    start_time_hour_and_minute = hour_and_minute[0].split(":")
    time_hour = start_time_hour_and_minute[0]
    time_minute = start_time_hour_and_minute[1]
    return time_hour, time_minute


def simple_subtract_time(start, end):
    end_time = end.split(":")
    start_time = start.split(":")
    end_time_hour = end_time[0]
    end_time_minute = end_time[1]
    start_time_hour = start_time[0]
    start_time_minute = start_time[1]
    if eval(end_time_minute) < eval(start_time_minute):
        resulting_time_minute = str((eval(end_time_minute) + eval("60")) - eval(start_time_minute))
        resulting_time_hour = str((eval(end_time_hour) - 1) - eval(start_time_hour))
    else:
        resulting_time_minute = str(eval(start_time_minute) - eval(end_time_minute))
        resulting_time_hour = str(eval(start_time_hour) - eval(end_time_hour))
    return f"{resulting_time_hour}:{resulting_time_minute}"


def add_hours_minutes(time, duration_to_add):
    period_change_time = "11:59"
    start_time_hour, start_time_minute, start_time_period = extract_hour_minute_and_period(time)
    elapsed_time_hours, elapsed_time_minutes = extract_hour_minute_and_period(duration_to_add)
    to_change_period = simple_subtract_time(period_change_time, time)
    pass


if __name__ == "__main__":
    print(simple_subtract_time("10:50", "11:40"))
