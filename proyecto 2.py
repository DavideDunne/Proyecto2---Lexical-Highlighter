#Raúl Antonio Castillejos Santillán A01174919
#Davide Dunne Sanchez A01642355

import re

entero = re.compile("int\b") #match int keywords
string = re.compile("string\b") #match string keywords
igualacion = re.compile("={2}\b") #match equal sign
asignacion = re.compile("={1}\b")
comentario = re.compile("\/{2}") #match double slash
terminador = re.compile(";") #match semicolon
brackets = re.compile("{|}") #match either curly braces
variable = re.compile("[a-z]+") #match character strings
parenthesis = re.compile("^\(.{0,}\)$") #Match strings that are inside of a parenthesis
square_brackets = re.compile("^\[.{0,}\]$") #match strings that are inside single square brackets
macro = re.compile("^#\w{1,}$") #match macros (ex. #include, #define, #ifndef)

archivo = open("texto.txt","r")
palabra = "int x string a hola()"
open('file.html', 'w').close()
final = open("file.html", "a")

cont = 0
lineas= {}
for i in archivo:
    lineas[cont] = i
    cont += 1

for i in range(len(lineas)):    
    lineas[i] = lineas[i].split(" ")
    
for i in range(len(lineas)):
    print(lineas[i])
    
linea = {}
    
for j in range(len(lineas)):
    linea = lineas[j]
    for i in range(len(linea)):
        if(entero.search(linea[i])):
            print('<font color="blue">int</font>')
        if(string.search(linea[i])):
            print('<font color = "red"> string </font> ')
        if(igualacion.search(linea[i])):
            print('<font color = "purple"> == </font> ')
        if(asignacion.search(linea[i])):
            print('<font color = "grey"> = </font> ')
        if(comentario.search(linea[i])):
            print('<font color = "green"> // </font> ')
        if(terminador.search(linea[i])):
            print('<font color = "red"> ; </font> ')
        if(brackets.search(linea[i])):
            print('<font color = ""> { } </font> ')
        if(variable.search(linea[i])):
            m = variable.search(linea[i])
            print(m.group())
            print('<font color = ""></font> ')
            
            
