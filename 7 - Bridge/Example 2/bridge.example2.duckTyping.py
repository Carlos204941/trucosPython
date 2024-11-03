class Bus:
    def __init__(self, engine):
        self._engine = engine

    def drive(self):
        print("Driving the bus")
        self._engine.start()

class Car:
    def __init__(self, engine):
        self._engine = engine

    def drive(self):
        print("Driving the car")
        self._engine.start()

class ElectricEngine:
    def start(self):
        print("Starting the electric engine")

    def stop(self):
        print("Stopping the electric engine")

class PetrolEngine: 
    def start(self):
        print("Starting the petrol engine")

    def stop(self):
        print("Stopping the petrol engine")    

   
car_with_petrol_engine = Car(PetrolEngine())
car_with_petrol_engine.drive()

bus_with_electric_engine = Bus(ElectricEngine())
bus_with_electric_engine.drive()