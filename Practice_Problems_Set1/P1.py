first_of_houses = "GHRSghrs"

name = input("name:")
signals = input("signals:").lower()

count = {
    "g": 0,
    "h": 0,
    "r": 0,
    "s": 0
}

for i in range(len(signals)):
    if signals[i] in first_of_houses:
        count[signals[i]] += 1

max_count = max(count.values())
max_key = max(count, key=count.get)

for key, value in count.items():
    if max_count == value:
        if key < max_key:
            max_key = key

if max_key == "g":
    print(name, "you belong in ....Gryffindor!(", max_count, "signals)")
elif max_key == "h":
    print(name, "you belong in ....Hufflepuff!(", max_count, "signals)")
elif max_key == "r":
    print(name, "you belong in ....RavenClaw!(", max_count, "signals)")
else:
    print(name, "you belong in ....Slytherin!(", max_count, "signals)")