class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError('The length must be above zero')

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError('The length must be above zero')


if __name__ == '__main__':
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
