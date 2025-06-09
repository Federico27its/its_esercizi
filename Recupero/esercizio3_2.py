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


    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato")


    def get_rented_movies(self, customer_id: str) ->list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato")
            return []
        
