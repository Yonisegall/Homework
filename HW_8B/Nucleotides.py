from abc import ABC, abstractmethod
from Errors import *
from LinkedList import *


class Nucleotides(ABC):

    nucleotides_mass = {}
    file = 'NucleotideMW.txt'
    try:
        with open(file, 'r') as g:
            a = g.readlines()
            for i in range(1, 6):
                a_1 = a[i].split()
                nucleotides_mass[a_1[0][-2]] = float(a_1[2])
    except Exception:
        raise FileNotFoundError(f'The file {file} did not found')

    def __init__(self, sequence):
        """
            A constructor that receives a sequence of characters and checks if they match to create a
            "nucleotides sequence". The constructor has 2 fields, the first is a linked list of the
            characters and the second is a dictionary whose keys are the types of characters that are
            in the sequence and the value are the number of times the character appears in the sequence
            :param sequence: A sequence of string type characters.
        """
        if not isinstance(sequence, str):
            raise TypeError(f'{sequence} is not from string type')
        for i in sequence:
            if i not in "ATGCU":
                raise NotNucleotideError(f'In {sequence} there are nucleotides that not from ATGCU')
        self.nucleotides_sequence = LinkedList()
        self.nucleotides_number = {}
        for i in sequence:
            self.nucleotides_sequence.add_at_end(i)
            if i in self.nucleotides_number.keys():
                self.nucleotides_number[i] += 1
            else:
                self.nucleotides_number[i] = 1

    def __str__(self):
        """ The method return a string representation of this object """
        return self.nucleotides_sequence.__str__()

    def __len__(self):
        """ The method return the length of this object """
        return self.nucleotides_sequence.__len__()

    @abstractmethod
    def calculate_mass(self):
        pass

    @abstractmethod
    def mutate(self):
        pass
