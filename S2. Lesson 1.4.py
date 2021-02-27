class dog:
    def make_noise(self, times):
        return "bark" * times

class Cat:

    def make_noise(self, times):
        return "meow" * times


def noise(noise_maker,times):
    print(noise_maker(times))

def create_class(cls):
    return cls

animal = Cat()

noise(animal.make_noise, 3)