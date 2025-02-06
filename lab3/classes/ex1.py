class Stringg:
    def __init__(self):
        slova = " "
    def get_string(self):
        self.slova = input()
    def printString(self):
        print(self.slova.upper())
slova = Stringg()
slova.get_string()
slova.printString()