class Building:
   def __init__(self, doors, windows, floors):
       self.doors = doors
       self.windows = windows
       self.floors = floors

class CalonMixin:
    def strigka(self, f):
        pass
    def manikur(self, n):
        pass
    def time_work(self,time_open,time_close, current_time=None):
        if current_time >= time_open and current_time < time_close:
            print(f'Салон открыт: {time_open} - {time_close} до закрытия {time_close - current_time} часов')
        else:
            print("Салон закрыт")

class BuildingWithCalonMixin(Building,CalonMixin):
    def __init__(self, doors, windows, floors):
        super(BuildingWithCalonMixin, self).__init__(floors, windows, doors)

hws = BuildingWithCalonMixin(3, 15, 17)
hws.time_work(10, 21, 20)
