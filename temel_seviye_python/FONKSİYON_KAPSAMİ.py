#global scope
x = 0

def fonk ():
    #local scope
    x = 1
    return x

# print(fonk())1
# print:(x) 0

a = []
print("a'nın ilk değeri")

def degistirir():
    def degiştirir():
        a.append(1)

        degistir2()
        return a

print(degistir())
print("a'nın son değeri",a)