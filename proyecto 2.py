import re






entero = re.compile("int")
string = re.compile("string")
igualacion = re.compile("={2}")
asignacion = re.compile("={1}")
comentario = re.compile("\/{2}")
terminador = re.compile(";")
brackets = re.compile("{|}")
variable = re.compile("[a-z]+")

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
            
            