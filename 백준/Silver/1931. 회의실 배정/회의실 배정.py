def max_meetings(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    count = 1
    end_time = meetings[0][1]
    
    for i in range(1, len(meetings)):
        if meetings[i][0] >= end_time:
            count += 1
            end_time = meetings[i][1]
    
    return count

n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

print(max_meetings(meetings))
