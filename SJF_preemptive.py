# SJF - Preemptive (Shortest Remaining Time First)

processes = [
    ["P1", 3, 1],
    ["P2", 2, 4],
    ["P3", 3, 6],
    ["P4", 1, 3],
    ["P5", 4, 2],
    ["P6", 6, 1]
]

# PID, Arrival Time, Burst Time, Remaining Time
processes = [[p[0], p[1], p[2], p[2]] for p in processes]

time = 0
completed = 0
n = len(processes)

completion_time = {}
gantt = []

while completed < n:

    # Find processes that have arrived
    available = [
        p for p in processes
        if p[1] <= time and p[3] > 0
    ]

    # CPU idle
    if not available:
        if not gantt or gantt[-1][0] != "Idle":
            gantt.append(["Idle", time, time + 1])
        else:
            gantt[-1][2] = time + 1

        time += 1
        continue

    # Select process with shortest remaining time
    # If tied, choose the process that arrived later
    current = min(available, key=lambda p: (p[3], -p[1]))

    # Add process to Gantt chart
    if not gantt or gantt[-1][0] != current[0]:
        gantt.append([current[0], time, time + 1])
    else:
        gantt[-1][2] = time + 1

    # Execute for 1 unit
    current[3] -= 1
    time += 1

    # Process completed
    if current[3] == 0:
        completed += 1
        completion_time[current[0]] = time


# Calculate CT, TAT and WT
print("PID\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for p in processes:

    pid, at, bt, rt = p

    ct = completion_time[pid]
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")


# Calculate averages
avg_tat = total_tat / n
avg_wt = total_wt / n

print("\nAverage Turnaround Time =", avg_tat)
print("Average Waiting Time =", avg_wt)


# Display Gantt Chart
print("\nGantt Chart:")

for g in gantt:
    print(f"| {g[0]} ", end="")

print("|")

print(gantt[0][1], end="")

for g in gantt:
    print(f"    {g[2]}", end="")

print()