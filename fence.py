# Author: Joseph Ryu
# Date: 
# 1.0 2024/5/17
# 1.5 2024/5/22



# The program keeps getting looped in a while True loop
while True:
    print("---------")
    try:
        width = int(input("Width > "))
        length = int(input("Length > "))
        m_cost = int(input("Cost/m > "))
        # all values are integers to be added properly

        if width > 0 and length > 0:
            perimeter = width + length
            perimeter += perimeter
            cost = perimeter*m_cost
            # Final print of the cost and perimeter
            print(f"Perimeter: {perimeter} m")
            print(f"Cost: ${cost}")

            input("Again <enter> >")
            pass
        else:
            #If value is 0 or under
            print("Please enter a valid value")
            break
    except ValueError:
        #if value is not an integer
        print("Error")

    