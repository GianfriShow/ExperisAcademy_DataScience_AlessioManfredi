# 1
# write a function called triangle_area() that takes as input base and height of a triangle and returns its area
# do the same with a square and a rectangle and make this repeatable, saving all results in a list

def area_game():

    def triangle_area(base, height):
        area = base*height/2
        return area

    def square_area(side):
        area = side**2
        return area

    def rectangle_area(base, height):
        area = base*height
        return area

    results = []
    continue_game = True

    while continue_game:
        choice = int(input("What would you like to find the area of? (type number)\n    1) Triangle\n    2) Square\n    3) Rectangle\n    4) Print results and exit\n"))
        if choice==4:
            print(results)
            continue_game = False
        elif choice==1:
            argument1 = float(input("Type the base of the triangle:\n"))
            argument2 = float(input("Type the height of the triangle:\n"))
            results.append(triangle_area(argument1,argument2))
        elif choice==2:
            argument1 = float(input("Type the side of the square:\n"))
            results.append(square_area(argument1))
        else:
            argument1 = float(input("Type the base of the rectangle:\n"))
            argument2 = float(input("Type the height of the rectangle:\n"))
            results.append(rectangle_area(argument1,argument2))

area_game()