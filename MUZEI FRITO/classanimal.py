class Animal:
    def __init__(self, name, species, habitat):
        
        self.name = name
        self.species = species
        self.habitat = habitat

    def describe_habitat(self):
        return f"{self.name} the {self.species} lives in {self.habitat}."

# Example usage:
lion = Animal("Simba", "Lion", "African savanna")
print(lion.describe_habitat())  # Output: Simba the Lion lives in African savanna.