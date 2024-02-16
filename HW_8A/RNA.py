from HW_8A.Nucleotides import Nucleotides
from Errors import *


class RNA(Nucleotides):
    def __init__(self, sequence):
        """
            The class inherits from the class "Nucleotides". The constractor constructs an
            RNA type sequence and checks that the sequence meets the conditions of an RNA sequence.
            :param sequence: A sequence of string type characters.
        """
        super().__init__(sequence)
        for i in sequence:
            if i not in "AUGC":
                raise NotNucleotideError(f'In {sequence} there are nucleotides that not from AUGC')
        if len(sequence) % 3 != 0:
            raise NotNucleotideError(f'The {sequence} sequence does not consist of threes')
        if sequence[0:3] != "AUG":
            raise NotNucleotideError(f'{sequence} do not start with AUG')
        if sequence[-3:] != "UAA" and sequence[-3:] != "UAG" and sequence[-3:] != "UGA":
            raise NotNucleotideError(f'{sequence} do not end with UAA or UAG or UGA')
        end_sec = sequence[-3:]
        flag_sec = ""
        count = 3
        index = 0
        for i in sequence:
            if index >= len(sequence) - 3:
                continue
            if count == 0:
                if flag_sec == end_sec:
                    raise NotNucleotideError(f'The final triple {end_sec} appears in another place in the sequence')
                flag_sec = ""
                count = 2
                flag_sec += i
                continue
            flag_sec += i
            index += 1
            count -= 1

    def calculate_mass(self):
        """ The method calculates the total mass of the RNA sequence """
        total_RNA_mass = 0
        for i in self.nucleotides_sequence:
            total_RNA_mass += self.nucleotides_mass.get(str(i))
        return total_RNA_mass + (70 * self.nucleotides_mass.get("A"))

    def mutate(self, mutation_position, nucleotide_letter):
        """
            The method receives a mutation to the RNA sequence and checks whether the mutation
            is normal. If it is normal, it changes the sequence with the new mutation.
            :param mutation_position: A non-negative number (index in the sequence)
            :param nucleotide_letter: A string with one character.
            :return: The new DNA sequence with the mutation.
        """
        if nucleotide_letter not in "AUGC":
            raise InputNotValidError(f'The letter {nucleotide_letter} is not from AUGC')
        if mutation_position > len(self.nucleotides_sequence):
            raise InputNotValidError(f'The DNA sequence has less then {mutation_position} nucleotides')
        self.nucleotides_sequence.delete(mutation_position)
        self.nucleotides_sequence.insert(mutation_position, nucleotide_letter)

    def RNA_generator(self):
        """ The method returns a generator that goes over the nucleotide sequence in groups of threes """
        generator = str(self.nucleotides_sequence)
        while len(generator) != 0:
            yield generator[0:3]
            generator = generator[3:]

    def validate_sequence(self):
        """
            The method validates the correctness of the sequence after creating mutations.
            The method returns True if the sequence is RNA Correct and False otherwise
            :return: True or False
        """
        result = True
        if str(self.nucleotides_sequence)[0:3] != "AUG":
            return False
        if str(self.nucleotides_sequence)[-3:] != "UAA" and str(self.nucleotides_sequence)[-3:] != "UAG" and str(self.nucleotides_sequence)[-3:] != "UGA":
            return False
        return result
