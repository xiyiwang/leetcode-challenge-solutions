"""
LeetCode Challenge: Keys and Rooms (2021-03-19)

There are N rooms and you start in room 0.  Each room 
has a distinct number in 0, 1, 2, ..., N-1, and each 
room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and 
each key rooms[i][j] is an integer in [0, 1, ..., N-1] 
where N = rooms.length.  A key rooms[i][j] = v opens 
the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Note:
- 1 <= rooms.length <= 1000
- 0 <= rooms[i].length <= 1000
- The number of keys in all rooms combined is at most 3000.
"""
# dfs - runtime: 60 ms (faster than 92.01%)
def canVisitAllRooms(rooms):
    unlocked = set([0])
    
    def dfs(room):
        for key in room:
            if key not in unlocked:
                unlocked.add(key)
                dfs(rooms[key])
        return unlocked

    return len(dfs(rooms[0])) == len(rooms)
