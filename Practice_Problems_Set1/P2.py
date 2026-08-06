hours = [
    "8AM",
    "9AM",
    "10AM",
    "11AM",
    "12AM",
    "1PM",
    "2PM"
]

cups = []


for i in range(len(hours)):
    data = int(input(f"Enter the total cups sold at {hours[i]}: "))
    cups.append(data)

print(cups)

total = sum(cups)
print(total)

avg = total / len(cups)
print(avg)

print("Rush hours (above average):")

for i in range(len(cups)):
    if cups[i] > avg:
        print(hours[i])