
def write_txt():
    nombres = ["Joaquin","Mariela","Octavio"]
    with open("trabajos_practicos/archivos/nombres.txt","w") as file:
        for nombre in nombres:
            file.write(nombre)
            file.write("\n")

def write_csv():
    nombres = ["Joaquin","Mariela","Octavio"]
    apellidos = ["Supevielle","Diaz","Villegas"]
    edad = [23,15,54]
    with open("trabajos_practicos/archivos/agenda.csv","w") as file:
        for i in range(len(nombres)):
            persona = f"{nombres[i]},{apellidos[i]},{edad[i]}\n"
            file.write(persona)
write_csv()

def clean_line_csv(string: str) -> list:
    string = string.strip()
    string_list = string.split(',')
    return string_list

def read_csv():
    personas = []
    with open("trabajos_practicos/archivos/agenda.csv") as file:
        for line in file:
            persona = clean_line_csv(line)
            personas.append(persona)
    print(personas)

read_csv()