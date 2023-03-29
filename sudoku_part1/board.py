import random


class Board:
    LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8]]

    def __init__(self):
        self.list_of_numbers = []

    def add_numbers_to_list(self):
        self.list_of_numbers = random.sample(range(1, 10), 9) # without duplicate
        # self.list_of_numbers = [random.randint(1, 10) for x in range(10)] # with duplicate
        return self.list_of_numbers

    def display_board(self, list_chars):
        print("%s | %s | %s" % (list_chars[0], list_chars[1], list_chars[2]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[3], list_chars[4], list_chars[5]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[6], list_chars[7], list_chars[8]))

    def check_duplicate_row_column(self):
        for line in self.LINES:
            if self.is_duplicate([self.list_of_numbers[line[0]], self.list_of_numbers[line[1]],
                                  self.list_of_numbers[line[2]]]):
                print("Row or colum contains duplicate")
                return False
        return True

    def is_duplicate(self, list):
        if len(list) == len(set(list)):
            return False
        else:
            return True
