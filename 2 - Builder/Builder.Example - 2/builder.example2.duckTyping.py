class Burger:
    def __init__(self):
           self.bread = ""
           self.meat = ""
           self.cheese = ""
           self.dressing = ""
           self.lettuce = False
           self.tomato = False

    def display_information(self):
          print(f"Bread: {self.bread}, Meat: {self.meat}, Cheese: {self.cheese}, Dressing: {self.dressing}, Lettuce: {self.lettuce},Tomato: {self.tomato}")

class ClassicBurgerBuilder:
      def __init__(self):
            self.burger = Burger()

      def add_bread(self):
            self.burger.bread = "Sesame bread"

      def add_cheese(self):
            self.burger.cheese = "Cheddar"

      def add_dressing(self):
            self.burger.dressing = "Kétchup"

      def add_lettuce(self):
            self.burger.lettuce = True

      def add_tomato(self):
        self.burger.tomato = True

      def add_meat(self):
        self.burger.meat = "Chicken"

      def get_burger(self):
        return self.burger


class VeggieBurgerBuilder:
      def __init__(self):
            self.burger = Burger()

      def add_bread(self):
            self.burger.bread = "Whole Wheat"

      def add_cheese(self):
            self.burger.cheese = "Vegan cheese"

      def add_dressing(self):
            self.burger.dressing = "Vegan mayo"

      def add_lettuce(self):
            self.burger.lettuce = True

      def add_tomato(self):
        self.burger.tomato = True

      def add_meat(self):
        self.burger.meat = "Lentil patty"

      def get_burger(self):
        return self.burger


class BurgerDirector:
     def make_burger(self, burger_builder):
           burger_builder.add_bread()
           burger_builder.add_meat()
           burger_builder.add_cheese()
           burger_builder.add_dressing()
           burger_builder.add_lettuce()
           burger_builder.add_tomato()


chef = BurgerDirector()

classic_builder = ClassicBurgerBuilder()
chef.make_burger(classic_builder)
classic_burger = classic_builder.get_burger()
print("Classic Burger:")
classic_burger.display_information()

veggie_builder = VeggieBurgerBuilder()
chef.make_burger(veggie_builder)
veggie_burger = veggie_builder.get_burger()
print("Veggie Burger:")
veggie_burger.display_information()



            
    
    

       


    