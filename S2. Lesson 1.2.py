class Bird:

    def __init__(self, type, size, color):
        self.type = type
        self.size = size
        self.color = color

    def fly(self):
        if self.size > 100:
            print("can't fly")
        else:
            print("can fly")

    def give_eggs(self):
        return f"Eggs {self.type}"


for i in range(1, 1):
    bird_list = []
    type = input()
    size = input()
    color = input()
    Bird(type, size, color)
    bird_list.append(Bird)


bird = Bird(type='pigeon', size=20, color="white")
bird.fly()
eggs = bird.give_eggs()

bird2 = Bird(type='straus', size=200, color='dark')
bird2.fly()
eggs2= bird2.give_eggs()

print(eggs, eggs2)
