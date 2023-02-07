import pyfiglet

score = []
currentvalue = 0

print("")
print(pyfiglet.figlet_format("Welcome To The Quiz!", justify="center" ,width=110))
print(pyfiglet.figlet_format("Created By Shinjan", justify="center" ,width=110))

print("")
user_input = input("Do You Want To Play This Quiz Game? : ")

user_input = user_input.lower()

if "yes" in user_input or "yep" in user_input or "yeah" in user_input:

# ---------------------------------------------------------------------

    print("")
    print("1. What does CPU stand for?")
    print("")
    ans = input("Ans:- ")
    ans = ans.lower().strip()
    
    if ans == "central processing unit":
        print("")
        score.append(f"True - {ans.title()}")
        currentvalue = currentvalue + 1
    
    else:
        print("")
        score.append(f"False - Correct Answer - Central Processing Unit - Your Answer - {ans.title()}")

# -----------------------------------------------------------------------

    print("2. What does GPU stand for?")
    print("")
    ans = input("Ans:- ")
    ans = ans.lower().strip()
    
    if ans == "graphics processing unit":
        print("")
        score.append(f"True - {ans.title()}")
        currentvalue = currentvalue + 1
    
    else:
        print("")
        score.append(f"False - Correct Answer - Graphics Processing Unit - Your Answer - {ans.title()}")

# -------------------------------------------------------------------------

    print("3. What does RAM stand for?")
    print("")
    ans = input("Ans:- ")
    ans = ans.lower().strip()
    
    if ans == "random access memory":
        print("")
        score.append(f"True - {ans.title()}")
        currentvalue = currentvalue + 1
    
    else:
        print("")
        score.append(f"False - Correct Answer - Random Access Memory - Your Answer - {ans.title()}")

# ---------------------------------------------------------------------------

    print("4. What does PSU stand for?")
    print("")
    ans = input("Ans:- ")
    ans = ans.lower().strip()
    
    if ans == "power supply":
        print("")
        score.append(f"True - {ans.title()}")
        currentvalue = currentvalue + 1
    
    else:
        print("")
        score.append(f"False - Correct Answer - Power Supply - Your Answer - {ans.title()}")

# ---------------------------------------------------------------------------

    print("5. What does BTW stand for?")
    print("")
    ans = input("Ans:- ")
    ans = ans.lower().strip()
    
    if ans == "by the way":
        print("")
        score.append(f"True - {ans.title()}")
        currentvalue = currentvalue + 1
    
    else:
        print("")
        score.append(f"False - Correct Answer - By The Way - Your Answer - {ans.title()}")

# ---------------------------------------------------------------------------

    print("-------------------------------------------------- Results --------------------------------------------------")

    for index, items in enumerate(score):
        index = index + 1
        print("")
        print(f"{index}. {items}")
        print("")
    value = currentvalue/5*100
    
    print("")
    print(f"Your Accuracy: {float(value)}%")
    print("")
    print("-------------------------------------------------------------------------------------------------------------")
    print("")

# ---------------------------------------------------------------------------

else:
    print("")
    exit()
