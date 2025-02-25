class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

# Decorator to add milk
class MilkDecorator:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + " with milk"

# Decorator to add sugar
class SugarDecorator:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 0.5

    def description(self):
        return self.coffee.description() + " with sugar"

# Start with plain coffee:
my_coffee = Coffee()
print("Base:", my_coffee.description(), "Cost:", my_coffee.cost())

# Add milk:
my_coffee = MilkDecorator(my_coffee)
print("After milk:", my_coffee.description(), "Cost:", my_coffee.cost())

# Add sugar:
my_coffee = SugarDecorator(my_coffee)
print("After sugar:", my_coffee.description(), "Cost:", my_coffee.cost())