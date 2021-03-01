class complex:
    def __init__(self, first,second,):
        self.first = first
        self.second = second

    def __str__(self):
        return(self.first)+(self.second)

    def __add__(self, other):
        summ = self.first + other.second
        summ2 = self.second + other.first
        result = f"z1={other.first} z={other.second} {complex(summ//summ2)}"
        return result

    def __add__(self, otherminus):
        minus1 = self.first - otherminus.second
        minus2 = self.second - otherminus.first

        return complex(minus1//minus2)


    def multiply(self, othermultiply):
        multi1 = self.first * othermultiply.second
        multi2 = othermultiply.first * self.second
        multiresult = complex(multi1//multi2)

        return multiresult





x = complex(3, 7)
y = complex(1, 3)
plus1 = (x.first + x.second)
plus2 = (y.first + y.second)
minus1 = (x.first - x.second)
minus2 = (y.first - y.second)
multi1 = (x.first * x.second)
multi2 = (y.first * y.second)

print(plus1, plus2)
print(minus1, minus2)
print(multi1, multi2)


