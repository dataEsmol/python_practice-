#Contador immobiliario 

# fase 1
passes = 0 # N passes
failures = 0 # N failures 



# fase 2
for student in range(10):
    result = int(input("input the next exam result"))
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

        
# fase 3
print(f"Number of fasses {passes}, Number of failures {failures}")

if passes >= 8:
    print("\Bonus to instructor")