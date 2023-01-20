import numpy as np

a = [[6 ,3 ,2],
     [2, 7, 3],
     [7, 5, 15]]

print(np.diag(a))
print(np.sum(np.abs(a), axis = 1))
print(np.sum(np.abs(a), axis = 1) - np.diag(a))

def checkDiagonallyDominant(a):
    diag = np.diag(a)
    sumWithDiagonal = np.sum(np.abs(a), axis = 1)
    sumWithoutDiagonal = sumWithDiagonal - diag
        
    if np.all(diag > sumWithoutDiagonal):
        print("True")
        return True
    else:
        print("False")
        return False
    
checkDiagonallyDominant(a)

a = 0
b = 0
c = 0
epsilon = 0.1
limit = 15

oldValue = np.array([a, b, c])

for i in range(1 , limit):
    a = (15 - 3 * b - 2 * c) / 6
    b = (6 - 2 * a - 3 * c) / 7
    c = (12 - 7 * a - 5 * b) / 15
    newValue = np.array([a, b, c])

    distance = np.sqrt(np.dot(newValue - oldValue, newValue - oldValue))

    print(i, a, b, c)
    if distance < epsilon:
        print("Solution Found")
        isCompleted = True
        break

    oldValue = newValue

if isCompleted == False:
    print("No Solution")

CaseX = [
  [
    [-3,9,-6],
    [7,-2,-3],
    [4,1,-4]
  ],
  [
    [1, 3, -3, 9],
    [2, -9,3, -3],
    [-1, 3, 15, -1],
   [21, 4, -1, 10]
  ],
  [
    [4,2,-1],
    [1,3,-1],
    [5,2,10]
  ],
  [
    [-7,2,-4],
    [-1,-19,-13],
    [-3,3,-19]
  ],
  [
    [-12, 1, -4, 6],
    [-3, 8,-3, 2],
    [3, 3, 10, -3],
    [3, -2, 3, 12]
  ],
  [
    [2,1,-1],
    [-2,5,-3],
    [-1,-6,-9]
  ]
]
CaseY=[
       [0, -6, 5],
       [12, 9, -6, 11],
       [19, 12, 5],
       [8, 3, 5],
       [3, 6, 9, 21],
       [3, 9, 12]
    ]

def gaussSeidel(x, y, epsilon, limit):
    x = np.array(x)
    y = np.array(y)

    diag = np.diag(x)
    sumWithDiagonal = np.sum(np.abs(x), axis = 1)
    sumWithoutDiagonal = sumWithDiagonal = diag
    if np.all(diag > sumWithoutDiagonal):
        print("False")
        return False
    
    print(x.shape[0])
    oldValue = np.zeros(x.shape[0])

    diagonal = np.diag(x)
    x = -x
    np.fill_diagonal(x, 0)

    print(x)

    for i in range(1, limit):
        newValue = oldValue
        for j, row in enumerate(x):
            newValue[j] = (y[j] + np.dot(row, newValue)) / diagonal[j]
        
        distance = np.sqrt(np.dot(newValue - oldValue, newValue - oldValue))

        if distance < epsilon:
            print("True")
            return True
        oldValue = newValue
    
    return False

for i, (x, y) in enumerate(zip(CaseX, CaseY)):
    if gaussSeidel(x, y , 0.01, 15):
        print("Solution Found!")
    else:
        print("Solution Not Found!")

temp = [
    [-3, 9, -6],
    [7, -2, -3],
    [4, 1, -4]
]

temp = np.array(temp)
print(temp.shape[0])
np.fill_diagonal(temp, 0)
print(temp)