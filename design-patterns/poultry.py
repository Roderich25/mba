class Duck:

    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


class Turkey:

    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")


class TurkeyAdapter:

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def quack(self):
        self.adaptee.gobble()

    def fly(self):
        for _ in range(5):
            self.adaptee.fly()


def duck_interaction(duck):
    duck.quack()
    duck.fly()


duck = Duck()
turkey = Turkey()
turkey_adapter = TurkeyAdapter(turkey)

print("The Turkey says ...")
turkey.gobble()
turkey.fly()

print("\nThe Duck says ...")
duck_interaction(duck)

print("\nThe TurkeyAdapter says ...")
duck_interaction(turkey_adapter)
