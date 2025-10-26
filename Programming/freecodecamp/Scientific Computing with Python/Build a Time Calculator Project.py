def add_time(start, duration, day=None):
    # split start time
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(':'))

    # convert to 24-hour
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    start_total = start_hour * 60 + start_minute

    # duration in minutes
    dur_hour, dur_min = map(int, duration.split(':'))
    dur_total = dur_hour * 60 + dur_min

    # total minutes
    total = start_total + dur_total
    days_later = total // (24 * 60)
    total = total % (24 * 60)

    # convert back
    end_hour = total // 60
    end_min = total % 60

    period = "AM"
    if end_hour >= 12:
        period = "PM"
    if end_hour > 12:
        end_hour -= 12
    if end_hour == 0:
        end_hour = 12

    # result
    new_time = f"{end_hour}:{end_min:02d} {period}"

    # handle day
    if day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = days.index(day.capitalize())
        new_day = days[(index + days_later) % 7]
        new_time += f", {new_day}"

    # handle days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time