class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        if self.energy >= 3:
            self.energy -= 3
            self.happiness = min(10, self.happiness + 1)
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
