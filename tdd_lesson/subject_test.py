class Pies():
    def __init__(self,imie):
        self.imie=imie

    def get_imie(self):
        return self.imie


reksio=Pies('reksio')
print(reksio.get_imie())