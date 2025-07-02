class Documento:
    def __init__(self, testo: str) -> None:
        self.setText(testo)
    
    def setText(self, testo: str) -> None:
        self.testo = testo

    def getText(self) -> str:
        return self.testo
    
    def isInText(self, testo: str) -> bool:
        return testo in self.testo

class Email(Documento):
    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(testo)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo)

    def setMittente(self, mittente: str) -> None:
        self.mittente = mittente

    def getMittente(self) -> str:
        return self.mittente
    
    def setDestinatario(self, destinatario: str) -> None:
        self.destinatario = destinatario

    def getDestinatario(self) -> str:
        return self.destinatario
    
    def setTitolo(self, titolo: str) -> None:
        self.titolo = titolo

    def getTitolo(self) -> str:
        return self.titolo
    
    def getText(self) -> str:
        return f"Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}"

    def writeToFile(self, path: str) -> None:
        path += ".txt"
        with open(path, mode = "w") as file:
            file.write(self.getText())

class File(Documento):

    def __init__(self, nomePercorso: str):
        self.setNomePercorso(nomePercorso)
        super().__init__(self.leggiTestoDaFile())


    def setNomePercorso(self, nomePercorso: str) -> None:
        self.nomePercorso = nomePercorso

    def getNomePercorso(self) -> str:
        return self.nomePercorso
    
    def leggiTestoDaFile(self) -> str:
        with open(self.getNomePercorso(), "r") as file:
           return file.read()

    def getText(self) -> str:
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"
    


if __name__ == "__main__":
    email: Email = Email("Ciao Bob, possiamo incontrarci domani?", "alice@example.com", "bob@example.com", "Incontro")
    file: File = File("document.txt")

    print(email.getText())
    print(file.getText())

    email.writeToFile("/home/its/new_its_esercizi/Lezione_21/email")
    print(email.isInText("incontrarci"))
    print(file.isInText("percorso"))