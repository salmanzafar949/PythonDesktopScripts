class parent():
    def prnt_frst_name(self):
        print("Salman")
class child(parent):
    def prnt_last_name(self):
        print("Zafar")

class child1(child):
    def prnt_age(self):
        print("22")

a = child1()
a.prnt_frst_name()
a.prnt_last_name()
a.prnt_age()