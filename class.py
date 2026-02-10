class cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

color_one = cookie("green")
color_two = cookie("red")

print("the color of cookie is: ",color_one.get_color())


#pointers 
dict1 = {
    'value' : 1
}

dict2 = dict1 

print("the result before value")
print("the value of dict1:", dict1)
print("the value of dict2:", dict2)

print("the id of dict1:", id(dict1))
print("the id of dict2:", id(dict2))

dict2['value'] = 22
print("the result after value")
print("the value of dict1:", dict1)
print("the value of dict2:", dict2)
print("the id of dict1:", id(dict1))
print("the id of dict2:", id(dict2))