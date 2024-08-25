def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

def g_to_kg(g):
    return g / 1000

def kg_to_g(kg):
    return kg * 1000

def main():
    print("Unit Converter")
    print("1. Centimeters to Meters")
    print("2. Meters to Centimeters")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")
    
    choice = int(input("Enter your choice (1-4): "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value} cm is {cm_to_m(value)} meters.")
    elif choice == 2:
        print(f"{value} meters is {m_to_cm(value)} centimeters.")
    elif choice == 3:
        print(f"{value} grams is {g_to_kg(value)} kilograms.")
    elif choice == 4:
        print(f"{value} kilograms is {kg_to_g(value)} grams.")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
