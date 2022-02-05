class Robot:
    def introduce_self(self):
        print("My name is " + self.name) #self is like this in Java

#objects and attributes
r1 = Robot()
r1.name = "Johnny"
r1.color = "black"
r1.weight = 30

r2 = Robot()
r2.name = "Brian"
r2.color = "brown"
r2.weight = 60

#runes r1 object in function introduce_self
r1.introduce_self()
r2.introduce_self()