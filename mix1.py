class Building:
   def __init__(self, doors, windows, floors):
       self.doors = doors
       self.windows = windows
       self.floors = floors

class CalonMixin:
    min_cost = 10
    def strigka(self, f):
        if f > 50:
            return CalonMixin.min_cost + CalonMixin.min_cost * 80/100
        elif f >= 30 and f <=50:
            return CalonMixin.min_cost + CalonMixin.min_cost * 50/100
        else:
            return CalonMixin.min_cost + CalonMixin.min_cost * 20/100

    def manikur(self):
        return CalonMixin.min_cost + CalonMixin.min_cost * 20/100

    def time_work(self,time_open,time_close, current_time=None):
        if current_time >= time_open and current_time < time_close:
            print(f'Салон открыт: {time_open} - {time_close} до закрытия {time_close - current_time} часов')
        else:
            print("Салон закрыт")

class BuildingWithCalonMixin(Building,CalonMixin):
    pass

hws = BuildingWithCalonMixin(3, 15, 17)
hws.time_work(10, 21, 20)
print(f"Стоимость маникюра {hws.manikur()}")
print(f"Стоимость стрижки с длинной волос до 30 см {hws.strigka(20)}")
print(f"Стоимость стрижки с длинной волос от 30 до 50 см {hws.strigka(40)}")
print(f"Стоимость стрижки с длинной волос более 50 см {hws.strigka(100)}")