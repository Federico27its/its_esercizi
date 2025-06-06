'''1. Classe Movie:
Attributi:
● movie_id: str - Identificatore di un film.
● title: str - Titolo del film.
● director: str - Regista del film.
● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:
● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
film '{self.title}' è già noleggiato."
● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
stato noleggiato da questo cliente."'''

class Movie():
    def __init__(self, movie_id: str, title:str , director:str, is_rented: bool = False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
    
    def rent(self):
        if  not self.is_rented:
            self.is_rented = True
        else: 
            print(f"Il film '{self.title}' è già noleggiato")

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da quersto clienete")


'''2. Classe Customer:
Attributi:
● customer_id: str - Identificativo del cliente.
● name: str - Nome del cliente.
● rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:
● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
noleggiato."
● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
noleggiato da questo cliente."'''

class Customer:
    def __init__(self,customer_id: str, name:str, rented_movies: list[Movie] = None):
        self.customer_id = customer_id
        self.name = name
        if rented_movies:
            self.rented_movies = rented_movies
        else:
            self.rented_movies = []

    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"Il film '{movie.title} è già noleggiato")
        
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film '{movie.title} non è stato noleggiato da questo cliente")

'''3. Classe VideoRentalStore:
Attributi:
● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
l'oggetto Movie.
● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
valore l'oggetto Customer.
Metodi:
● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
ID '{movie_id}' esiste già."
● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
con ID '{customer_id}' è già registrato."
● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.'''

class VideoRentalStore:
    def __init__(self, movies:dict[str, Movie] = [], customers: dict[str, Customer] = []):
        if movies:
            self.movies = movies
        else:
            self.movies = {}
        if customers:
            self.customers = customers
        else:
            self.customers = {}

    def add_movie(self, movie_id: str, title:str, director: str):
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director)
        else:
            print("Il film con ID '{movie_id}' esiste già")

    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        else:
            print(f"Il cliente con ID '{customer_id}' è già registrato")

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato")

    '''● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."'''
    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato")

    '''● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.'''
    def get_rented_movies(self, customer_id: str) ->list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato")
            return []
        
print("TEST VIDEO RENTAL STORE")

store = VideoRentalStore()

# Test 1: aggiunta film
store.add_movie("M003", "Interstellar", "Christopher Nolan")
store.add_movie("M004", "The Prestige", "Christopher Nolan")

# Test 2: aggiunta film duplicato
store.add_movie("M003", "Duplicato", "Qualcuno")  # ⚠️ "Il film con ID 'M003' esiste già."

# Test 3: registrazione cliente
store.register_customer("C002", "Bob")
store.register_customer("C003", "Carla")

# Test 4: registrazione cliente duplicato
store.register_customer("C002", "Bob Clone")  # ⚠️ "Il cliente con ID 'C002' è già registrato."

# Test 5: noleggio film disponibile
store.rent_movie("C002", "M003")  # ✅ Bob noleggia Interstellar
print([m.title for m in store.customers["C002"].rented_movies])  # ['Interstellar']
print(store.movies["M003"].is_rented)  # True

# Test 6: noleggio film già noleggiato
store.rent_movie("C003", "M003")  # ⚠️ "Il film 'Interstellar' è già noleggiato."

# Test 7: noleggio con cliente o film inesistente
store.rent_movie("C999", "M003")  # ⚠️ "Cliente o film non trovato."
store.rent_movie("C002", "M999")  # ⚠️ "Cliente o film non trovato."

# Test 8: restituzione corretta
store.return_movie("C002", "M003")  # ✅ Bob restituisce Interstellar
print(store.movies["M003"].is_rented)  # False

# Test 9: restituzione già effettuata → errore
store.return_movie("C002", "M003")  # ⚠️ "Il film 'Interstellar' non è stato noleggiato da questo cliente."

# Test 10: restituzione con dati errati
store.return_movie("C999", "M003")  # ⚠️ "Cliente o film non trovato."

# Test 11: visualizzazione film noleggiati
store.rent_movie("C003", "M004")
print([m.title for m in store.get_rented_movies("C003")])  # ['The Prestige']

# Test 12: richiesta film noleggiati da cliente inesistente
store.get_rented_movies("C999")  # ⚠️ "Cliente o film non trovato." o errore gestito

print()
