class Point: #clase punto
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def compute_distance(self,p2):
        distance=((self.x-p2.x)**2 + (self.y-p2.y)**2)**0.5
        return(distance)
    
class Line: #clase linea compuesta de puntos (punto inicial y final)
    def __init__(self,start_point:Point,end_point:Point,length):
        
        self.length=length#distancia entre ambos puntos => longitud de la arista
        self.start_point=start_point
        self.end_point=end_point

class Shape: #clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        
        self.is_regular=is_regular
        self.vertices=vertices
        self.edges=edges
        self.inner_angles=inner_angles

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar area()") #se usa polimorfismo para definir el metodo area de manera diferente dependiendo de la figura
    
    def compute_perimeter(self):# el perimetro se calcula igual en cualquier caso, por lo que se define inicialmente en la clase shape (la suma de las longitudes se las aristas dentro de la lista "edges")
        perimeter=0
        for edge in self.edges:
            perimeter += edge.length
        return perimeter
    
    def compute_inner_angles(self):# la suma de los angulos internos 
        angle_sum=0
        for angle in self.inner_angles:
            angle_sum+=angle
        return angle_sum