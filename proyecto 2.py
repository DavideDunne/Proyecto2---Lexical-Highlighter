#Raúl Antonio Castillejos Santillán A01174919@tec.mx
#Davide Dunne Sanchez A01642355@tec.mx

import re

entero = re.compile("int") #match int keywords
string = re.compile("string") #match string keywords
si = re.compile("if") #match if keywords
igualacion = re.compile("={2}") #match doble equal sign
asignacion = re.compile("={1}") #match equal signs
comentario = re.compile("\/{2}") #match double slash
terminador = re.compile(";") #match semicolon
bracketStart = re.compile("{") #match start of curly braces
bracketEnd = re.compile("}") #match end of curly braces
variable = re.compile("[a-z]+") #match character strings
parenthesis = re.compile("^\(.*\)$") #Match strings that are inside of a parenthesis
comillas = re.compile("^\".*\"$") # match strings that are inside of a " "
square_brackets = re.compile("[a-z]+\[.{0,}\]$") #match strings that are inside single square brackets
cout = re.compile("<{2}") #matches the << symbols
number = re.compile("[0-9]+") #matches all numbers
macro = re.compile("^#\w+$") #match macros (ex. #include, #define, #ifndef)

archivo = open("texto.txt","r")
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


final.write('<html>\n<head>\n<tittle></tittle>\n</head>\n<body>\n')
for j in range(len(lineas)):
    linea = lineas[j]
    palabra=""
    
    for i in range(len(linea)):
        L = False
        if(entero.search(linea[i])):
            palabra += '<font color="blue">int </font> '
            L = 1
        if(string.search(linea[i])):
            palabra += '<font color = "red">string </font> '
            L= 1
        if(igualacion.match(linea[i])):
            palabra += '<font color = "purple">== </font> '
            L = 1
        elif(asignacion.match(linea[i])):
            m = asignacion.search(linea[i])
            palabra += '<font color = "pink">'+m.group()+'</font> '
            L= 1
        if(comentario.search(linea[i])):
            palabra += '<font color = "green">// </font> '
            L= 1
        if(terminador.search(linea[i])):
            palabra += '<font color = "red">; </font> '
            L= 1
        if(bracketStart.search(linea[i])):
            palabra += '<font color = "yellow">{ </font> '
            L= 1
        if(bracketEnd.search(linea[i])):
            palabra += '<font color = "yellow">} </font> '
            L= 1
        if(cout.search(linea[i])):
            palabra += '<font color = "74138C"><< </font> ' 
            L= 1
        if(si.search(linea[i])):
            palabra += '<font color = "DB9900">if </font> ' 
            L= 1
        if(parenthesis.search(linea[i])):
            m = parenthesis.search(linea[i])
            palabra += '<font color = "2DC800">'+m.group()+' </font> '
            L= 1
        if(square_brackets.search(linea[i])):
            m = square_brackets.search(linea[i])
            palabra += '<font color = "FF68DD">'+m.group()+' </font> '
            L= 1
        if(number.search(linea[i]) and L == 0):
            m = number.search(linea[i])
            palabra += '<font color = "B05F3C">'+m.group()+' </font> '
            L= 1
        if(comillas.search(linea[i])):
            m = comillas.search(linea[i])
            palabra += '<font color = "892EE4">'+m.group()+' </font> '
            L= 1
        if(L == 0):
            palabra += " "+linea[i]+" "
    palabra += '<br>'
    print(palabra)
    final.write(palabra)
        
final.write('\n</body>\n</html>') 
