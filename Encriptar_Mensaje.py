import numpy as np
import math
import cv2

#Message to encrypt
message = input("Message: ")

#Image to encrypt in
image = input("Name of image: ")

#List that will store every value for each letter
code = []

#Codification matrix
codificationMatrix = np.array([[3,0,2],[3,1,3],[1,1,2]])

#Iterating letter by letter in the message
for letter in message:

    #Archive that has the values of each letter in the alphabet
    archive = open("code.txt", "r")
    
    #Iterating each line in the archive
    for line in archive.readlines():
    
        #If a letter from the archive match with the current letter in the message
        if letter == line[0]:
            
            #Adding to the list the code for that letter
            code.append(int(line[1:3]))
            
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

print(matrixMessage)

#Multiplying the codification matrix by the matrix that has the message 
codificatedMatrix = codificationMatrix.dot(matrixMessage)

print(codificatedMatrix)
#Convert to list to iterate it
matrixList = codificatedMatrix.tolist()

#Load an image
imageToEncrypt = cv2.imread(image, 1)

#Store the length of the message in the first pixel
imageToEncrypt[1,1,0] = lenMessage

PosX = 461
PosY = 1965
y = PosY
pixel = [0,0,0]

#Iterating the codificated matrix
for i in range(len(matrixList)):
    pixel = [0,0,0]
    for j in range(len(matrixList[i])):
        #Assignment of the values to the RGB pixels respectively
        pixel[0] = math.floor(matrixList[i][j]/3)
        pixel[1] = math.floor(matrixList[i][j]/3)
        pixel[2] = math.floor(matrixList[i][j]/3)
        
        #If the sum is lower than the value in the codificated matrix
        if sum(pixel) < matrixList[i][j]:
            #Add the difference to the blue color
            pixel[2] = pixel[2] + (matrixList[i][j] - sum(pixel))
        #Assignment of the value to the positions X and Y 
        imageToEncrypt[PosX, PosY] = pixel
        PosY+=1
    PosX+=1
    PosY = y
 
#Storing the image with the message already encrypted
cv2.imwrite("pruebaencriptada.png", imageToEncrypt)


        
        
        