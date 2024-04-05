from classShape_1 import Shape

class Triangle(Shape): #clase triangulo que hereda de super clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

class Isosceles(Triangle): #clase isosceles (dos de tres lados iguales) que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):#se verifica que lado es el que tiene una longitud diferente para tomarlo como la base den triangulo
                           #poder hallar su altura y por tanto su area
        if self.edges[0].length==self.edges[1].length:

            heigth=(self.edges[0].length**2-(self.edges[2].length/2)**2)**0.5
            area=(self.edges[2].length*heigth)/2

            return area


        elif self.edges[0].length==self.edges[2].length:

            heigth=(self.edges[0].length**2-(self.edges[1].length/2)**2)**0.5
            area=(self.edges[1].length*heigth)/2

            return area

        elif self.edges[1].length==self.edges[2].length:

            heigth=(self.edges[1].length**2-(self.edges[0].length/2)**2)**0.5
            area=(self.edges[0].length*heigth)/2

            return area
        
        else: 
            print("El triangulo no es isosceles") #si no tiene dos lados iguales, no es isosceles

class Equilateral(Triangle): #clase equilatero que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self): #todos los lados son iguales, por lo que se toma la longitud de unicamente primero para hallar altura y area del triangulo equilatero

        heigth=(self.edges[0].length**2+(self.edges[0].length/2)**2)**0.5
        area=(self.edges[0].length*heigth)/2

        return area

class TriRectangle(Triangle): #clase triangulo rectangulo que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):
        ordered_edges=sorted(edge.length for edge in self.edges)#se ordena la lista de aristas de menor a mayor longitud

        #la arista con mayor longitud sera la hipotenusa, por lo que para hallar el area solo se toman las dos primeras aristas (las mas pequeñas)
        #como base y altura del rectangulo

        widht=ordered_edges[0]
        height=ordered_edges[1]
        area=(widht*height)/2

        return area
    

class Scalene(Triangle): #clase escaleno que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):

        s=(self.edges[0].length+self.edges[1].length+self.edges[2].length)/2 #semiperimetro= (perimetro/2)
        area=(s*(s-self.edges[0].length)*(s-self.edges[1].length)*(s-self.edges[2].length))**0.5 # formula de Herón , usando el semiperimetro, 
                                                                                                  #para hallar el area del triangulo escaleno sin necesidad de hallar su altura.

        return area