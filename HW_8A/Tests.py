from HW_8A.DNA import DNA
from RNA import RNA
from FastaFileReader import FastaFileReader


############### Tests for DNA ###################
DNA_1 = DNA("ACGGCATTTGGGAAATAATCGC")
print(f"The main strand is:")
print(DNA_1.__str__())
print(f"The complementry strand is: {DNA_1.complement()}")
DNA_1.mutate("addition", 0, "ACG")
print(f"The DNA sequence post addition mutation is:{str(DNA_1)}")
DNA_1.mutate("replacement", 3, "AC")
print(f"The DNA sequence post replacement mutation is:{str(DNA_1)}")
DNA_1.mutate("deletion", 3, "AC")
print(f"The DNA sequence post deletion mutation is:{str(DNA_1)}")
print(f"The DNA sequence mass is:{DNA_1.calculate_mass()}")
print(DNA_1.nucleotides_number)
print(DNA_1.nucleotides_mass)


############### Tests for RNA ###################
RNA_1 = RNA("AUGGCUUAUUAA")
print(f"The RNA sequence is: {RNA_1}")
print(f"The RNA sequence mass is:{RNA_1.calculate_mass()}")
RNA_1.mutate(5, "A")
print(f"The RNA sequence post replacement mutation is:{str(RNA_1)}")
print(f"The RNA sequence validation output is :{RNA_1.validate_sequence()}")
RNA_generator = RNA_1.RNA_generator()
print(f"The RNA sequence in triples:")
print(next(RNA_generator))
print(next(RNA_generator))
print(next(RNA_generator))
print(next(RNA_generator))



################# Tests for Fasta ####################
fasta_file = FastaFileReader("sequence_example.fna")
print(f"The fasta file contains the sequences:" + "\n" +
      f"{fasta_file.sequences_dict.keys()}")
print(fasta_file.sequences_dict)
print(fasta_file.transcript("NC_000011.10:c5249857-5248269 HBG1 [organism=Homo sapiens] [GeneID=3047] [chromosome=11]"))
print(fasta_file.translate("NC_000011.10:c5249857-5248269 HBG1 [organism=Homo sapiens] [GeneID=3047] [chromosome=11]"))
