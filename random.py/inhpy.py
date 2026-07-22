class Animal:
      def __init__(self, name):
          self.name = name
      def speak(self):
          print(f"{self.name} is speaking.")
class Dog(Animal):
    pass
d = Dog("Rex")
d.speak()
