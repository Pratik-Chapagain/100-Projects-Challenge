#----------------------
# COMMAND-LINE UNIT CONVERTER
#----------------------

#--- Temperature Conversion Functions ---
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

#--- length conversion functions ---
def meter_to_kilometer(m):
    return m / 1000

def kilometer_to_meter(km):
    return km * 1000 

def meter_to_feet(m):
    return m * 3.28084

def feet_to_meter(ft):
    return ft / 3.28084


#---weight conversion functions ---
def kg_to_gram(kg):
    return kg * 1000

def gram_to_kg(g):
    return g / 1000    

def kg_to_pounds(kg):
    return kg * 2.20462  

def pounds_to_kg(lb):
    return lb / 2.20462  


def temperature_menu():
    print("\n🌡️ Temperature Conversion:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    choice = input("Choose option: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f} °F = {fahrenheit_to_celsius(f):.2f} °C")
    else:
        print("❌ Invalid choice!")

def length_menu():
    print("\n📏 Length Conversion:")
    print("1. Meter → Kilometer")
    print("2. Kilometer → Meter")
    print("3. Meter → Feet")
    print("4. Feet → Meter")
    choice = input("Choose option: ")

    if choice == "1":
        m = float(input("Enter Meters: "))
        print(f"{m} m = {meter_to_kilometer(m):.3f} km")
    elif choice == "2":
        km = float(input("Enter Kilometers: "))
        print(f"{km} km = {kilometer_to_meter(km):.2f} m")
    elif choice == "3":
        m = float(input("Enter Meters: "))
        print(f"{m} m = {meter_to_feet(m):.2f} ft")
    elif choice == "4":
        ft = float(input("Enter Feet: "))
        print(f"{ft} ft = {feet_to_meter(ft):.2f} m")
    else:
        print("❌ Invalid choice!")

def weight_menu():
    print("\n⚖️ Weight Conversion:")
    print("1. Kg → Gram")
    print("2. Gram → Kg")
    print("3. Kg → Pounds")
    print("4. Pounds → Kg")
    choice = input("Choose option: ")

    if choice == "1":
        kg = float(input("Enter Kg: "))
        print(f"{kg} kg = {kg_to_gram(kg):.2f} g")
    elif choice == "2":
        g = float(input("Enter Grams: "))
        print(f"{g} g = {gram_to_kg(g):.2f} kg")
    elif choice == "3":
        kg = float(input("Enter Kg: "))
        print(f"{kg} kg = {kg_to_pounds(kg):.2f} lbs")
    elif choice == "4":
        lb = float(input("Enter Pounds: "))
        print(f"{lb} lbs = {pounds_to_kg(lb):.2f} kg")
    else:
        print("❌ Invalid choice!")

# --- Main Menu ---
def main():
    while True:  # Loop until user chooses Exit
        print("\n===== UNIT CONVERTER =====")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Exit")
        choice = input("Choose a category: ")

        # Call the respective submenu based on choice
        if choice == "1":
            temperature_menu()
        elif choice == "2":
            length_menu()
        elif choice == "3":
            weight_menu()
        elif choice == "4":
            print("👋 Exiting Unit Converter. Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

        # Pause before showing menu again
        input("\nPress Enter to continue...")


    
# --- Entry point ---
if __name__ == "__main__":
    main()