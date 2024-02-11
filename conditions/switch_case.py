def switch_case(argument):
  
    if argument=="a":
        print(f"you selected option : {argument}")
        return "Apple"
    elif argument=="b":
        return "Banana"
    elif argument=="c":
        return "Cherry"
    elif argument=="d":
        return "dates"
    else:
        print("Invalid option")
Input=input("Enter your value : ")
print(switch_case(Input))