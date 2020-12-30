class G:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am in MCA. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("MASTER")


class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am in bteq. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("BACHELOR")


G1 = G("ayushi", 21)
B1 = B("radhi", 20)

for poly in (G1, B1):
    poly.make_sound()
    poly.info()
    poly.make_sound()