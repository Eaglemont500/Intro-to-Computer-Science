import math

people = [
    ([0, 2, 2, 5.5, 2], "Underclassmen"),
    ([0, 1, 1, 6.5, 1], "Underclassmen"),
    ([1, 2, 3, 4.5, 3], "Underclassmen"),
    ([0, 3, 2, 7.0, 2], "Underclassmen"),
    ([1, 1, 4, 5.0, 1], "Underclassmen"),
    ([0, 2, 1, 6.0, 4], "Underclassmen"),
    ([1, 3, 2, 4.0, 2], "Underclassmen"),
    ([0, 2, 4, 5.5, 3], "Underclassmen"),
    ([1, 2, 1, 7.0, 1], "Underclassmen"),
    ([0, 1, 3, 6.0, 2], "Underclassmen"),

    ([1, 3, 3, 5.0, 3], "Underclassmen"),
    ([1, 2, 4, 4.5, 4], "Underclassmen"),
    ([2, 2, 2, 6.0, 3], "Underclassmen"),
    ([1, 4, 3, 5.5, 2], "Underclassmen"),
    ([2, 3, 5, 4.0, 4], "Underclassmen"),
    ([1, 2, 2, 7.0, 3], "Underclassmen"),
    ([2, 4, 4, 5.0, 5], "Underclassmen"),
    ([1, 3, 5, 6.0, 2], "Underclassmen"),
    ([2, 2, 3, 5.5, 4], "Underclassmen"),
    ([1, 4, 2, 4.5, 3], "Underclassmen"),

    ([2, 3, 4, 4.5, 5], "Upperclassmen"),
    ([3, 2, 3, 5.5, 4], "Upperclassmen"),
    ([2, 4, 5, 4.0, 5], "Upperclassmen"),
    ([3, 3, 2, 6.0, 3], "Upperclassmen"),
    ([2, 5, 4, 4.5, 6], "Upperclassmen"),
    ([3, 3, 6, 5.0, 4], "Upperclassmen"),
    ([2, 4, 3, 6.5, 5], "Upperclassmen"),
    ([4, 2, 5, 4.0, 6], "Upperclassmen"),
    ([3, 4, 4, 5.5, 5], "Upperclassmen"),
    ([2, 3, 6, 4.5, 4], "Upperclassmen"),

    ([3, 4, 5, 4.0, 5], "Upperclassmen"),
    ([4, 3, 4, 5.0, 6], "Upperclassmen"),
    ([3, 5, 6, 3.5, 6], "Upperclassmen"),
    ([5, 3, 5, 4.5, 7], "Upperclassmen"),
    ([4, 4, 7, 4.0, 6], "Upperclassmen"),
    ([3, 2, 4, 6.0, 5], "Upperclassmen"),
    ([5, 4, 6, 3.5, 8], "Upperclassmen"),
    ([4, 5, 5, 5.0, 7], "Upperclassmen"),
    ([3, 3, 7, 4.5, 6], "Upperclassmen"),
    ([4, 4, 6, 5.5, 5], "Upperclassmen")
]

# New person
new_person = [3, 2, 5, 6.0, 10]


# Calculate Euclidean distance
def distance(person1, person2):
    total = 0

    for i in range(len(person1)):
        total += (person1[i] - person2[i]) ** 2

    return math.sqrt(total)


# Calculate distances from new person
distances = []

for person, label in people:
    d = distance(new_person, person)
    distances.append((d, label, person))


# Sort from closest to farthest
distances.sort()


# Look at the 3 nearest neighbors
k = 5

print("Nearest neighbors:")

for d, label, person in distances[:k]:
    print(label, "distance =", round(d, 2))


# Vote
Upperclassmen = 0
Underclassmen = 0

for d, label, person in distances[:k]:
    if label == "Upperclassmen":
        Upperclassmen += 1
    else:
        Underclassmen += 1


if Upperclassmen > Underclassmen:
    prediction = "Upperclassmen"
else:
    prediction = "Underclassmen"


print("\nPrediction:", prediction)


## Answers

## Student A
## k=1: Upperclassmen
## k=3: Upperclassmen
## k=5: Upperclassmen

## Student B
## k=1: Upperclassmen
## k=3: Upperclassmen
## k=5: Upperclassmen

## Student C
## k=1: Upperclassmen
## k=3: Upperclassmen
## k=5: Upperclassmen

## Student D
## k=1: Upperclassmen
## k=3: Upperclassmen
## k=5: Upperclassmen

## Student E
## k=1: Upperclassmen
## k=3: Upperclassmen
## k=5: Upperclassmen