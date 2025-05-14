from persona import Persona
from alieno import Alieno

# creare un oggetto p della classe persona
p: Persona = Persona("Federico", "Rotella", 29)

# visualizzare le informazioni dell'oggetto p
print(p)


# creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")

# visualizzare le informazioni dell'oggetto et
print(et)

# l'oggetto p invochi il metodo speak
p.speak()

# l'oggetto et invochi il metodo speak
et.speak()

 