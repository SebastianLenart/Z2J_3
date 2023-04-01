import random
import pprint


class Board:
    N = 11
    p1 = [0, 1, 2]
    p2 = [4, 5, 6]
    p3 = [8, 9, 10]
    pp = [p1, p2, p3]

    def __init__(self):
        self.points = []
        self.squares = []
        self.list_of_numbers = [[0] * self.N] * self.N
        self.add_squares()

    def add_numbers_to_list(self):
        for i in range(11):
            if i in [3, 7]:
                self.list_of_numbers[i] = "-----------"
                continue
            for j in range(11):
                # self.list_of_numbers[i][j] = 1
                if j in [3, 7]:
                    self.list_of_numbers[i][j] = "|"
                    continue
        return self.list_of_numbers

    def add_squares(self):
        for x in self.pp:
            for y in x:
                for z in self.pp:
                    for v in z:
                        self.points.append([y, v])

        # pprint.pp(self.points)
        # square without duplicates
        a = zip(self.p1, self.p1)
        for s in range(3):

            print(s)



    def display_board(self, list_chars):
        for i in range(11):
            print(*list_chars[i])


    # def check_duplicate_row_column(self):
    #     for line in self.LINES:
    #         if self.is_duplicate([self.list_of_numbers[line[0]], self.list_of_numbers[line[1]],
    #                               self.list_of_numbers[line[2]]]):
    #             print("Row or colum contains duplicate")
    #             return False
    #     return True
    #
    # def is_duplicate(self, list):
    #     if len(list) == len(set(list)):
    #         return False
    #     else:
    #         return True
