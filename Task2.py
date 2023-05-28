#Task 2
# Для попереднього проєкту (Меню Ресторану)
# реалізувати можливість додавання страв з меню до замовлення через оператор "+=".

class Dish:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} uah'


class Order:

    def __init__(self):
        self.dishes = []
        self.quantities = []

    def __iadd__(self, other: tuple):
        if isinstance(other, tuple):
            if len(other) == 1 and isinstance(other[0], Dish):
                self.dishes.append(other[0])
                self.quantities.append(1)
                return self
            if len(other) == 2 and isinstance(other[0], Dish) and isinstance(other[1], int | float):
                self.dishes.append(other[0])
                self.quantities.append(other[1])
                return self
        if isinstance(other, Dish):
            self.dishes.append(other)
            self.quantities.append(1)
            return self
        return NotImplemented

    def __str__(self):
        res = ''
        for dish, quantity in zip(self.dishes, self.quantities):
            res += f'{dish} x {quantity} = {dish.price * quantity} uah\n '
        return res


dish_1 = Dish('Страва 1', 100)
dish_2 = Dish('Страва 2', 101)
dish_3 = Dish('Страва 3', 102)
dish_4 = Dish('Страва 4', 103)
dish_5 = Dish('Страва 5', 104)
dish_6 = Dish('Страва 6', 105)
dish_7 = Dish('Страва 7', 106)
dish_8 = Dish('Страва 8', 107)
dish_9 = Dish('Страва 9', 108)
dish_10 = Dish('Страва 10', 109)

order_1 = Order()
order_1 += dish_1
order_1 += (dish_2, )
order_1 += (dish_3, 2)
print(order_1)
