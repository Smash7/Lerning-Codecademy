# 1.
class Menu:
    # 2.
    def __init__(self, name: str, items: dict, start_time: int, end_time: int):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # 9.
    def calculate_bill(self, purchased_items: list) -> int:
        total_price = 0
        for i in purchased_items:
            if i in self.items:
                total_price += self.items[i]
        return total_price

    # 7-8
    def __repr__(self):
        return "{name} menu available from {start} to {end}".format(name=self.name, start=self.start_time,
                                                                    end=self.end_time)


# 12-13
class Franchise:
    def __init__(self, address: str, menus: list):
        self.address = address
        self.menus = menus

    # 15.
    def __repr__(self):
        return self.address

    # 16.
    def available_menus(self, time: int) -> list:
        available_menu = []
        for i in self.menus:
            if i.start_time <= time <= i.end_time:
                # print(i)?
                available_menu.append(i)
        return available_menu


# 19-20
class Business:
    def __init__(self, name: str, franchises: list):
        self.name = name
        self.franchises = franchises


# 3.
brunch = Menu("brunch", {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}, 11, 16)

# 4.
early_bird = Menu("early bird", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}, 15, 18)

# 5.
dinner = Menu("dinner", {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}, 17, 23)

# 6.
kids = Menu("kids", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}, 11, 21)

# 22.
arepas_menu = Menu("arepa", {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}, 10, 20)

# 10.
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# 11.
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# 14.
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# 17.
print(flagship_store.available_menus(12))

# 18.
print(flagship_store.available_menus(17))

# 21.
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# 23.
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# 24
second_business = Business("Take a' Arepa", [arepas_place])
