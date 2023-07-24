from Bio import SeqIO
import sys

DNAs = []

with open(sys.argv[1]) as file:
    for record in SeqIO.parse(file, "fasta"):
        DNAs.append(str(record.seq))

overlaps = []
overlapping = []
for i in range(len(DNAs)):
    curr_read = DNAs[i]
    for j in range(len(curr_read) // 2, len(curr_read)):
        curr_suffix = curr_read[-(j + 1) :]
        for k in range(len(DNAs)):
            curr_comp = DNAs[k]
            for l in range(len(curr_comp) // 2, len(curr_comp)):
                curr_prefix = curr_comp[:l]
                if curr_suffix == curr_prefix:
                    overlaps.append(k)
                    overlapping.append([len(curr_suffix), i, k])

s = set(overlaps)
first_read = ""
count = len(overlapping)
for m in range(len(overlapping)):
    suf_index = overlapping[m][1]
    if suf_index not in s:  # find first read and initialise new str
        first_read = suf_index
        new_str = (
            reads[overlapping[m][1]] + reads[overlapping[m][2]][overlapping[m][0] :]
        )
        count -= 1
        pref_index = overlapping[m][2]
        while count > 0:  # when the first read is found, add
            for n in range(len(overlapping)):  # the remaining in the correct order
                if pref_index == overlapping[n][1]:
                    new_str += reads[overlapping[n][2]][overlapping[n][0] :]
                    pref_index = overlapping[n][2]
                    count -= 1

print(new_str)
