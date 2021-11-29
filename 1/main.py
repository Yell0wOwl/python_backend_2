import sys


class CustomList(list):
    '''Класс особого списка'''

    def __init__(self, lst):
        if not isinstance(lst,list):
            sys.exit("CustomList принамает только списки!")
        self.lst = lst
        self.new_other = []
        self.new_lst = []

    def check_n_equalize(self, other):
        '''Приводит списки к одинаковой длине для проведения арифметических операций.
        Возвращает иготовую длину.
        '''

        if not (isinstance(self.lst, list) and isinstance(other, list)):
            sys.exit("CustomList поддерживает операции только с CustomList и списками!")
        len1 = len(self.lst)
        self.new_lst = self.lst[:]
        try:
            len2 = len(other.lst)
            self.new_other = other.lst[:]
        except AttributeError:
            len2 = len(other)
            self.new_other = other[:]
        if len1 != len2:
            if len1 < len2:
                self.new_lst = self.lst + [0] * (len2 - len1)
                len1 = len2
            else:
                self.new_other = other + [0] * (len1 - len2)
        return len1

    def check_n_sum(self, other):
        '''Считает суммы элементов списков перед операциями сравнения.
        Возвращает список из двух элементов - сумм элементов сравниваемых списков.
        '''

        if not (isinstance(self.lst, list) and isinstance(other, list)):
            sys.exit("CustomList поддерживает операции только с CustomList и списками!")
        sum1 = 0
        sum2 = 0
        for i in enumerate(self.lst):
            sum1 += i[1]
        try:
            for i in enumerate(other.lst):
                sum2 += i[1]
        except AttributeError:
            for i in enumerate(other):
                sum2 += i[1]
        return [sum1, sum2]

    def __add__(self, other):
        lenth = self.check_n_equalize(other)
        for i in range(lenth):
            self.new_other[i] += self.new_lst[i]
        return CustomList(self.new_other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        lenth = self.check_n_equalize(other)
        for i in range(lenth):
            self.new_lst[i] -= self.new_other[i]
        return CustomList(self.new_lst)

    def __rsub__(self, other):
        self.new_other = []
        self.new_lst = []
        lenth = self.check_n_equalize(other)
        for i in range(lenth):
            self.new_other[i] -= self.new_lst[i]
        return CustomList(self.new_other)

    def __lt__(self, other):
        sums = self.check_n_sum(other)
        return sums[0] < sums[1]

    def __gt__(self, other):
        sums = self.check_n_sum(other)
        return sums[0] > sums[1]

    def __le__(self, other):
        sums = self.check_n_sum(other)
        return sums[0] <= sums[1]

    def __ge__(self, other):
        sums = self.check_n_sum(other)
        return sums[0] >= sums[1]

    def __eq__(self, other):
        sums = self.check_n_sum(other)
        return sums[0] == sums[1]

    def __ne__(self, other):
        sums = self.check_n_sum(other)
        return sums[0] != sums[1]

if __name__ == '__main__':
    pass
