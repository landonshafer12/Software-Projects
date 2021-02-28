choice = int(input("Enter your choice:\n1)Calculate circumference\n2)Calculate area\n0)Exit\n"))

while(choice!=0):
    if(choice==1): #Explain
        print("Calculating circumference of a circle: ")
        radius = float(input("What is the radius: "))
        circumference = 2*3.14159*radius;
        print("The circumference is: " + str(circumference));
        choice = int(input("Enter your choice:\n1)Calculate circumference\n2)Calculate area\n0)Exit\n"))
    elif(choice==2): #Explain
        print("Calculating area of a circle: ")
        radius = float(input("What is the radius: "))
        area = 2*3.14159*radius*radius;
        print("The area is: " + str(area));
        choice = int(input("Enter your choice:\n1)Calculate circumference\n2)Calculate area\n0)Exit\n"))
    elif(choice==0): #Explain
        choice=0
    else: #Explain
        print("You entered a wrong number. Please use 1, 2, or 0 as your choice. ")
        choice = int(input("Enter your choice:\n1)Calculate circumference\n2)Calculate area\n0)Exit\n"))
