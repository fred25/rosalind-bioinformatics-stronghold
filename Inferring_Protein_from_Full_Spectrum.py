import sys
from Extras.rosalind_functions import mass_table_to_dict


def find_aa(current, ions, TABLE):
    for i in ions:
        for j in TABLE:
            if abs(TABLE[j] - (i-current)) < 0.001:
                return j, i
    return False

def infer_protein(ions:list, TABLE:dict) -> str:
    l = (len(ions)-2)//2
    
    protein = ""
    curr = ions[0]
    rest = ions[1:]
    
    while len(protein) < l:
        aa, ion = find_aa(curr, rest, TABLE)
        if aa:
            protein += aa
            curr += TABLE[aa]
            rest.remove(ion)
    
    return protein
    
if __name__ == "__main__":    
    TABLE = mass_table_to_dict(sys.argv[2])

    x_ions = []
    mass = .0

    with open(sys.argv[1]) as file:
        data = list(map(float, file.read().split("\n")))
        mass = data.pop(0)
        x_ions = data

    print(infer_protein(x_ions, TABLE))