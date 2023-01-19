#!/usr/bin/env python3


data = {
    'monday': [
        'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
    ],
    'tuesday': [
        'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'
    ],
    'wednesday': [
        'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'
    ],
    'thursday': [
        'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
    ],
    'friday': [
        'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE'
    ]
}


# extract data to dictionary

colours = {}

for day, cols in data.items():
    for col in cols:
        # for
        if col in colours:
            colours[col] += 1
        else:
            colours[col] = 1


# sort dictionary
sorted_colours = sorted(colours.items(), key=lambda x:x[1])

# calculate mean, median and mode
total_appr = 0
for col in sorted_colours:
    total_appr += col[1]

mean = total_appr/len(sorted_colours)
mean_colour = sorted_colours[int(mean)]
median_colour = sorted_colours[int(len(sorted_colours)/2)]
max_colour = sorted_colours[-1]

print('Mean: ', mean_colour[0])
print('Median: ', median_colour[0])
print('Max: ', max_colour[0])


variance = sum((x - mean) ** 2 for col, x in colours.items()) / (len(colours) - 1)

# print(colours)
print('Variance: ', round(variance, 2))

total_freq = sum(x for col, x in colours.items())

prob_red = colours['RED'] / total_freq

print('PROB RED: ', round(prob_red, 4))


colours = [{'name': name, 'frequency': freq} for name, freq in colours.items()]
# print(colours)