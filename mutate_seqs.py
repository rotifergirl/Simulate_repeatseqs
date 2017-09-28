from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from random import random,choice
import sys


mutated_reads=[]
def main(file_name,mutation_freq,out_file):
	records=list(SeqIO.parse(file_name,"fastq"))
	for read in records:
		sequence=(list(read.seq))
		for i in range(0,len(sequence)):
			val=random()
			if val < mutation_freq:
				sequence[i]=choice([x for x in "ACTG"])
		mut_seq=''.join(sequence)
		record = SeqRecord(Seq(mut_seq),id=read.id,name=read.name,description=read.description)
		record.letter_annotations["phred_quality"]=read.letter_annotations["phred_quality"]
		mutated_reads.append(record)
	SeqIO.write(mutated_reads,out_file,"fastq")

if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]),sys.argv[3])
    



