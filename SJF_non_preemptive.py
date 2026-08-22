# SJF (Shortest Job First) - Non Preemptive

processes = [
    ["P1", 3, 1],
    ["P2", 2, 4],
    ["P3", 3, 6],
    ["P4", 1, 3],
    ["P5", 4, 2],
    ["P6", 6, 1]
]

current_time = 0
total_tat = 0
total_wt = 0
completed = []

print("PID\tAT\tBT\tCT\tTAT\tWT")

while len(completed) < len(processes):

    available = []

    # Find all processes that have arrived
    for p in processes:
        if p[0] not in completed and p[1] <= current_time:
            available.append(p)

    # If no process is available, increase time
    if len(available) == 0:
        current_time += 1
        continue

    # Select the process with the shortest Burst Time
    available.sort(key=lambda x: x[2])

    pid, at, bt = available[0]

    # Execute the selected process
    current_time += bt

    # Calculate times
    ct = current_time
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    completed.append(pid)

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

# Calculate averages
avg_tat = total_tat / len(processes)
avg_wt = total_wt / len(processes)

print("\nAverage Turnaround Time =", avg_tat)
print("Average Waiting Time =", avg_wt)