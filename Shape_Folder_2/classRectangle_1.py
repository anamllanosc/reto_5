from classShape_1 import Shape

class Rectangle(Shape): #clase rectangulo que hereda de super clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self): 
        width=min(edge.length for edge in self.edges) #la arista con la menor longitud se toma como el ancho del rectangulo
        height=max(edge.length for edge in self.edges) #la arista con la mayor longitud se toma como el alto del rectangulo
        area=width*height
        return area 
    
class Square(Rectangle): #clase cuadrado que hereda de la super clase rectangulo
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):
        
        area=self.edges[0].length**2 #todos sus lados son iguales, por lo que simplemente se toma el primero y se eleva al cuadrado
        return area 