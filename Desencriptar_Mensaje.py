import numpy as np
import cv2
import math
PosX = 461
PosY = 1965

#Codification matrix
matrizCodificacion = np.array([[3,0,2],[3,1,3],[1,1,2]])

#Loading the image
image2 = cv2.imread("pruebaencriptada.png", 1)
codigoD = []

#Getting the length of the message
longitudMD = image2[1,1,0]

#Iterating in the positions where the message is
X = PosX
for X in range(X, X+3, 1):
    Y = PosY
    
    for Y in range(Y, Y+int(math.ceil(longitudMD)/3),1):   
        #Storing the values from the message in the list
        codigoD.append(sum(image2[X,Y]))
        
#The list is now a matrix 3 x n
matrizMensajeD = np.matrix(codigoD).reshape(3, int(math.ceil(longitudMD)/3))

#Inverse codification matrix
matrizInversa = np.linalg.inv(matrizCodificacion)

#Multiplying the inverse Matrix by the message to decrypt
matrizDecodificada = matrizInversa.dot(matrizMensajeD)
matrizDecodificada = np.transpose(matrizDecodificada)

#Convert to list to iterate it
matrizBusqueda = matrizDecodificada.tolist()

mensajeD = ""
cod = ""

#Iterating the list
for i in range(len(matrizBusqueda)):
    for j in range(len(matrizBusqueda[i])):
        #Opening the archive with the values of each letter
        archivo1 = open("code.txt", "r")
        #Reading each line 
        for codigo in archivo1.readlines():
            
            #Contatenation of the last characters (the values)
            cod = codigo[-3:-1]
            letra = int(cod)
            
            #If the value is the same than the value in the archive
            if round(matrizBusqueda[i][j]) == letra:
                
                #Contatenate the message decrypted
                mensajeD = mensajeD + codigo[0]
        archivo1.close()
        
#Print the message
print("The message is: ",mensajeD, "...")