"""
LeetCode Challenge: My Calendar I (2021-06-10)

Implement a MyCalendar class to store your events. A new event can 
be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, 
this represents a booking on the half open interval [start, end), the 
range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection 
(ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event 
can be added to the calendar successfully without causing a double booking. 
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); 
MyCalendar.book(start, end)

Note:
- The number of calls to MyCalendar.book per test case will be at most 1000.
- In calls to MyCalendar.book(start, end), start and end are integers in the 
  range [0, 10^9].
"""

# Brute Force - O(N^2)
class MyCalendar1:
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for (s, e) in self.booked:
            if s < end and e > start:
                return False
        self.booked.append((start, end))
        return True