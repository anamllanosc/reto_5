# reto_5
## Shape_Folder_1
Esta carpeta contiene los archivos con la primera estructura. Tiene un paquete llamado "Shape_Package" y un modulo "main.py". El paquete "Shape_Package" esta compuesto a su vez de los modulos "__init__.py" y "classShape.py", este ultimo contiene todo el codigo relacionado con la clase shape, y es en "main.py" donde este es importado para poder crear el codigo de inicialización.

```css
estructura_archivos/
├── Shape_Folder_1/
│   ├── Shape_Package/
│   │   ├── __init__.py
│   │   └── classShape.py
│   └── main.py
```
## Shape_Folder_2
Esta carpeta contiene los archivos con la segunda estructura: modulos individuales que heredan de la clase Shape. En este caso se crean los modulos "classRectangle_1.py" y "classTriangle_1.py", que son los que importaran la clase Shape del modulo "classShape_1.py" para heredar de ella. Asi mismo se tiene el modulo "main_1.py", en donde es necesario importar la clase Isoceles de "classTriangle_1.py", la clase Rectangle de "classRectangle_1.py", y la clase Line y Point de "classShape_1.py", para poder crear y ejecutar el codigo de inicialiazacion.
```css
Shape_Folder_2
├── classRectangle_1.py
├── classTriangle_1.py
├── classShape_1.py
└── main_1.py
```


