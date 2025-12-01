print(" Select a Physics formula")
print("A. speed ( v = d/t)")
print("B. Force ( F = m * a)")
print("C. Pressure ( P = F / A)")
print("D. ohm's Law ( V = I * R)")
print("E. Work ( w = f * d)")

user_choice = input("Enter a letter A-E ").upper()

if user_choice == "A":
    distance = float(input("Enter distance (in meters): "))
    time = float(input("Enter time (in seconds): "))
    if time == 0:
        print("time cannot be zero")
    else: 
        speed = distance / time
        print("Speed =", speed, "m/s")
        
elif user_choice == "B":
    mass = float(input("Enter mass in Kg"))
    accel = float(input("Enter acceleration (in m/s²): "))
    force = mass * accel 
    print ("Force =", force, "N")
    
elif user_choice == "C":
    force = float(input("Enter force (in N): "))
    area = float(input("Enter area (in m²): "))
    if area == 0:
        print("Area cannot be zero.")
    else:
        pressure = force / area 
        print("Pressure =", pressure, "Pa")
elif user_choice == "D":
    force =  float(input("Enter force (in N): "))
    distance = float(input("Enter distance (in meters): "))
    work = force * distance
    print("Work =", work, "J")

elif user_choice == "E":
    current = float (input("Enter current  (in A): "))
    resistance = float (input("Enter resistance (in Ω): "))
    voltage  = current * resistance 
    print ("voltage =", voltage, "V")
    
else:
    print("Invalid choice. Please Choose from A to E.")
        