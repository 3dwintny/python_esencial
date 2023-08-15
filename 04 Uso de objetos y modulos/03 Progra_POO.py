# como se usa POO

class Airplane:
    def __init__(self, passengers, seats, pillots=[]):
        self.passengers = passengers
        self.seats = seats
        self._pillots = pillots
        def takeoff(self):
            pass

class Person:
    #init, nos permite inicializar los valores, es cuando carga una base de datos o datos externos
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print('Hello, my name is {} and I am {} years old'.format(self.name, self.age))
        
if __name__ == '__main__':
    
    person = Person('Edwin', 24)
    print('Age: {}'.format(person.age))
    person.say_hello()
    