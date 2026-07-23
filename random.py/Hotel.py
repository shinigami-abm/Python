class Hotel:

      def set_name(self, name):
          self.__name = name

      def set_stars(self, s):
          if s < 6 and s > 0:
             self.__stars = s 
             print(f"There is now {self.get_stars()} stars.")
          else:
              print("There is no Hotel has more than 5 stars or less than 1.")

      def get_name(self):
          return self.__name

      def get_stars(self):  
          return self.__stars

      def __init__(self, name, stars):
          self.set_name(name)
          self.set_stars(stars)
          self.__rooms = []

      def add_star(self):
          if self.get_stars() < 5:
             self.set_stars(self.get_stars() + 1)
          else:
              print(f"{self.get_name()} has the limit of stars 5.")

      def count_rooms(self):
          return len(self.__rooms)

      def add_room(self):
          try:
             r = Hotel.room(self.count_rooms() + 1 ,float(input("Give me the price of the room.\n")))
          except:
             print("Please!!!, enter a price not a string !!!")   
             return 
          self.__rooms.append(r)

      def search_room(self, n):
          if len(self.__rooms) >= n:
                 return True
          else:
              return False
      def Book_room(self):
          try:
              r = int(input("Give me the number of the room that you want to book.\n"))
              if self.search_room(r) == True and self.__rooms[r-1].stat() != True:
                 print(f"You have to pay {self.__rooms[r-1].get_price()}") 
                 self.__rooms[r-1].Book()
              elif self.search_room(r) == False:
                  print("This room does not exist.")
              else: 
                  print("This room is booked.")
          except:
              print("Please, give an number not a string")

      def Un_book_room(self):
          try:
              r = int(input("Give me the number.\n"))
              if self.search_room(r) == True:
                 self.__rooms[r-1].unBook()
                 print("I hope you got a great night")
              else:
                  print("This room does not excest.")
          except:
              print("OMG!!!!!!!!!!")

      def remove_room(self):
          try:
             r = int(input("Give me the number of the room.\n")) 
             if self.search_room(r) == True:
                temp = self.__rooms[r-1] 
                self.__rooms.remove(temp)
             else:
                 print("This room does no exist.")
          except:
                print("Please !!, put a number!!!!!!!.")   
      
      def Toatl(self):
          T = 0
          for i in self.__rooms:
              if i.stat() == True:
                  T += i.get_price()
          print(f"The total is {T}.")        
 
      class room:
            def set_number(self, n):
                self.__number = n
            def set_price(self, p):
                if p >= 0:
                   self.__price = p
                else:
                    print("There is no negiteve price!")
            def get_price(self):
                return self.__price
            def get_number(self):
                return self.__number
            def __init__(self, n, p):
                self.set_number(n)
                self.set_price(p)
                self.__booked = False
            def Book(self):
                self.__booked = True
            def unBook(self):
                self.__booked = False
            def stat(self):
                return self.__booked
            def __repr__(self):
                return f"price = {self.get_price()}, number = {self.get_number()}\n"
def menu(h):
    print(f"Welcom in {h.get_name()} Hotel.")
    print("========== MENU ==========")
    print("1-add star.")
    print("2-count rooms.")
    print("3-add room.")
    print("4-remove room.")         
    print("5-Book room.")
    print("6-Un book room.")      
    print("7-Get the total.")
    print("99- Exit\n==========================")
    ctrl = True
    while ctrl == True:
          try:
              c= int(input("\nGive me your choose.\n"))
              if c == 1:
                 h.add_star()
              elif c == 2:
                   print(f"There is {h.count_rooms()} Rooms.")            
              elif c == 3:
                   h.add_room()
              elif c == 4:
                   h.remove_room()
              elif c == 5:
                   h.Book_room()
              elif c == 6:
                   h.Un_book_room()
              elif c == 7:
                   h.Toatl()
              elif c == 99:
                   ctrl = False
                   print("Thank you, Have a great day.")
          except:
              print("Please be real.")
H = Hotel("Djawhara", 4) 
menu(H)
