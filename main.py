# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python.
#   Esse código tem como objetivo explicar classes e programação orientada a objeto.
# EN: 
#   This is a comment and will be ignored by Python.
#   This code has the objective to explain classes and object oriented programming.


# PT-BR: Importa os arquivos car.py, aston_martin.py, ferrari.py, mclaren.py importando 
#        suas respectivas classes existentes em cada arquivo.
# EN: Imports the files car.py, aston_martin.py, ferrari.py, mclaren.py importing
#        its respectively existing classes in each file.

from car import Car
from aston_martin import Aston_Martin
from ferrari import Ferrari
from mclaren import Mclaren

# PT-BR: Cria os objetos a partir das classes, armazenando em variaveis diferentes respectivamente, 
#        essas variaveis depois de sua criação, são consideradas objetos.
# EN: Creates the objects from the classes, storing in different variables respectively,
#     these variables are considered objects after their creation.
car_obj = Car()
aston_martin_obj = Aston_Martin()
ferrari_obj = Ferrari()
mclaren_obj = Mclaren()

# PT-BR: Imprime a propiedade/atributo para saber verificar o valor de cada uma.
# EN: Print property/attribute from each objective to see their value.
print(car_obj.Brand)
print(aston_martin_obj.Brand)
print(ferrari_obj.Brand)
print(mclaren_obj.Brand)