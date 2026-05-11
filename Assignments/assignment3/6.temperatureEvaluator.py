# 6. Create a nested if/elif structure to evaluate a temperature reading: print “Cold” if below 10, “Cool” if 10–20, “Warm” if 21–30, and “Hot” if above 30. If the value is outside a realistic range (below -50 or above 60), print “Sensor error”.


temperature = float(input("Enter the temperature : "))

if temperature < -50 or temperature > 60:
    print("Sensor error")
else:
    if temperature < 10:
        print("Cold")
    elif 10 <= temperature <= 20:
        print("Cool")
    elif 21 <= temperature <= 30:
        print("Warm")
    else:  
        print("Hot")
