"""
Nombre: Federico
Apellido: Deniard
"""

suspects = [["Juan Perez","CGGGGCTAAAATTTTTTACGATCG"],
            ["María Rodríguez","AACGTTTAATGTTCTAAGCTGCG"],
            ["Carlos Sánchez","CGGGGCTAAAATTTTTTACGATCG"]]

def find_killer(dna: str, data_base: list):
    killer = "No hay ningún asesino"
    search_length = len(dna)
    for i in range(len(data_base)):
        suspect_dna = data_base[i][1]
        for j in range(len(suspect_dna)):
            if suspect_dna[j:j+search_length] == dna:
                killer = f"La persona culpable es: {data_base[i][0]}"
                break
    return killer

print(find_killer("CGTTTAATG",suspects))
