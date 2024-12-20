# 1-D Kinematics Physics Equations Solver


# Defines All Variables Used In Program Before Usage
vf = float
vi = float
a = float
t = float
deltax = float 
equationtype = int
choice1 = bool
choice2 = bool
choice3 = bool
choice4 = bool
choice5 = bool



print("1-D Kinematics Problem Solver, Made By KDB")
print("Please Choose Which Variable You Lack Via Entering The Corresponding Number")
print("1. Final Velocity")
print("2. Initial Velocity")
print("3. Acceleration")
print("4. Time")
print("5. Displacement Of X")
equationtype = input("Type Here")

match equationtype:
    case "1":
        choice1 == True
    case "2":
        choice2 == True
    case "3":
        choice3 == True
    case "4":
        choice4 == True
    case "5":
        choice5 == True
    case _:
        print("please just input something brother man")
if choice1 == True:

