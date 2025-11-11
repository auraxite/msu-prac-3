class Sender:
    first = True

    @classmethod
    def report(self):
        if self.first:
            self.first = False
            print("Greetings!")
        else:
            print("Get away!")

class Asker:
    @staticmethod
    def askall(lst):
        for el in lst:
            el.report()

sender1, sender2, sender3 = Sender(), Sender(), Sender()
asker = Asker()
asker.askall([sender1, sender2, sender3])