import random
import pprint


class Board:
    N = 11
    p1 = [0, 1, 2]
    p2 = [4, 5, 6]
    p3 = [8, 9, 10]
    pp = [p1, p2, p3]

    def __init__(self):
        self.list_of_numbers2 = [[0] * self.N] * self.N # only to tests
        self.list_of_numbers = [[0 for i in range(self.N)] for j in range(self.N)]

    """ IMPORTANT!!!!!!
            print(self.list_of_numbers[0] is self.list_of_numbers[1])
            print(self.list_of_numbers2[0] is self.list_of_numbers2[1]) # SEPARATE LISTS !!!!!!!!
    
    """

    def add_numbers_to_list(self):
        for i in range(11):
            if i in [3, 7]:
                self.list_of_numbers[i] = "-----------"
                continue
            for j in range(11):
                if j in [3, 7]:
                    self.list_of_numbers[i][j] = "|"
                    continue
        self.add_squares()
        return self.list_of_numbers

    def add_squares(self):  # very difficult function!!!! BUT WORK!
        for k in range(3):
            for l in range(3):
                bufor_unique_numbers = random.sample(range(1, 10), 9)
                for i in range(3):
                    for j in range(3):
                        self.list_of_numbers[self.pp[k][i]][self.pp[l][j]] = bufor_unique_numbers.pop()

    def display_board(self, list_chars):
        for i in range(11):
            print(*list_chars[i])
        print("*"*10)

    def check_duplicate_row_column(self):
        for row in range(self.N): # check rows
            self.is_duplicate(self.list_of_numbers[row], "row")
        for row in range(self.N): # check columns
            bufor_column = []
            for col in range(self.N):
                bufor_column.append(self.list_of_numbers[col][row])
            self.is_duplicate(bufor_column, "column")


    def is_duplicate(self, list, where):
        bufor_list = []
        bufor_set = set()
        for num in list:
            if num in [x for x in range(1, 10)]:
                bufor_list.append(num)
                bufor_set.add(num)
        # print(bufor_list)
        # print("len list:", len(bufor_list), "len set:", len(bufor_set))
        if len(list) == len(set(list)):
            return False
        else:
            print(f"Exist duplicate in {where}")
            exit()
            return True
