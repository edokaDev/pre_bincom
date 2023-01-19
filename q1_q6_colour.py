#!/usr/bin/env python3

class COLOUR:
    def __init__(self):
        self.data = {
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

        self.colours = {}

    def to_dict(self):
        # extract data to dictionary
        for day, cols in self.data.items():
            for col in cols:
                # for
                if col in self.colours:
                    self.colours[col] += 1
                else:
                    self.colours[col] = 1

    @property
    def sorted_dict(self):
        # sort dictionary
        return(sorted(self.colours.items(), key=lambda x:x[1]))
    
    @property
    def total_freq(self):
        return sum(x for col, x in self.colours.items())

    @property
    def mean_(self):
        return self.total_freq / len(self.sorted_dict)
    
    @property
    def mean_colour(self):
        return self.sorted_dict[int(self.mean_)][0]
    
    @property
    def median_colour(self):
        return self.sorted_dict[int(len(self.sorted_dict)/2)][0]
    
    @property
    def max_colour(self):
        return self.sorted_dict[-1][0]

    @property
    def variance(self):
    # calculate variance
        return sum((x - self.mean_) ** 2 for col, x in self.colours.items()) / (len(self.colours) - 1)

    def red_propability(self):
        return self.colours['RED'] / self.total_freq

    def output_answer(self):
        print(f"Mean Colour: {self.mean_colour}")
        print(f"Colour mostly worn: {self.max_colour}")
        print(f"Median Colour: {self.median_colour}")
        print(f"Variance: {round(self.variance, 4)}")
        print(f"Probability of a Red at Random is: {round(self.red_propability(), 4)}")

    def save_to_db(self):
        json = [{'name': name, 'frequency': freq} for name, freq in self.colours.items()]


# FOR QUESTIONS 1 T0 6
colours = COLOUR()
colours.to_dict()
colours.output_answer()
