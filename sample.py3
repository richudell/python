import math

def volume(rad):
    vol = (4/3)*math.pi*(rad**3)
    return vol

def in_range(x,y,z):
    for num in range (x,y):
        if z == num:
            return True
    return False

def Char_Upper_Lower(sentence):
    upper = 0
    lower = 0
    for char in sentence:
        if char == char.lower():
            lower+=1
        elif char == char.upper():
            upper+=1
    return str(lower) + ' lower and ' + str(upper) + ' upper'

def Unique_Numbers(x):
    unique = tuple(x)
    list_of_unique = []
    for num in unique:
        if num not in list_of_unique:
            list_of_unique.append(num)
    return len(list_of_unique)

def Multiplication(x):
    y=1
    for num in x:
        y*=num
    return y

def Palindrome(word):
    revword = word[::-1]
    if revword == word:
        return True
    else:
        return False

def Pangram(sentence):
    unique = set()
    for letter in sentence:
        unique.add(letter.lower())
    print (unique)
    if unique >= {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}:
        return True
    else:
        return False


print(volume(4))

print(in_range(2,10,11))

print(Char_Upper_Lower('The quick brown fOx JumpS ovEr the LaZy doG.'))

a = (1,2,2,4,1,5,5,5,2)
print(Unique_Numbers(a))

b=[2,3,4,5,6,7,8,9]
print (Multiplication(b))

print(Palindrome('eyes'))

print(Pangram('The quick brown fox jumped over the lazy dogs'))