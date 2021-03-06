#!/usr/bin/env python3
#coding:utf-8

# Script name: codec
# Description: programme avec Clé de chiffrement matricielle
# Made by: Ezeqielle & Batmine3
# Begin: 14/12/2019
# End: 

# /!\ ne pas oublier d'enlever les print() de debug a la fin /!\
#Add creation de matrice
import os
import binascii

#matrix encode
def matrixEncodeSize(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    matrixSize = len(key)
    return matrixSize

def matrixEncode(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    return key

#matrix decode
def matrixDecode(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    print(workKey)
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    matrixSize = len(key)
    print(matrixSize)
    matrixID(matrixSize)

#file_encode
def fileEncode(fileUsed, matrixSize, key):
    fileOpen = open("file_encode/"+fileUsed, "rb")  #ouverture du fichier
    workFile = fileOpen.read()                      #passage des data dans une variable
    contenerFile = list(workFile)                   #conversion en list
    bits = map(bytes, contenerFile)                 #conversion en bytes

    fileExtension = fileUsed.split(".")             #recuperation de l'extension
    fileExtension = fileExtension[1]                #
    workFileLength = len(workFile)
    fileOpen.close()
    bits = []
    for i in range(workFileLength):
        contenerFile[i] = bin(contenerFile[i])
        bits = bits + list(contenerFile[i])
    
    
    deleteBinary(bits)
    
    size = len(bits)
    
    ourDict = {}
    iteration = size / matrixSize

    if iteration > round(iteration):
        iteration = round(iteration) + 1
    else:
        iteration = round(iteration)
    
    for i in range( int(iteration) ):
        ourDict["X" + str(i)] = getValues( size, matrixSize, i, bits) # 3 4 {0, 1, 2}


    fileOpen = open("file_encode/"+fileUsed+"c", "w+")
    fileContent = ""
    for x in ourDict:
        for value in ourDict[x]:
            for result in value:
                for matrix in key:
                    for multiplier in matrix:
                        fileContentTmp = fileContent + str(int(multiplier) ^ int(result))
    fileContent = ""
    lenght = len(fileContentTmp)

    while 0 <= lenght - 1:
        convert = ""
        j = 0
        for j in range(4):
            if lenght + j < lenght:
                convert = convert + str(fileContentTmp[lenght - j])

        fileContent = fileContent + str(binascii.a2b_uu(convert))
        lenght = lenght - j
    
    print(fileContent)
    fileOpen.write(fileContent)
    fileOpen.close()

#decouper le fichier par segment binaire de taille Gx trouver au dessus
#compter la taille de la liste pour la longueur de la boucle


def deleteBinary(bits):                                             #fonction pour supprimer les identifiants binaires ('0b')
    i = 0
    size = len(bits)
    while i + 1 < size:
        delete = "" + str(bits[i]) + str(bits[i + 1])
        if delete == '0b':
            bits.pop(i)
            bits.pop(i)
            size -= 2
        else:
            i += 1

def getValues(size, matrixSize, endValue, contenerFile):                      
    if endValue != 0:
        startValue = endValue * matrixSize
        endValue = matrixSize * (endValue + 1)
    elif endValue == 0:
        startValue = 0
        endValue = matrixSize                                                           
    result = ""
    while (startValue < endValue and startValue < size):
        if result == "":
            result = result + "" + str(contenerFile[startValue])
        else:
            result = result + str(contenerFile[startValue])
        startValue += 1
    return result



#file_decode
def fileDecode(fileUsed):
    fileOpen = open("file_decode/"+fileUsed, "rb")
    workFile = fileOpen.read()
    fileExtension = fileUsed.split(".")
    fileExtension = fileExtension[1]
    print(fileExtension)
    
#matrix ID
def matrixID(matrixSize):
    print(" Entrez la cle d'encodage de la matrice : ")
    c = 0
    i = 0
    encodeKey = [0] * matrixSize
    while (i < matrixSize):
        c += 1
        G = input("column "+str(c)+" : ")
        encodeKey[i] = G
        i += 1
    print(encodeKey)
#recuperation de la matrice identitee

#matrix calculation
def matrixMul():
    ""

#key creation
def keyCreation():
    ""

q = 0
while (q == 0):
    x = input(" Select you option : \n 1 - Encode file \n 2 - Decode file \n 3 - Create matrix \n 4 - Quit \n\n Your option : ")
    if (x == "1"):
        print("\n encode file : \n")
        matrix = input(" Entrez le nom de la matrice a selectionner : ")
        matrixKey = matrixEncode(matrix)
        matrixSize = matrixEncodeSize(matrix)
        file = input(" Entrez le nom du fichier avec son extension: ")
        fileEncode(file, matrixSize, matrixKey)
    elif (x == "2"):
        print("\n decode files : \n")
        matrix = input(" Entrez le nom de la matrice a selectionner : ")
        matrixDecode(matrix)
        file = input(" Entrez le nom du fichier avec son extension: ")
        fileDecode(file)
    elif (x == "3"):
        print("\n creation matrix : \n")
    elif (x == "4"): 
        a = input(" Are you sure want exit ? (y/n) : ")
        if(a == "y" or a == "Y" or a == "yes" or a == "Yes" or a == "YES"):
            q = 1
        else:
            q = 0
    else:
        print(" invalid choice")