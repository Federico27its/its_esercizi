from formaGenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()
        
        self.setShape("rettangolo")

    def draw(self) -> None:
        print(f"\n{self.getShape()}\n")

        for i in range(5):
            for j in range(5*2):
                if i == 0 or i == 5-1:
                    print("*", end = "  ")
                elif j == 0 or j == 10-1:
                    print("*", end = "  ")
                else:
                    print(" ", end = "  ")
            print("\n")

