'''
from persona import Persona

fr: Persona = Persona("Federico", "Rotella", 29)
print(fr)
print(fr.lastname)
fr.displayData()'''

from persona2 import Persona

fr: Persona = Persona()
fr.setName("Federico")
fr.setLastname("Rotella")
fr.setAge(29)

print("--------------")

fr.displayData()

print(fr.getName(), fr.getLastname(), fr.age())