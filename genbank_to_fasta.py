from Bio import SeqIO
import sys

gbk_filename = sys.argv[1]

input_handle  = open(gbk_filename, "r")

genome_record = SeqIO.read(gbk_filename, 'genbank')
for feature in genome_record.features:
    if feature.type == "CDS":
        print(">" + feature.qualifiers['db_xref'][0])
        print(feature.qualifiers['translation'][0])

'''
for seq_record in SeqIO.parse(input_handle, "genbank") :
    print(seq_record.id)
    print(seq_record.description)
    print(seq_record.seq)
    for feature in 
'''
