# Calendar Scripts

## Dane's Schedule

[dane_sched.py](./dane_sched.py) generates the schedule for Dane, repeating forever.

**Algorithm**
Here’s the algorithm describing the frequency of your work schedule:

* Cycle Pattern: Every cycle is 8 days long.
  * Days 1 to 4: Work during the day shift (6 AM to 6 PM).
  * Days 5 to 8: Off days.

* Rotation Switch: After 6 cycles (48 days), switch from day shift to night shift or vice versa.
  * Next 6 cycles (48 days):
  * Days 1 to 4: Work during the night shift (6 PM to 6 AM).
  * Days 5 to 8: Off days.

* Continuation: This pattern repeats indefinitely.

* Repeat every 48 weeks: Each set of 48 days will continue the sequence of switching shifts.

So it’s: 4 days on, 4 days off; repeat for 6 cycles; switch to the opposite shift; repeat for another 6 cycles, and so on, forever.
