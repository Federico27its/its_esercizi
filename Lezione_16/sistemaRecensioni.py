class Media():
    def __init__(self, title:str, reviews: list[int]) -> None:
        self.set_title(title)
        self.reviews = reviews

    def set_title(self, title: str) -> None:
        self.title= title

    def get_title(self) -> str:
        return self.title
    
    def aggiungiValutazione(self, voto: int) -> None:
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            raise ValueError("Voto non valido")
        
    def getMedia(self) -> str:
        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self) -> str:
        media = round(self.getMedia())
        if media == 1:
            return "Terribile"
        elif media == 2:
            return "Brutto"
        elif media == 3:
            return "Normale"
        elif media == 4:
            return "Bello"
        else:
            return "Grandioso"
        
    def ratePercentage(self, voto) -> str:
        c = self.reviews.count(voto)
        return f"{(c*100)/len(self.reviews):.2f}%"
    
    def recensione(self) -> None:
        print(f"Titolo del Media: {self.title}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1)}\nBrutto: {self.ratePercentage(2)}\nNormale: {self.ratePercentage(3)}\nBello: {self.ratePercentage(4)}\nGrandioso: {self.ratePercentage(5)}")

class Film(Media):
    def __init__(self, titolo: str, reviews: list[int]):
        super().__init__(titolo, reviews)
    def recensione(self) -> None:
        print(f"Titolo del Film: {self.title}\nVoto Medio: {self.getMedia():.2f}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1)}\nBrutto: {self.ratePercentage(2)}\nNormale: {self.ratePercentage(3)}\nBello: {self.ratePercentage(4)}\nGrandioso: {self.ratePercentage(5)}")

f = Film("Titolone", [1, 2, 3, 3, 4, 3])
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.aggiungiValutazione(5)
f.recensione()

