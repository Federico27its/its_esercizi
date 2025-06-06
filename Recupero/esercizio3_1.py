'''Metodi:
● create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto,
aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri
di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il
messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
● add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero
di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo
contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il
contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero
di telefono è già presente per il contatto specificato.
● remove_phone_number(contact_name: str, phone_number: str): Rimuove un
numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il
solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se
il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il
numero di telefono non esiste per il contatto specificato.
● update_phone_number(contact_name: str, old_phone_number: str,
new_phone_number: str): Sostituisce un numero di telefono con un altro nel
contatto specificato. Restituisce un nuovo dizionario con il solo contatto
aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non
esiste oppure "Errore: il numero di telefono non è presente." se il numero di
telefono non esiste per il contatto specificato.
● list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario
contacts.
● list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un
contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di
errore "Errore: il contatto non esiste." se il contatto non esiste.
● search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i
contatti che contengono un determinato numero di telefono. Restituisce una lista
di tutte le chiavi all'interno del dizionario contacts che hanno il numero
specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con
questo numero di telefono." se nessun contatto contiene il numero di telefono.'''

class ContactManager():

    contacts: dict[str, list[str]]

    def __init__(self, contacts: dict[str, list[str]] = None):
        if contacts:
            self.contacts = contacts
        else:
            self.contacts = {}

    '''● create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto,
aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri
di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il
messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.'''
    def create_contact(self, name: str, phone_numbers: list[str]):
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return {name: phone_numbers}
        print("Errore: il contatto esiste già")

    '''● add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero
di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo
contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il
contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero
di telefono è già presente per il contatto specificato.'''
    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                self.contacts[contact_name].append(phone_number)
            else:
                print("Errore: il numero di telefono esiste già")
        else:
            print("Errore: ill contatto non esiste")


    ''' remove_phone_number(contact_name: str, phone_number: str): Rimuove un
numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il
solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se
il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il
numero di telefono non esiste per il contatto specificato.'''
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                return {contact_name: self.contacts[contact_name]}
            else:
                print("Errore: il numero di telefono non è presente")
        else:
            print("Errore: il contatto non esiste")

    '''● update_phone_number(contact_name: str, old_phone_number: str,
new_phone_number: str): Sostituisce un numero di telefono con un altro nel
contatto specificato. Restituisce un nuovo dizionario con il solo contatto
aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non
esiste oppure "Errore: il numero di telefono non è presente." se il numero di
telefono non esiste per il contatto specificato.'''
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
            else:
                print("Errore: il numero di telefono non è presente")
        else:
            print("Errore: il contatto non esiste")

    '''● list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario
contacts.'''
    def list_contacts(self):
        return list(self.contacts.keys())
    
    '''● list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un
contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di
errore "Errore: il contatto non esiste." se il contatto non esiste.'''
    def list_phone_numbers(self, contact_name: str):
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        print("Errore: il contatto non esiste")


    '''● search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i
contatti che contengono un determinato numero di telefono. Restituisce una lista
di tutte le chiavi all'interno del dizionario contacts che hanno il numero
specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con
questo numero di telefono." se nessun contatto contiene il numero di telefono.'''
    def search_contact_by_phone_number(self, phone_number: str):
        l = []
        for key, value in self.contacts.items():
            if phone_number in value:
                l.append(key)
        return l if l else print("Nessun contatto trovato con questo numero di telefono")

rubrica = ContactManager()

# Test 1: Creazione contatto nuovo
print(rubrica.create_contact("Mario Rossi", ["1234567890"]))
# Atteso: {"Mario Rossi": ["1234567890"]}

# Test 2: Creazione contatto già esistente
print(rubrica.create_contact("Mario Rossi", ["0987654321"]))
# Atteso: "Errore: il contatto esiste già."

# Test 3: Aggiunta numero a contatto esistente
print(rubrica.add_phone_number("Mario Rossi", "0987654321"))
# Atteso: {"Mario Rossi": ["1234567890", "0987654321"]}

# Test 4: Aggiunta numero già esistente
print(rubrica.add_phone_number("Mario Rossi", "1234567890"))
# Atteso: "Errore: il numero di telefono esiste già."

# Test 5: Aggiunta numero a contatto inesistente
print(rubrica.add_phone_number("Luigi Verdi", "1112223333"))
# Atteso: "Errore: il contatto non esiste."

# Test 6: Rimozione numero esistente
print(rubrica.remove_phone_number("Mario Rossi", "1234567890"))
# Atteso: {"Mario Rossi": ["0987654321"]}

# Test 7: Rimozione numero non presente
print(rubrica.remove_phone_number("Mario Rossi", "0000000000"))
# Atteso: "Errore: il numero di telefono non è presente."

# Test 8: Rimozione da contatto inesistente
print(rubrica.remove_phone_number("Luigi Verdi", "1231231234"))
# Atteso: "Errore: il contatto non esiste."

# Test 9: Aggiorna numero presente
print(rubrica.update_phone_number("Mario Rossi", "0987654321", "2223334444"))
# Atteso: {"Mario Rossi": ["2223334444"]}

# Test 10: Aggiorna numero non presente
print(rubrica.update_phone_number("Mario Rossi", "9999999999", "1111111111"))
# Atteso: "Errore: il numero di telefono non è presente."

# Test 11: Aggiorna numero in contatto inesistente
print(rubrica.update_phone_number("Luigi Verdi", "111", "222"))
# Atteso: "Errore: il contatto non esiste."

# Test 12: Lista contatti
print(rubrica.list_contacts())
# Atteso: ["Mario Rossi"]

# Test 13: Lista numeri di un contatto esistente
print(rubrica.list_phone_numbers("Mario Rossi"))
# Atteso: ["2223334444"]

# Test 14: Lista numeri di un contatto inesistente
print(rubrica.list_phone_numbers("Giovanni Bianchi"))
# Atteso: "Errore: il contatto non esiste."

# Test 15: Ricerca contatto per numero
rubrica.create_contact("Anna Neri", ["2223334444", "5556667777"])
print(rubrica.search_contact_by_phone_number("2223334444"))
# Atteso: ["Mario Rossi", "Anna Neri"]

print(rubrica.search_contact_by_phone_number("0000000000"))
# Atteso: []
