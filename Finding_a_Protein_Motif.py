import requests, sys

API_URL = ["http://www.uniprot.org/uniprot/",".fasta"]

def check_Nglyco(protein:str) -> bool:
    if (protein[0] == "N" and 
    protein[1] != "P" and
    protein[2] in ["S", "T"] and
    protein[3] != "P"):
       return True
    return False

# open data
data = open(sys.argv[1]).readlines()

# clean names
API_names = []
for name in data:
    API_names.append(name[:name.find("_")])

# get protein data in API
protein_data = {}
for index in range(len(API_names)):
    protein_data[data[index].replace("\n", "")] = "".join(requests.get(API_URL[0]+API_names[index]+API_URL[1]).text.split("\n")[1:])

# for each protein get N-glycosylation motif (N{P}[ST]{P}) index 
indexes = {}

for protein in protein_data:
    amn = protein_data[protein]
    
    indexes[protein] = []
    
    for index in range(len(amn)-3):
        if check_Nglyco(amn[index:index+4]):
            indexes[protein].append(index+1)

# print result
for protein in indexes:
    if len(indexes[protein]) == 0: continue
    print(protein)
    for num in indexes[protein]:
        print(num, end=" ")
    print()