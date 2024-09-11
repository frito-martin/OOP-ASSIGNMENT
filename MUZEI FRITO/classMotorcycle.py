class Motorcycle:
    def __init__(self, brand, model, fuel_tank_capacity, fuel_efficiency):
        
        self.brand = brand
        self.model = model
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_efficiency = fuel_efficiency

    def calculate_range(self):
        """

        Returns:
            float: The estimated range in kilometers.
        """
        return self.fuel_tank_capacity * self.fuel_efficiency

# Example usage:
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 12, 20)
print(motorcycle.calculate_range())  # Output: 240