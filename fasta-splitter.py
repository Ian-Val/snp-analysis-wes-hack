from Bio import SeqIO

def split_fasta(id):
    for index in range(2):
        records = list(SeqIO.parse(f"./raw-data/{id}.fasta", "fasta"))
        output_sequences = []
        for i in range(len(records)):
            if i % 2 == index:
                records[i].id = records[i].id+str(index)
                output_sequences.append(records[i])
        f = open(f"./clean-data/{id}-clean-{index}.fasta", "w") 
        SeqIO.write(output_sequences, f"./clean-data/{id}-clean-{index}.fasta", "fasta")        

split_fasta('SRR19637188')
split_fasta('SRR19637190')
split_fasta('SRR19637216')