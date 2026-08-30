# Round Robin - Preemptive
# Standard Round Robin is inherently preemptive.

from collections import deque

processes = [
    ["P1", 0, 8],
    ["P2", 1, 4],
    ["P3", 2, 2],
    ["P4", 3, 1],
    ["P5", 4, 3]
]

time_quantum = 2
n = len(processes)

remaining_time = [p[2] for p in processes]
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

queue = deque()
visited = [False] * n

time = 0
completed = 0
gantt = []

while completed < n:

    for i in range(n):
        if processes[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if not queue:
        time += 1
        continue

    current = queue.popleft()
    start = time

    run_time = min(time_quantum, remaining_time[current])

    time += run_time
    remaining_time[current] -= run_time

    gantt.append((processes[current][0], start, time))

    for i in range(n):
        if processes[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if remaining_time[current] > 0:
        queue.append(current)
    else:
        completion_time[current] = time
        completed += 1

for i in range(n):
    turnaround_time[i] = completion_time[i] - processes[i][1]
    waiting_time[i] = turnaround_time[i] - processes[i][2]

print("Gantt Chart:")
for item in gantt:
    print(item[0], ":", item[1], "-", item[2])

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(
        processes[i][0],
        "\t",
        processes[i][1],
        "\t",
        processes[i][2],
        "\t",
        completion_time[i],
        "\t",
        turnaround_time[i],
        "\t",
        waiting_time[i]
    )

print("\nAverage Waiting Time:", sum(waiting_time) / n)
print("Average Turnaround Time:", sum(turnaround_time) / n)