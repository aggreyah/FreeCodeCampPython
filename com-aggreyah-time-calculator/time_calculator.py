def add_time(start, duration, day_of_week=None):
    start_time_hour, start_time_minute, start_time_period = extract_hour_minute_and_period(start)
    elapsed_time_hours, elapsed_time_minutes = extract_hour_minute_and_period(duration)
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
