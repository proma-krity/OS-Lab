requests = [0, 41, 30, 100, 62, 51, 20]
head = 70
direction = "left"

left = []
right = []

for request in requests:
    if request < head:
        left.append(request)
    else:
        right.append(request)

left.sort(reverse=True)
right.sort()

order = [head]

if direction == "right":
    for request in right:
        order.append(request)

    for request in left:
        order.append(request)

else:
    for request in left:
        order.append(request)

    for request in right:
        order.append(request)

total_movement = 0

print("Disk Scheduling Algorithm: SCAN")
print("Direction:", direction)
print("Head Movement Order:", order)

print("\nIndividual Head Movements:")

for i in range(len(order) - 1):
    movement = abs(order[i + 1] - order[i])
    total_movement += movement

    print(order[i], "->", order[i + 1], "=", movement)

print("\nTotal Head Movements:", total_movement)