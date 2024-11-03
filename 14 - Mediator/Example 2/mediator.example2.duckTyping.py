class Aircraft:
    def __init__(self, tower, name):
        self.tower = tower
        self.name = name
        tower.register_aircraft(self)

    def send_message(self, message):
        self.tower.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")

class Airplane(Aircraft):
   pass

class Helicopter(Aircraft):
    pass

class Tower:
    def __init__(self):
        self.aircrafts = []

    def register_aircraft(self, aircraft):
        if aircraft not in self.aircrafts:
            self.aircrafts.append(aircraft)

    def send_message(self, sender, message):
        for aircraft in self.aircrafts:
            if aircraft is not sender:
                aircraft.receive_message(message)


tower = Tower()
airplane1 = Airplane(tower, "Airplane1")
airplane2 = Airplane(tower, "Airplane2")

airplane1.send_message("Hello from Airplane1!")