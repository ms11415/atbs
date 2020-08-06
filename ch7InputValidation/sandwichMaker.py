import pyinputplus as pyip


print('WELCOME TO SOBWEI')
sandwich = {}
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], 'Choose a bread type:\n')
protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], 'Choose a protein:\n')
sandwich.update({'Bread': bread, 'Protein': protein})
cheese = pyip.inputYesNo('Would you like to add cheese?\n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], 'Please choose a cheese:\n')
    sandwich.update({'Cheese': cheeseType})
numSandwich = pyip.inputInt('How many sandwiches would you like?\n', min=1)
if numSandwich > 1:
    noun = 'sandwiches'
else:
    noun = 'sandwich'
prices = {'Wheat': 1.50, 'White': 1.25, 'Sourdough': 1.75,
          'Chicken': 3.00, 'Turkey': 2.50, 'Ham': 2.00, 'Tofu': 2.75,
          'Cheddar': 1.00, 'Swiss': 1.25, 'Mozzarella': 1.50}
print('You ordered', numSandwich, noun, 'with the following options:')
for k, v in sandwich.items():
    print(k, ':', v, ' - ', prices[v])
total = 0.00
for item in sandwich.values():
    total += prices[item]
total *= numSandwich
print('Your total is', total)