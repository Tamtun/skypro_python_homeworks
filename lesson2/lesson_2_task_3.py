def square(side):
    area = side * side
    if area != int(area):
        return int(area) + 1
    else:
        return int(area)
    
side = 5.7
area = square(side)
print("Площадь квадрата со стороной", side, "равна:", area)