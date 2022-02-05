class Robot:
    #constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"My name is " + self.name + "\nMy color is " + self.color + "\nMy weight is " + self.weight) #self is like this in Java

#objects and attributes when used without contstructor
# r1 = Robot()
# r1.name = "Johnny"
# r1.color = "black"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Brian"
# r2.color = "brown"
# r2.weight = 60

#objects and attributes when used with contstructor
r1 = Robot("Johnny", "black", "30")
r2 = Robot("Brian", "brown", "60")

#runs r1 and r2 object in function introduce_self
r1.introduce_self()
r2.introduce_self()