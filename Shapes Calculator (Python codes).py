def continuation():
    WantToContinue = input("Do you want to continue (Y/N) : ").upper()
    if WantToContinue == "Y":
        print()
        main()

    elif WantToContinue == "N":
        print("exiting...")
        exit()

    else:
        print("Invalid input! Try again with a 'Y' or a 'N'\n")
        continuation()


def main():

    print("SHAPES CALCULATOR\n")

    print("1. Calculate Surface Area of a cone")
    print("2. Calculate Volume of a cone")
    print("3. Calculate Base Area of a cone")
    print("4. Calculate Volume of a rectangular pyramid")
    print("5. Calculate Surface Area of a rectangular pyramid")
    print("6. Exit\n")

    choice = int(input("Enter Your Preferred Option : "))
    
    if (choice == 1):

        radius, height, SurfaceArea, SlantHeight = 0.0, 0.0, 0.0, 0.0
        pi = 3.14
        WantToContinue = "Yes"

        while(WantToContinue == "Yes"):
            ValidRadiusInp = "Yes"
            ValidHeightInp = "Yes"

            # --- Get the Radius ---
            radius = float(input("\nEnter the radius of the base : "))
            print()
            if(radius<0):
                print("The radius value cannot be negative.")
                ValidRadiusInp = "No"
            if(radius==0.0):
                print("The radius value cannot be zero.")
                ValidRadiusInp = "No"


            # --- Get the height only if Radius value is valid ---

            if(ValidRadiusInp == "Yes"):
                height = float(input("Enter the height of the cone : "))
                print()
                if(height<0):   
                  print("The height value cannot be negative.")
                  ValidHeightInp = "No"
                if(height==0.0):
                  print("The height value cannot be zero.")
                  ValidHeightInp = "No"


            # --- Calculate the slanted height and surface area but display only the SurfaceArea only if the values are valid ---

            if(ValidRadiusInp == "Yes" and  ValidHeightInp == "Yes"):
               SlantHeight = (((radius*radius) + (height*height))**0.5)
               SurfaceArea = (pi*radius*radius) + (pi*radius*SlantHeight)
               
               # --- Display the Surface Area ---
               print("The Surface Area of the cone = ",format(SurfaceArea,'.2f'),"cm\u00B2""\n")
            else: 
                print("Could not calculate the Surface Area due to invalid inputs. Please try again with valid inputs.\n")

            continuation()
                
    elif (choice == 2):
        
        radius, height = 0.0, 0.0
        pi = 3.14
        WantToContinue = "Yes"

        while(WantToContinue == "Yes"):
            ValidRadiusInp = "Yes"
            ValidHeightInp = "Yes"


            # --- Get the Radius ---
            radius = float(input("\nEnter the radius of the base : "))
            print()
            if(radius<0):
                print("The radius value cannot be negative")
                ValidRadiusInp = "No"
            if(radius==0.0):
                print("The radius value cannot be zero")
                ValidRadiusInp = "No"


            # --- Get the Height only if Radius value is valid ---

            if(ValidRadiusInp == "Yes"):
                height = float(input("Enter the height of the cone : "))
                print()
                if(height<0):   
                  print("The height value cannot be negative")
                  ValidHeightInp = "No"
                if(height==0.0):
                  print("The height value cannot be zero")
                  ValidHeightInp = "No"


            # --- Calculate & display the volume only if the values are valid ---

            if(ValidRadiusInp == "Yes" and ValidHeightInp == "Yes"):
               Volume = 1/3*(pi*radius*radius)*height

               # --- Display the volume ---
               print("The volume of the cone = ",format(Volume,'.2f'),"cm\u00B3""\n")
            else:
                print("Could not calculate the volume due to invalid inputs. Please try again with valid inputs.\n")

            continuation()

    elif (choice == 3):
        
        radius = 0.0
        pi = 3.14
        WantToContinue = "Yes"

        while(WantToContinue == "Yes"):
            ValidRadiusInp = "Yes"


            # --- Get the Radius ---
            radius = float(input("\nEnter the radius of the base : "))
            print()
            if(radius<0):
                print("The radius value cannot be negative")
                ValidRadiusInp = "No"
            if(radius==0.0):
                print("The radius value cannot be zero")
                ValidRadiusInp = "No"


            # --- Calculate & display the Base Area only if the value is valid ---

            if(ValidRadiusInp == "Yes" ):
               BaseArea = pi*(radius*radius)

               # --- Display the Base Area ---
               print("The Base Area of the cone = ",format(BaseArea,'.2f'),"cm\u00B2""\n")
            else:
                print("Could not calculate the Base Area due to invalid inputs. Please try again with valid inputs.\n")

            continuation()

    elif (choice == 4):
        
        length, width, height = 0.0, 0.0, 0.0
        WantToContinue = "Yes"

        while(WantToContinue == "Yes"):
            ValidLengthInp = "Yes"
            ValidWidthInp = "Yes"
            ValidHeightInp = "Yes"


            # --- Get the base length ---
            length = float(input("\nEnter the base length of the rectangular pyramid : "))
            print()
            if(length<0):
                print("The base length value cannot be negative")
                ValidLengthInp = "No"
            if(length==0.0):
                print("The base length value cannot be zero")
                ValidLengthInp = "No"


            # --- Get the base width only if base length value is valid ---

            if(ValidLengthInp == "Yes"):
                width = float(input("Enter the base width of the rectangular pyramid : "))
                print()
                if(width<0):   
                  print("The base width value cannot be negative")
                  ValidWidthInp = "No"
                if(width==0.0):
                  print("The base width value cannot be zero")
                  ValidWidthInp = "No"


            # --- Get the Height only if base length and base width values are valid ---

            if(ValidLengthInp == "Yes" and ValidWidthInp == "Yes"):
                height = float(input("Enter the height of the rectangular pyramid : "))
                print()
                if(height<0):   
                  print("The height value cannot be negative")
                  ValidHeightInp = "No"
                if(height==0.0):
                  print("The height value cannot be zero")
                  ValidHeightInp = "No"


            # --- Calculate & display the volume only if the values are valid ---

            if(ValidLengthInp == "Yes" and ValidWidthInp == "Yes" and ValidHeightInp == "Yes"):
               Volume = (length*width*height)/3
               
               # --- Display the volume ---
               print("The volume of the rectangular pyramid = ",format(Volume,'.2f'),"cm\u00B3""\n")
            else:
                print("Could not calculate the volume due to invalid inputs. Please try again with valid inputs.\n")

            continuation()

    elif (choice == 5):
        
        length, width, height, surface_area = 0.0, 0.0, 0.0, 0.0
        want_to_continue = "Yes"


        while(WantToContinue == "Yes"):
            ValidLengthInp = "Yes"
            ValidWidthInp = "Yes"
            ValidHeightInp = "Yes"


            # --- Get the base length ---
            length = float(input("\nEnter the base length of the rectangular pyramid : "))
            print()
            if(length<0):
                print("The base length value cannot be negative.")
                ValidLengthInp = "No"
            if(length==0.0):
                print("The base length value cannot be zero.")
                ValidLengthInp = "No"


            # --- Get the base width only if base length value is valid ---

            if(ValidLengthInp == "Yes"):
                width = float(input("Enter the base width of the rectangular pyramid : "))
                print()
                if(width<0):   
                  print("The base width value cannot be negative.")
                  ValidWidthInp = "No"
                if(width==0.0):
                  print("The base width value cannot be zero.")
                  ValidWidthInp = "No"


            # --- Get the Height only if base length and base width values are valid ---

            if(ValidLengthInp == "Yes" and ValidWidthInp == "Yes"):
                height = float(input("Enter the height of the rectangular pyramid : "))
                print()
                if(height<0):   
                  print("The height value cannot be negative.")
                  ValidHeightInp = "No"
                if(height==0.0):
                  print("The height value cannot be zero.")
                  ValidHeightInp = "No"

            # --- Calculate & the surface area only if the values are valid ---

            if(ValidLengthInp == "Yes" and ValidWidthInp == "Yes" and ValidHeightInp == "Yes"):
               surface_area = (length*width)+length*((((width/2)*(width/2))+(height*height))**0.5)+width*((((length/2)*(length/2))+(height*height))**0.5)
               
               # --- Display the  surface area ---
               print("The surface area of the rectangular pyramid = ",format(surface_area,'.2f'),"cm\u00B2""\n")
            else:
                print("Could not calculate the surface area due to invalid inputs. Please try again with valid inputs.\n")

            continuation()

    elif (choice == 6):
        exit()

    else:
        print("Enter a valid option (1,2,3,4,5 or 6)\n")
        main()

main()
