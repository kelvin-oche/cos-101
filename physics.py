formulas = [
    r"F = ma",
    r"KE = \frac{1}{2}mv^2",
    r"PE = mgh",
    r"V = IR",
    r"v = \frac{d}{t}"
]

#F = ma
#KE = 1/2mv^2
#PE = mgh
#V = IR
#v = d/t


def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    print("Force =", mass * acceleration, "N")


def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    print("Kinetic Energy =", 0.5 * mass * velocity ** 2, "J")


def potential_energy():
    mass = float(input("Enter mass (kg): "))
    gravity = 9.8
    height = float(input("Enter height (m): "))
    print("Potential Energy =", mass * gravity * height, "J")


def voltage():
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ω): "))
    print("Voltage =", current * resistance, "V")


def velocity():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    print("Velocity =", distance / time, "m/s")


# Main program
while True:
    print("\nPHYSICS CALCULATOR")
    print("1. Force (F = ma)")
    print("2. Kinetic Energy (KE = ½mv²)")
    print("3. Potential Energy (PE = mgh)")
    print("4. Voltage (V = IR)")
    print("5. Velocity (v = d/t)")

    choice = input("\nChoose an operation (1-5): ")

    if choice == "1":
        force()
    elif choice == "2":
        kinetic_energy()
    elif choice == "3":
        potential_energy()
    elif choice == "4":
        voltage()
    elif choice == "5":
        velocity()
    else:
        print("Invalid choice!")

    continue_program = input(
        "\nWould you like to perform another calculation? (yes/no): "
    ).lower()

    if continue_program != "yes":
        print("Thank you for using the Physics Calculator!")
        break
