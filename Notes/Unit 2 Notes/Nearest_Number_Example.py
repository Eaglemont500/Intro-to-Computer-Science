from sklearn.neighbors import KNeighborsClassifier   #with a knn package

## Features:
## "k" is always odd
##
## [age, education, salary, sex]
##
## education:
## 1 = high school
## 2 = bachelor's
## 3 = master's
## 4 = doctorate
##
## sex:
## 0 = female
## 1 = male


## x is the input
x = [
    [22, 1, 30000, 0],
    [25, 2, 40000, 0],
    [31, 2, 50000, 0],
    [35, 3, 65000, 1],
    [28, 2, 45000, 0],
    [42, 3, 80000, 1],
    [50, 4, 50000, 0],
    [55, 4, 90000, 1],

    [55, 1, 85000, 1],
    [30, 2, 95000, 1],
    [45, 3, 75000, 0],
    [60, 4, 120000, 1],
    [70, 3, 60000, 1],
    [65, 2, 970000, 0]
]

## y is the known data
y = [
    "Democrat",
    "Democrat",
    "Democrat",
    "Democrat",
    "Democrat",
    "Democrat",
    "Democrat",
    "Democrat",

    "Republican",
    "Republican",
    "Republican",
    "Republican",
    "Republican",
    "Republican"
]

## Create the KNN model
knn = KNeighborsClassifier(n_neighbors=3)

## Train the model
knn.fit(x, y)

## A new person
new_person = [[62, 2, 95000, 0]]

## Make a prediction
prediction = knn.predict(new_person)

print("Prediction:", prediction[0])


distances, indices = knn.kneighbors(new_person)

print("Nearest neighbors:")

for distance, index in zip(distances[0], indices[0]):
    print(x[index], y[index], "distance =", round(distance, 2))
'''
#without a knn package
import math

# [age, education, salary, sex]
# education: 1=HS, 2=BA, 3=MA, 4=PhD
# sex: 0=female, 1=male

people = [
    ([22, 1, 30000, 0], "Democrat"),
    ([25, 2, 40000, 1], "Democrat"),
    ([31, 2, 50000, 0], "Democrat"),
    ([35, 3, 65000, 1], "Democrat"),
    ([28, 2, 45000, 0], "Democrat"),
    ([42, 3, 80000, 1], "Democrat"),

    ([23, 1, 35000, 1], "Republican"),
    ([30, 2, 55000, 1], "Republican"),
    ([45, 3, 75000, 0], "Republican"),
    ([60, 4, 120000, 1], "Republican")
]

# New person
new_person = [40, 3, 70000, 1]


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
k = 3

print("Nearest neighbors:")

for d, label, person in distances[:k]:
    print(label, "distance =", round(d, 2))


# Vote
democrats = 0
republicans = 0

for d, label, person in distances[:k]:
    if label == "Democrat":
        democrats += 1
    else:
        republicans += 1


if democrats > republicans:
    prediction = "Democrat"
else:
    prediction = "Republican"


print("\nPrediction:", prediction)
'''