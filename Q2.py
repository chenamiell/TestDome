class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combination_list = list()
        for ingredient in self.ingredients:
            for topping in self.toppings:
                combination_list.append([ingredient, topping])
        return combination_list


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())