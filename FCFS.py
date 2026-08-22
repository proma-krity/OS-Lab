# FCFS CPU Scheduling Algorithm

processes = [
    ["P1", 3, 3],
    ["P2", 2, 1],
    ["P3", 5, 2],
    ["P4", 0, 3],
    ["P5", 1, 2]
]

# Sort processes according to Arrival Time
processes.sort(key=lambda x: x[1])

current_time = 0
total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

for pid, at, bt in processes:

    # Handle CPU idle time
    if current_time < at:
        current_time = at

    # Completion Time
    current_time += bt
    ct = current_time

    # Turnaround Time
    tat = ct - at

    # Waiting Time
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

# Calculate average times
avg_tat = total_tat / len(processes)
avg_wt = total_wt / len(processes)

print("\nAverage Turnaround Time =", avg_tat)
print("Average Waiting Time =", avg_wt)