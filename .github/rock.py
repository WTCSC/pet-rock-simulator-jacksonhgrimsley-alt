class PetRock:
    def __init__(self):
        self.hunger = 1        
        self.happiness = 5     
        self.alive = True

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print("You fed the rock. Less hungry.")
        else:
            print("The rock isn't hungry.")
        self._decrease_happiness()

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            print("You played with the rock. Happier!")
        else:
            print("The rock is already very happy!")
        self._increase_hunger()

    def _decrease_happiness(self):
        if self.happiness > 0:
            self.happiness -= 1
            print("But it feels a bit bored...")

    def _increase_hunger(self):
        if self.hunger < 10:
            self.hunger += 1
            print("But now it's hungrier...")

    def status(self):
        print(f"\nStatus => Hunger: {self.hunger}/10, Happiness: {self.happiness}/10\n")

    def check_endgame(self):
        print("\n--- Final Result ---")
        if self.hunger >= 10:
            print("Your rock starved.")
        elif self.happiness <= 0:
            print("Your rock became too sad and gave up.")
        elif self.hunger == 0 and self.happiness == 10:
            print("Perfect care! Your rock thrives!")
        else:
            print("Your time is up. The rock survives, but it's just... okay.")
        self.alive = False


rock = PetRock()
print("Welcome to the 3-Turn Pet Rock Simulator!")
rock.status()

for turn in range(1, 4):
    print(f"--- Turn {turn} ---")
    choice = input("Do you want to 'feed' or 'play' with your rock? ").strip().lower()
    if choice == 'feed':
        rock.feed()
    elif choice == 'play':
        rock.play()
    else:
        print("Invalid choice. Turn wasted.")
    
    rock.status()

rock.check_endgame()
