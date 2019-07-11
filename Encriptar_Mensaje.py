import numpy as np
import math
import cv2

#Message to encrypt
message = input("Message: ")

#Image to encrypt in
image = input("Name of image: ")

#Channel
color = int(input("Channel: "))

#List that will store every value for each letter
code = []

#Codification matrix
codificationMatrix = np.array([[0,1,1],[1,0,1],[1,0,0]])

#Iterating letter by letter in the message
for letter in message:

    #Archive that has the values of each letter in the alphabet
    archive = open("codigo2.txt", "r")
    
    #Iterating each line in the archive
    for line in archive.readlines():
    
        #If a letter from the archive match with the current letter in the message
        if letter == line[0]:
            
            #Adding to the list the code for that letter
            code.append(int(line[1:4]))
            
    archive.close()
    
#Condition if the matrix is full 
if len(message) < 3*math.ceil(len(message)/3):
    #For each character that is missing, it fills with spaces
    for missing in range(3*math.ceil(len(message)/3)-len(message)):
        code.append(7)


#Storing the length of the message
lenMessage = len(code)     
print(lenMessage)

#Reshape and convert the list to a matrix of 3 x n dimensions
matrixMessage = np.array(code).reshape(math.ceil(len(message)/3),3)
matrixMessage = np.transpose(matrixMessage)



#Multiplying the codification matrix by the matrix that has the message 
codificatedMatrix = codificationMatrix.dot(matrixMessage)
m,n = codificatedMatrix.shape
print(codificatedMatrix)
#Convert to list to iterate it
matrixList = codificatedMatrix.tolist()

#Load an image
imageToEncrypt = cv2.imread(image, 1)

#Store the number of columns and color in the first pixel
imageToEncrypt[1,1,1] = n
imageToEncrypt[1,1,0] = color


PosX = 100
PosY = 100
pixel = [0,0,0]

 #Iterating the codificated matrix
for i in range(0,m):
     for j in range(0,n):
         #Assignment of the values to the Green pixel
         imageToEncrypt[PosX+20*i, PosY+20*j, color] = matrixList[i][j]
#Storing the image with the message already encrypted
cv2.imwrite("pruebaencriptada.png", imageToEncrypt)


        
        
        