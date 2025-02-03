#1 Ejercicio#


#L = ["Tablero", "Hierro", "Uruguay", "Nube", "Ronaldo", "Roberto", "Uruguay"]

#m = 0

#while m != 6:
    
    #r = L[m]

    ####print(r, end = ", ")

    #m += 1

    #t = L[m:]

    #s = list(t)

    ####print(s, end = ", ")

    #for x in s:
        #if r == x:
            #print("Sí hay elementos repetidos")
        
####################################################



#2 ejercicio


#N = ["radar", "Flor", "Rafael", "Montaña"]
#for palabra in N:
    #t = list(palabra)
    #r = t[::-1]
    #if t == r:
        #print("La siguiente palabra en la lista es palíndrome: ","".join(t))
        #break   
#else:
    #print("No existe")
    
####################################################



#3 ejercicio

L = ["Matemáticas", "sol", "ONU", "Bonn", "fly"]

v = "aeiouAEIOUáéíóúÁÉÍÓÚ"

c = len(L)


n = 0

while n < c:

    y = L[n]
    p = 0
    for letra in y:
        for t in v:
            while letra == t and p < 2:
                p += 1
                if p >= 2:
                    print("Esta palabra tiene dos o más vocales: ", y)
                break
                
    n += 1

#####################################################



#4 ejercicio

#l = [1, 5, 3, 1, 4, 2]

#i = 0

#n = len(l)

#while i < n:

    #p = l[i]

    #r = l[n - 1 - i]

    #i += 1

    #if p == r:
        #print("La cadena es palíndrome")
        #break
#else:
    #print("La cadena no es palíndrome")
        






    
                
        
                
                











        

    
 




    

    
    
        
    
        