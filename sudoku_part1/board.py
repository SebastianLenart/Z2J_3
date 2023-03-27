import random


class Board:
    LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]

    def __init__(self):
        self.list_of_numbers = []

    def add_numbers_to_list(self):
        self.list_of_numbers = random.sample(range(1, 10), 9)
        return self.list_of_numbers

    def display_board(self, list_chars):
        print(list_chars)
        print("%s | %s | %s" % (list_chars[0], list_chars[1], list_chars[2]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[3], list_chars[4], list_chars[5]))
        print("__|___|__")
        print("%s | %s | %s" % (list_chars[6], list_chars[7], list_chars[8]))

    def check_duplicate_row_column(self, list_chars):
        pass

