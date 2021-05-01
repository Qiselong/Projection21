#Importations
from PIL import Image
import numpy as np 
## font used: BP Dots UnicaseSquare-Bold
# this code print every character in an image; only in order to test the associated matrix of each character.

# L = [ [], [], [], [], []]
# Li correspond to the matrix to generate the form of the character i. it's done using font_generate. 
def font_generate(L, data): #i got bored lol
    '''
    L: a list of exactly 5 list that may be empty.
    works for a 7x(7n) image
    each sub list of L, for instance L[i] correspond to the index to whiten at the i-th line.
    '''
    for i in range(0, 5):
        for j in L[i]:
            data[i+1, j] = [255,255,255]
    return data

## 1
l, h = 7,7

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L1 = [ [1,2,3], [3], [3], [3], [1,2,3,4,5]]
data = font_generate(L1, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/1.png')


## 2

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]


L2 = [ [2,3,4], [1,5], [3,4], [2], [1,2,3,4,5]]
data = font_generate(L2, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/2.png')

## 3

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]


L3 = [ [1,2,3,4], [5], [2,3,4], [5], [1,2,3,4]]
data = font_generate(L3, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/3.png')

## 4

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]



L4 = [ [4], [3,4] , [2,4], [1,2,3,4,5], [4] ]

data = font_generate(L4, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/4.png')


## 5
# L = [ [], [], [], [], []]

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L5 = [ [1,2,3,4,5], [1], [1,2,3,4], [5], [1,2,3,4]]

data = font_generate(L5, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/5.png')

## 6
# L = [ [], [], [], [], []]

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L6 = [ [2,3,4], [1], [1,2,3,4], [1,5], [2,3,4]]

data = font_generate(L6, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/6.png')


## 7
# L = [ [], [], [], [], []]

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L7 = [ [1,2,3,4,5], [5], [4], [3], [2]]

data = font_generate(L7, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/7.png')

## 8
# L = [ [], [], [], [], []]

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L8 = [ [2,3,4], [1,5], [2,3,4], [1,5], [2,3,4]]

data = font_generate(L8, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/8.png')

## 9
# L = [ [], [], [], [], []]

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L9 = [ [2,3,4], [1,5], [2,3,4,5], [5], [2,3,4]]

data = font_generate(L9, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/9.png')

## 0
# L = [ [], [], [], [], []]

data = np.zeros((h, l, 3), dtype = np.uint8)

w = [255, 255,255]

L0 = [ [2,3,4], [1,4,5], [1,3,5], [1,2,5], [2,3,4]]

data = font_generate(L0, data)

img = Image.fromarray(data, 'RGB')
img.save('images/fonts/0.png')


## Concatenation
#
#now we want to be able to concatenate two matrix Li. We will try for instance to print 10.

def concatenate_font(L):
    '''
    L: list on matrix Li.
    uses the content of the matrix Li to return a big List corresponding to the suite of characters.
    '''
    

    Lt = L[0]

    for i in range(1,len(L)): #character loop
        for k in range(5): #line loop
            for pos in L[i][k]:
                Lt[k].append(pos+7*i) #ndlr: L[i][k] corresponds to list of pixel to whiten. *7*i allows to space the things properly

    return Lt

#print(concatenate_font([L0, L0]))


L1 = [ [1,2,3], [3], [3], [3], [1,2,3,4,5] ]


## Recognition
## now we give a number (as a str) and we put it in an image.

def recognition(num): #IS OK \/
    L0 = [ [2,3,4], [1,4,5], [1,3,5], [1,2,5], [2,3,4] ]
    L1 = [ [1,2,3], [3], [3], [3], [1,2,3,4,5] ]
    L2 = [ [2,3,4], [1,5], [3,4], [2], [1,2,3,4,5] ]
    L3 = [ [1,2,3,4], [5], [2,3,4], [5], [1,2,3,4] ]
    L4 = [ [4], [3,4] , [2,4], [1,2,3,4,5], [4] ]
    L5 = [ [1,2,3,4,5], [1], [1,2,3,4], [5], [1,2,3,4] ]
    L6 = [ [2,3,4], [1], [1,2,3,4], [1,5], [2,3,4] ]
    L7 = [ [1,2,3,4,5], [5], [4], [3], [2] ]
    L8 = [ [2,3,4], [1,5], [2,3,4], [1,5], [2,3,4] ]
    L9 = [ [2,3,4], [1,5], [2,3,4,5], [5], [2,3,4] ]

    L = []
    for e in num:
        if e == '0':
            L.append(L0)
        if e == '1':
            L.append(L1)
        if e == '2':
            L.append(L2)
        if e == '3':
            L.append(L3)
        if e == '4':
            L.append(L4)
        if e == '5':
            L.append(L5)
        if e == '6':
            L.append(L6)
        if e == '7':
            L.append(L7)
        if e == '8':
            L.append(L8)
        if e == '9':
            L.append(L9)
    return L


def num_to_png(num):
    L11 = recognition(num)
    data = np.zeros((7,7,3), dtype = np.uint8)
    data = font_generate(L11[0], data)
    for i in range(1,len(L11)):  #pour chaque caractère
        datatmp = np.zeros((7,7,3), dtype = np.uint8)
        datatmp = font_generate(L11[i], datatmp)
        data = np.concatenate((data, datatmp), axis=1)
    img = Image.fromarray(data, 'RGB')
    img.save('images/fonts/'+num+'.png')

#L11c = concatenate_font(L11)
#print(L11c)
#dataL11C = np.zeros((7,7*len(L11c),3), dtype = np.uint8)
#print(dataL11C)

#dataL11C = font_generate(L11c, dataL11C)
#img = Image.fromarray(dataL11C, 'RGB')
#img.save('images/fonts/TEST.png')

#print(len(L11))
#L12 = concatenate_font([L0, L0])
#print(concatenate_font(L12))
#print(len(L11))
#print(L11[1] == L1)
#print(concatenate_font(L11))
#num_to_png('8758208602097')

num_to_png('69420')

#L11 est donc une liste de liste de char sous forme font.





