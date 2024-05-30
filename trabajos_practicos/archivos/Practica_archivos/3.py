"""
3. Crear una función que reciba como parámetros dos paths: uno correspondiente a un archivo de origen y otro correspondiente a un archivo de destino. 
La función debe leer el contenido del archivo de origen y luego transcribirlo en el archivo de destino. 
En caso de error la función retornará algún tipo de código de error indicando que paso.
"""

def copy_file(root_file: str, destiny_path: str):
    try:
        with open(root_file,'r') as root:
            content = root.readlines()
            with open(destiny_path,'w') as destiny:
                destiny.writelines(content)
    except:
        print(f"No se econtró la ruta {root_file}")

copy_file('trabajos_practicos/archivos/Practica_archivos/1_numbers.txt','trabajos_practicos/archivos/Practica_archivos/copy_numbers.txt')