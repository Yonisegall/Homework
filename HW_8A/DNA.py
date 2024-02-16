from Nucleotides import Nucleotides
from Errors import *
from DoublyLinkedList import *


class DNA(Nucleotides):
    def __init__(self, sequence):
        """
            The class inherits from the class "Nucleotides". The constractor constructs a
            DNA type sequence and checks that the sequence meets the conditions of a DNA sequence.
            :param sequence: A sequence of string type characters.
        """
        super().__init__(sequence)
        for i in sequence:
            if i not in "ATGC":
                raise NotNucleotideError(f'In {sequence} there are nucleotides that not from ATGC')

    def complement(self):
        """
            The method returns a two-way linked list of the characters of the sequence in
            reverse order with each character becoming another character.
            "A" to "T"
            "T" to "A"
            "G" to "C"
            "C" to "G"
        """
        complementary_strand = DoublyLinkedList()
        for i in self.nucleotides_sequence.__str__():
            if i == "A":
                complementary_strand.push("T")
            if i == "T":
                complementary_strand.push("A")
            if i == "G":
                complementary_strand.push("C")
            if i == "C":
                complementary_strand.push("G")
        return complementary_strand

    def calculate_mass(self):
        """ The method calculates the total mass of the DNA sequence """
        total_DNA_mass = 0
        for u in self.nucleotides_sequence:
            total_DNA_mass += (self.nucleotides_mass.get(str(u)))
        for i in self.complement():
            total_DNA_mass += (self.nucleotides_mass.get(str(i)))
        return total_DNA_mass

    def mutate(self, mutation_type, mutation_position, nucleotides_mutation):
        """
            The method receives a mutation to the DNA sequence and checks whether the mutation is normal.
            If it is normal, it changes the sequence with the new mutation
            :param mutation_type: Addition, replacement, deletion
            :param mutation_position: A non-negative number (index in the sequence)
            :param nucleotides_mutation: A string
            :return: The new DNA sequence with the mutation.
        """
        for i in nucleotides_mutation:
            if i not in "ATGC":
                raise InputNotValidError("The sequence not good")
        if mutation_type == "addition":
            if mutation_position > len(self.nucleotides_sequence):
                raise InputNotValidError(f'The DNA sequence has less then {mutation_position} nucleotides')
            while len(nucleotides_mutation) != 0:
                self.nucleotides_sequence.insert(mutation_position, nucleotides_mutation[len(nucleotides_mutation) - 1])
                nucleotides_mutation = nucleotides_mutation[:-1]
        if mutation_type == "replacement":
            if mutation_position > len(self.nucleotides_sequence):
                raise InputNotValidError(f'The DNA sequence has less then {mutation_position} nucleotides')
            count_1 = len(nucleotides_mutation) + mutation_position
            if count_1 > len(self.nucleotides_sequence):
                raise InputNotValidError(f'from index {mutation_position} the DNA sequence has less then'
                                         f' {len(nucleotides_mutation)} nucleotides')
            count_2 = len(nucleotides_mutation)
            while count_2 > 0:
                self.nucleotides_sequence.delete(mutation_position)
                count_2 -= 1
            while len(nucleotides_mutation) != 0:
                self.nucleotides_sequence.insert(mutation_position, nucleotides_mutation[-1])
                nucleotides_mutation = nucleotides_mutation[:-1]
        if mutation_type == "deletion":
            if mutation_position > len(self.nucleotides_sequence):
                raise InputNotValidError(f'The DNA sequence has less then {mutation_position} nucleotides')
            loc_1 = mutation_position + len(nucleotides_mutation) - 1
            loc_2 = len(nucleotides_mutation) - 1
            if loc_1 > len(self.nucleotides_sequence):
                raise InputNotValidError(f'from index {mutation_position} the DNA sequence has less then'
                                         f' {len(nucleotides_mutation)} nucleotides')
            while loc_1 != mutation_position - 1:
                a = str(self.nucleotides_sequence[loc_1])
                b = nucleotides_mutation[loc_2]
                if str(self.nucleotides_sequence[loc_1]) != nucleotides_mutation[loc_2]:
                    raise ValueError(f'The {nucleotides_mutation} sequence is not exist in the DNA sequence in '
                                     f'index {mutation_position}')
                self.nucleotides_sequence.delete(loc_1)
                loc_1 -= 1
                loc_2 -= 1
