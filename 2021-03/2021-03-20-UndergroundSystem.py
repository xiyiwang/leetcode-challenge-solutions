"""
LeetCode Challenge: Design Underground System (2021-03-20)

Implement the `UndergroundSystem` class:
- `void checkIn(int id, string stationName, int t)`
  - A customer with a card id equal to `id`, gets in the station 
    `stationName` at time `t`.
  - A customer can only be checked into one place at a time.
- `void checkOut(int id, string stationName, int t)`
  - A customer with a card id equal to `id`, gets out from the 
    station `stationName` at time `t`.
- `double getAverageTime(string startStation, string endStation)`
  - Returns the average time to travel between the `startStation` 
    and the `endStation`.
  - The average time is computed from all the previous traveling 
    from `startStation` to `endStation` that happened directly.
  - Call to `getAverageTime` is always valid.

You can assume all calls to `checkIn` and `checkOut` methods are 
consistent. If a customer gets in at time t1 at some station, they 
get out at time t2 with t2 > t1. All events happen in chronological 
order.

Constraints:
- There will be at most 20000 operations.
- 1 <= id, t <= 10^6
- All strings consist of uppercase and lowercase English letters, and 
  digits.
- 1 <= stationName.length <= 10
- Answers within 10^-5 of the actual value will be accepted as correct.
"""

# runtime: 228 ms (faster than 95.68%)
# memory: 23.5 MB (better than 87.88)
class UndergroundSystem:

    def __init__(self):
        self.checkedIn = dict()
        self.time = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn = self.checkedIn.pop(id)
        start_end = (checkIn[0], stationName)
        if start_end not in self.time:
            self.time[start_end] = [t - checkIn[1]]
        else:
            self.time[start_end].append(t - checkIn[1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.time[(startStation, endStation)]
        return sum(times)/len(times)
