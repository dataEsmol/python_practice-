# programa de promedio de clase


# fase 1

total = 0
counter = 0 

# fase 2

grade = int(input("introdusca el numero de la clese"))

while grade  != -1:
    total += grade 
    counter +=1 
    grade = int(input("introdusca el numero de la clese"))
    
if counter != 0:
    media = total/counter
    print(f'el promedio es {media}')
else :
    print("no an entrado calificaciónes")