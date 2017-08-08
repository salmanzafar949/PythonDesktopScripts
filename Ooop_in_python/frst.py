class fighter:
    def __init__(self, x):
        self.eneregy = x
    def get_energy(self):
        print(self.eneregy)

salman = fighter(10)
sam = fighter(20)

salman.get_energy()
sam.get_energy()