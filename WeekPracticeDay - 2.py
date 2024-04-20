class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def __gt__( self, other ) :
        if self.age > other.age :
            return True
        else : 
            return False

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 47, 68, 95)

if sakib > musfiq :
    if sakib > kamal :
        if sakib > jack :
            if sakib > kalam :
                print( 'Sakib' )
        else :
            if jack > kalam :
                print('Jack')
            else :
                print('Kalam')
    else :
        if kamal > jack :
            if kamal > kalam :
                print('Kamal')
            else :
                print('Kalam')
else :
    if musfiq > kamal :
        if musfiq > jack :
            if musfiq > kalam :
                print( 'Musfiq' )
        else :
            if jack > kalam :
                print('Jack')
            else :
                print('Kalam')
    else :
        if kamal > jack :
            if kamal > kalam :
                print( 'Kamal' )
        else :
            if jack > kalam :
                print( 'Jack' )
            else :
                print( 'Kalam' )