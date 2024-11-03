from abc import ABC, abstractmethod

class IDatabase(ABC):
    @abstractmethod
    def add(self, data: str) -> None:
        pass

    @abstractmethod
    def retrieve(self) -> str:
        pass

class LegacyDatabase:
    def insert_data(self, data: str) -> None:
        print(f"Inserted data into legacy database: {data}")

    def get_data(self) -> str:
        return "Data from legacy database"

class DatabaseAdapter(IDatabase):   
    def __init__(self, legacy_database): 
        self.legacy_database = legacy_database

    def add(self, data: str) -> None:
        self.legacy_database.insert_data(data)    

    def retrieve(self) -> str:
        return self.legacy_database.get_data()
    

class NewSystem:
    def __init__(self, database: IDatabase):
        self.database = database

    def save_data(self, data: str) -> None:
        self.database.add(data)
        print("Data saved in the new system.")

    def load_data(self) -> None:
        data = self.database.retrieve()
        print(f"Data loaded in the new system: {data}")


legacy_database = LegacyDatabase()
adapter = DatabaseAdapter(legacy_database)

new_system = NewSystem(adapter)
new_system.save_data("Important data")
new_system.load_data()
