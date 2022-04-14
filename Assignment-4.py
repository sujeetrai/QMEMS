class trang:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.area = 0

class triangle(trang):
    def __init__(self, a, b, c):
        poly.__init__(self, a, b, c)

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = float((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5

    def get_area(self):
        return self.area     

a, b, c = input("a = "), input("b = "), input("c = ")

t = triangle(a, b, c)
t.calculate_area()
print("area : {}".format(t.get_area()))
a = 1
b = 2
c = 3
area : 0.0

def filterlongword(string,number):

    for i in range(len(string)):
        listwords = []
        if len(string[i]) > number:
            listwords.append(string[i])

        return listwords 


def main():
    words = input("Please input the list of words: ")
    integer = eval(input("Please input an integer: "))

    words1 = filterlongword(words,integer)

    print("The list of words greater than the integer is",words1)

main()  
Please input the list of words: sujeet
Please input an integer: 1
The list of words greater than the integer is []

list_of_strings = ["5","6","7","8","9", "10"]

result = []

for string in list_of_strings:
    result.append(int(string))
    
print(result)
[5, 6, 7, 8, 9, 10]

def vowel(char):
    if char.lower() in 'aeiou':
        return True
    if char.upper() in 'AEIOU':
        return TRUE
    else:
        return False