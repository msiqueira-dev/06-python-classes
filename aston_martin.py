# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python.
#   Essa classe é a classe Aston_Martin e herda da classe Car sendo então a classe filho.
# EN: 
#   This is a comment and will be ignored by Python.
#   This class is the Aston_Martin class and inherits from the class Car, being the child class.

# PT-BR: Importa o arquivo car.py e importa a classe Car
# EN: Imports the file car.py and imports the class Car
from car import Car

class Aston_Martin(Car):
    """ 
        PT-BR:
            Isso é um comentário padrão de classe e será ignorado pelo Python
            A class Aston_Martin herda de Car tem a propiedade/atributo Brand definida como 'Aston_Martin',
            também propiedade/atributo Color definida como None (vazio), e por último a propriedade nova, 
            inexistente na classe Car, Model, que está definida como None (vazio).
        EN: 
            This is a function comment and will be ignored by Python.
            The class Aston_Martin inherits from Car and has the property/attribute Brand defined 
            with the value 'Aston_Martin', also the property/attribute Color defined as None (empty), and for last,
            a new property, that does not exists in the class Car, Model, that is defined as None (empty).
    """
    Brand = 'Aston_Martin'
    Color = None
    Model = None