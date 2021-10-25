#task5
def area_triangle(side1, side2, side3):
    semi_perimetre = 0.5 * (side1 + side2 + side3)
    area = (semi_perimetre*(semi_perimetre-side1)*(semi_perimetre-side2)*(semi_perimetre-side3))**0.5
    return area