from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio.Seq import Seq
count = 0
total_len = 0
sequences = [None, None, None]
sequence_fn = ['SRR19637188.fasta','SRR19637190.fasta','SRR19637216.fasta']

for i in range(len(sequences)):
    with open(f"./data/{sequence_fn[i]}") as in_handle:
        sequence_data = ''
        for title, seq in SimpleFastaParser(in_handle):
            sequence_data += seq
        sequences[i] = Seq(sequence_data)
    print(sequences[i])