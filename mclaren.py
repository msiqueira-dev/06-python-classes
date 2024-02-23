# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python.
#   Essa classe é a classe McLaren e herda da classe Car sendo então a classe filho.
# EN: 
#   This is a comment and will be ignored by Python.
#   This class is the Mclaren class and inherits from the class Car being the child class.

# PT-BR: Importa o arquivo car.py e importa a classe Car
# EN: Imports the file car.py and imports the class Car
from car import Car

class Mclaren(Car):
    """ 
        PT-BR:
            Isso é um comentário padrão de classe e será ignorado pelo Python
            A class Mclaren herda de Car tem a propiedade/atributo Brand definida como 'Mclaren',
            também propiedade/atributo Color definida como None (vazio), e por último a propriedade nova, 
            inexistente na classe Car, Model, que está definida como None (vazio).
        EN: 
            This is a function comment and will be ignored by Python.
            The class Mclaren inherits from Car and has the property/attribute Brand defined 
            with the value 'Mclaren', also the property/attribute Color defined as None (empty), and for last,
            a new property, that does not exists in the class Car, Model, that is defined as None (empty).
    """
    Brand = 'McLaren'
    Color = None
    Model = None