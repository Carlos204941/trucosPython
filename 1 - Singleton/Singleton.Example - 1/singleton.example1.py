class MySingleton:
     _instance = None

     def __new__(cls):
          if cls._instance is None:
                print("Creating the new Singleton's instance")
                cls._instance = super(MySingleton, cls).__new__(cls)
          return cls._instance
     
singleton = MySingleton()     