import csv


def minute(value):
    index_colon = value.find(":")
    if index_colon != -1:
        minutes = float(value[:index_colon])
        seconds = float(value[index_colon + 1 :])
        return seconds + minutes * 60
    else:
        return value


solves = []
with open("csTimerExport_20240218_114925.csv") as csvfile:

    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        # print(row[1])
        if row[1] != "Time":
            solves.append(row[1])

# print(solves)
for i, solve in enumerate(solves):
    if solve.startswith("DNF"):
        solves[i] = float("inf")
    else:
        solves[i] = float(minute(solve))
# print(solves)

best_solves = []

for i in range(10):
    best_solves.append(min(solves[i * 3], solves[i * 3 + 1], solves[i * 3 + 2]))

print(sum(best_solves) / 10)
