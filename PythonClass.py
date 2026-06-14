#class example
class Animal:
    def __init__(self, name):
            self.name = name
            
    def getAnimalName(self):
          print("Animal is", self.name)

# a=Animal("dog", "Barking ")
# a.sound()

#create a class and inherit from parent class
class Dog(Animal):
      def __init__(self,name, voice:any):
            super().__init__(name)
            self.voice=voice

      def sound(self):
            print("It is", self.voice)      

      def getPetname(self):
            print("Its pet name is", self.name)
                  

d=Dog("Dog","barking")
d.getAnimalName()
d.getPetname()
d.sound()


class cat(Animal):
      def __init__(self, name, description):
            super().__init__(name)  
            self.description=description


      def getFetures(self):
            print("Am ", self.name, self.description)

c=cat("Cat","I have bright eyes")
c.getFetures()
#Child class can also add its own features
class car:
      def __init__(self, name, model,engine ):
        self.name  =name
        self.model=model
        self.engine = engine

      def getCardetails(self):
            print("details of the car", self.name, self.model, self.engine)
      
c=car("honda","2000","CVT")
c.getCardetails()

class Honda(car):
      def __init__(self, name, model, engine, color):
            super().__init__(name, model, engine)
            self.color = color

      def getCarColor(self):
            print("Color of the car is", self.color)  

h=Honda("Honda", "2009", "Auto" ,"Red")
h.getCardetails( )
h.getCarColor()

class Bus:
      def __init__(self, Name, model, engine , numberofpassangersAllowed):
           self.Name=Name
           self.model = model
           self.engine=engine
           self.numberofpassangersAllowed = numberofpassangersAllowed

      def getBusDetails(self):
            print("Bus details are", self.Name, self.model,self.engine, self.numberofpassangersAllowed)


b=Bus("Volvo","2010","auto", 120)
b.getBusDetails(  )

#why use super 

#Method overriding in inheritance

#use different types of methods

#write different inheritance

#