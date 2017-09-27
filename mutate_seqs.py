from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from random import random,choice



def read_file(file_name):
	records=list(SeqIO.parse(file_name,"fastq"))

mutated_reads=[]
def mutate_reads(file_name,mutation_freq):
	for read in records:
		sequence=(list(read.seq))
		for i in range(0,len(sequence)):
			val=random()
			if val < mutation_freq:
				sequence[i]=choice([x for x in "ACTG"])
			mut_seq=''.join(sequence)
			record = SeqRecord(mut_seq,read.id,"version 2")
		mutated_reads.append(record)

    
SeqIO.write(mutated_reads,'file_name_%i.fq'%(1),"fastq")


