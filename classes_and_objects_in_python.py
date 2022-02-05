class Robot:
    def introduce_self(self):
        print("My name is " + self.name) #self is like this in Java

#objects and attributes
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

#runes r1 object in function introduce_self
r1.introduce_self()