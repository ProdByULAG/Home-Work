name = "Daniar"
age = 21




def function(func): # Call Back
    a = func()
    return a

def function2():
    return "LOL"


a = function
print(a(function2))

print(function(function2))


