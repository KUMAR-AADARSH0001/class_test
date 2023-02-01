class Car:

    def __init__(self, name, milage, doors, tyres, sunroof):
        self.name = name
        self.milage = milage
        self.doors = doors
        self.tyres = tyres
        self.sunroof = sunroof

        print(f'{name} is a best Car.\nIt give {milage} milage. \nIt had only {doors} doors. \nTheir had no sunroof in car.')


Car('Thar', '15kmp', 3, 4, True)
