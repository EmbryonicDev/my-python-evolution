
# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def add_number(self, number):
        self.__numbers.append(number)

    def add_address(self, address):
        self.__address = address

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

    def name(self):
        return self.__name

    # def __iter__(self):
    #     self.n = 0
    #     return self

    # def __next__(self):
    #     if self.n < len(self.__numbers):
    #         # Select the current item from the list within the object
    #         number = self.__numbers[self.n]
    #         # increase the counter (i.e. iteration variable) by one
    #         self.n += 1
    #         # return the current item
    #         return number
    #     else:
    #         # All numbers have been traversed
    #         raise StopIteration


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        newPerson = Person(name)
        if newPerson not in self.__persons:
            newPerson.add_number(number)
            self.__persons[newPerson] = newPerson
        else:
            for person in self.__persons:
                if person.name == name:
                    person.add_number(number)

    def add_address(self, name: str, address: str):
        newPerson = Person(name)
        if newPerson not in self.__persons:
            newPerson.add_address(address)
            self.__persons[newPerson] = newPerson
        else:
            for person in self.__persons:
                if person.name == name:
                    person.add_address(address)

    def get_entry(self, name: str):
        # found = False
        address = None
        number = None
        for person in self.__persons:
            if person.name() == name:
                if person.address() != None:
                    address = person.address()
                if len(person.numbers()) > 0:
                    number = person.numbers()[0]

        if number == None:
            print('number unknown')
        else:
            print(number)
        if address == None:
            print('address unknown')
        else:
            print(address)

    def all_entries(self):
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print('3 add address')

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input('name: ')
        address = input('address: ')
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        self.__phonebook.get_entry(name)

        # if numbers == None:
        #     print("number unknown")
        #     return

        # # for number in numbers:
        # print(number)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == '3':
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# if __name__ == '__main__':
#     print('\nPart 1')
#     person = Person("Eric")
#     print(person.name())
#     print(person.numbers())
#     print(person.address())
#     person.add_number("040-123456")
#     person.add_address("Mannerheimintie 10 Helsinki")
#     print(person.numbers())
#     print(person.address())

#     print('\nPart 2')
#     phonebook = PhoneBook()
#     phonebook.add_number("Eric", "02-123456")
#     print(phonebook.get_entry("Eric"))
#     print(phonebook.get_entry("Emily"))
