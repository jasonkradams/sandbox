from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Setup timezone and initial dates
pst = pytz.timezone('US/Pacific')
start_date_day = pst.localize(datetime(2024, 12, 9, 6, 0))
shift_length = timedelta(hours=12)
cycle_days = 8
repeat_weeks = 48
total_cycles = 48 * 7 // cycle_days  # Total cycles in 48 weeks

cal = Calendar()
cal.add('prodid', '-//My Calendar Product//example.com//')
cal.add('version', '2.0')

def add_shift_event(cal, start, summary, interval_weeks):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start)
    event.add('dtend', start + shift_length)
    event.add('rrule', {'freq': 'weekly', 'interval': interval_weeks})
    cal.add_component(event)
    print(f"Added {summary} shift on {start}")

current_date_day = start_date_day

for cycle in range(total_cycles):
    shift_type = "day" if cycle % 12 < 6 else "night"
    print(f"Cycle: {cycle}, Shift type: {shift_type}")
    
    if shift_type == "day":
        for j in range(4):  # 4 day shifts
            add_shift_event(cal, current_date_day, "Dane", repeat_weeks)
            current_date_day += timedelta(days=1)
        current_date_day += timedelta(days=cycle_days - 4)  # Skip 4 days off
    else:
        for j in range(4):  # 4 night shifts
            add_shift_event(cal, current_date_day.replace(hour=18), "Dane", repeat_weeks)
            current_date_day += timedelta(days=1)
        current_date_day += timedelta(days=cycle_days - 4)  # Skip 4 days off

# Save to .ics file
with open('work_schedule_pacific.ics', 'wb') as f:
    f.write(cal.to_ical())

