class Enemy():
    life = 3
    def attack(self):
        print("OoooUuuuuch")
        self.life -=1
    def checklife(self):
        if self.life <= 0:
            print("i'm dead.......")
        else:
            print(str(self.life) + " lifes left")


e = Enemy()
e.attack()
e.attack()
e.attack()
e.attack()
e.checklife()