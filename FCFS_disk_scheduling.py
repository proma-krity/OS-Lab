requests = list(map(int, input("Enter request: ").split()))
head = int(input("Enter initial head: "))

total_movement = 0

print("Disk Scheduling Algorithm: FCFS")
print("Seek Sequence:", end=" ")
print(head, end=" ")

for request in requests:
    movement = abs(request - head)
    total_movement += movement
    head = request
    print("->", request, end=" ")

print("\nTotal Head Movement:", total_movement)