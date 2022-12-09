# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to: 'RealProperty'):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to: 'RealProperty'):
        self_price = self.square_metres * self.price_per_sqm
        compared_to_price = compared_to.square_metres * compared_to.price_per_sqm
        difference = self_price - compared_to_price
        return difference if difference > 0 else difference * -1

    def more_expensive(self, compared_to: 'RealProperty'):
        self_price = self.square_metres * self.price_per_sqm
        compared_to_price = compared_to.square_metres * compared_to.price_per_sqm
        return self_price > compared_to_price


if __name__ == '__main__':
    print('\nPart 1')
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))

    print('\nPart 2')
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))

    print('\nPart 3')
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))
