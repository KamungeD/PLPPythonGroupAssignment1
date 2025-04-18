from pet import Pet

# Create a pet object
my_pet = Pet("Bosco")

# Test the pet's methods
print("Creating pet: Bosco")
my_pet.get_status()

print("\nBosco is eating...")
my_pet.eat()
my_pet.get_status()

print("\nBosco is playing...")
my_pet.play()
my_pet.get_status()

print("\nBosco is sleeping...")
my_pet.sleep()
my_pet.get_status()


print("\nBosco is learning tricks...")
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.show_tricks()

print("\nBosco's final stats are:")
my_pet.get_status()
