# class Pencil:

#     def __init__(self, color='серый'):
#         self.color = color
    
#     def draw_picture(self):
#         return f"Нарисован рисунок цветом {self.color}."
    
# class Pen(Pencil):

#     def __init__(self, color, pen_type):
#         super().__init__(color=color)
#         self.pen_type = pen_type

#     def sign_document(self):
#         if self.color not in ("синий","черный","фиолетовый"):
#             return f"Ручкой цвета {self.color} нельзя подписать документ"
#         elif self.pen_type == 'гелевая':
#             return f'Ручкой типа {self.pen_type} нельзя подписать документ'
#         return f"Документ подписан"
    
#     def draw_picture(self):
#         return f"Нарисован рисунок ручкой {self.pen_type}, цветом {self.color}."
    
# blue_pen = Pen(color="синий", pen_type="шариковая")
# print(blue_pen.draw_picture())
# print(blue_pen.sign_document())

# red_pen = Pen(color="синий", pen_type='гелевая')
# print(red_pen.draw_picture())
# print(red_pen.sign_document())

# class GreetingFormal:

#     def __init__(self):
#         self.formal_greeting = "Добрый день, "

#     def greet_formal(self, name):
#         return f"{self.formal_greeting} {name}!"

# class GreetingInformal:

#     def __init__(self):
#         self.informal_greeting = "Привет, "

#     def greet_informal(self, name):
#         return  f"{self.informal_greeting} {name}!"

# class GreetingMix(GreetingFormal, GreetingInformal):

#     def __init__(self):
#         GreetingFormal.__init__(self)
#         GreetingInformal.__init__(self)

# mixed_greeting = GreetingMix()
# print(mixed_greeting.greet_formal("Пользователь"))
# print(mixed_greeting.greet_informal("Пользователь"))

class Car:
    
    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен"
        return "Двигатель уже был запущен или нет топлива"

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен"
        return "Двигатель уже был остановлен"  

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен"
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива"
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."  
    
    def refuel(self):
        self.reserve = self.tank_volume
        return "Бак заправлен полностью!"

    def get_mileage(self):
        return f"Пробег {self.mileage} км."

    def get_reserve(self):
        return self.reserve
    
    def get_consumption(self):
        return self.consumption


class ElectricCar(Car):

    def __init__(self, color, consumption, bat_capacity, mileage=0):
        super().__init__(color, consumption, bat_capacity, mileage)
        self.bat_capacity = bat_capacity

    def __str__(self):
        return f"Электромобиль." \
                f"Цвет: {self.color}" \
                f"Пробег: {self.mileage} км." \
                f"Остаток заряда: {self.reserve} кВт*ч"
                
    def __repr__(self):
        return f"Электромобиль." \
                f"Цвет: {self.color}" \
                f"Пробег: {self.mileage} км." \
                f"Остаток заряда: {self.reserve} кВт*ч"
    

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен"
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас заряда"
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч." 
    
    def recharge(self):
        self.reserve = self.bat_capacity


electric_car = ElectricCar(color="white", consumption=15, bat_capacity=90)
print(repr(electric_car))
electric_car_2 = ElectricCar(color="black", consumption=25, bat_capacity=70)
print([electric_car, electric_car_2])