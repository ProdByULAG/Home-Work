class human:

    class_name = 'homo sapiens'


    def __init__(self, name, gender, race, height, weight):
        self.name = name
        self.gender = gender
        self.race = race
        self.height = height
        self.weight = weight




human1 = human(name='Daniar', gender='Male', race='Asian', height=1.80, weight=52)
human2 = human(name='Aman', gender='Male', race='Asian', height=1.70, weight=66)
print(human1.class_name,human1.name, human1.height, human1.weight, human1.gender, human1.race)
print(human2.class_name,human1.name, human2.height, human2.weight, human2.gender, human2.race)

