
class ProgressVisualizer:
    def __init__(self, data):
        self.__cnt = 0
        self.__size = len(data)

    def is_completed(self):
        return self.__cnt == self.__size

    def __str__(self):
        return '{0:.2f}% {1}'.format(100 * self.__cnt / self.__size,
                                    '{}-th line among {} lines'.format(self.__cnt, self.__size))

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        print(str(self))
        return self

    def __next__(self):
        self.__cnt += 1
        print(str(self))
