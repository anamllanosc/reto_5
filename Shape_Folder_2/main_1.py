from classTriangle_1 import Isosceles
from classRectangle_1 import Rectangle
from classShape_1 import Line,Point

def main():
    point_1 = Point(2,1)
    point_2 = Point(6,1)
    point_3 = Point(4,6)
    edges = [
        Line(point_1, point_2, point_1.compute_distance(point_2)),
        Line(point_1, point_3,point_1.compute_distance(point_3)), 
        Line(point_2, point_3,point_2.compute_distance(point_3))]
    vertices_t = [point_1, point_2, point_3] 
    triangle_1 = Isosceles(vertices_t, edges, [50,65,65]) #Se crea un triangulo isosceles


    point_1r = Point(3,1)
    point_2r = Point(7,1)
    point_3r = Point(7,8)
    point_4r = Point(3,8)
    edges_r = [
        Line(point_1r, point_2r, point_1r.compute_distance(point_2r)),
        Line(point_2r, point_3r,point_2r.compute_distance(point_3r)), 
        Line(point_3r, point_4r,point_3r.compute_distance(point_4r)),
        Line(point_4r, point_1r,point_4r.compute_distance(point_1r))]

    vertices_r=[point_1r, point_2r, point_3r, point_4r]
    rectangle_1=Rectangle(vertices_r, edges_r, [90,90,90,90])
    print(f"Área Triangulo: {triangle_1.compute_area()},Perimetro Triangulo: {triangle_1.compute_perimeter()}, Suma de ángulos internos Triangulo: {triangle_1.compute_inner_angles()}")
    print(f"Área Rectangulo: {rectangle_1.compute_area()},Perimetro Rectangulo: {rectangle_1.compute_perimeter()}, Suma de ángulos internos Rectangulo: {rectangle_1.compute_inner_angles()}")  

if __name__ == "__main__":
    main()
