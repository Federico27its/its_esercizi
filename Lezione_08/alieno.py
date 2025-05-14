class Alieno:
    '''Della classe alieno ci interessa la galassia di provenienza
    self.galaxy: str'''

    def __init__(self, galaxy: str) -> None:
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) -> None:
        if galaxy:
            self.galaxy = galaxy

        else:
            print("Errore! La galassia di provenienza non può essere una stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print(f"fgreguykiluhtr")

    def __str__(self) -> str:
        return f"Alieno proveniente dalla galassia {self.getGalaxy()}"