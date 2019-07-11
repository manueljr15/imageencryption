import numpy as np
import cv2
PosX = 100
PosY = 100

#Codification matrix
matrizCodificacion = np.array([[0,1,1],[1,0,1],[1,0,0]])

#Loading the image
image2 = cv2.imread("pruebaencriptada.png", 1)
codigoD = []

#Getting the number of columns of the message and the color where is stored
n = image2[1,1,1]
color = image2[1,1,0]

#Iterating in the positions where the message is
for i in range(0, 3):
    
    for j in range(0,n):   
        #Storing the values from the message in the list
        codigoD.append(image2[PosX+20*i,PosY+20*j,color])
        
#The list is now a matrix 3 x n
matrizMensajeD = np.matrix(codigoD).reshape(3,n)

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
for i in range(0,n):
    for j in range(0,3):
        #Opening the archive with the values of each letter
        archivo1 = open("codigo2.txt", "r")
        #Reading each line 
        for codigo in archivo1.readlines():
            
            #Contatenation of the last characters (the values)
            cod = codigo[-4:-1]
            letra = int(cod)
            #If the value is the same than the value in the archive
            if round(matrizBusqueda[i][j]) == letra:
                #Contatenate the message decrypted
                mensajeD = mensajeD + codigo[0]
        archivo1.close()
        
#Print the message
print("The message is: ",mensajeD, "...")