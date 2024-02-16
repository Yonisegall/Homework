RNA_to_Protien = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                  "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                  "UAU": "Y", "UAC": "Y",
                  "UGU": "C", "UGC": "C", "UGG": "W",
                  "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                  "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                  "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                  "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                  "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                  "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                  "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                  "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                  "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                  "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                  "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                  "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

from HW_8A.DNA import DNA
from RNA import RNA


class FastaFileReader:
    def __init__(self, pathway):
        """
            The constructor accepts the name of a file as a string. The constructor reads the file, and creates
            a dictionary whose key is the first line in the file and the value is the rest of the file
            :param pathway: A string
        """
        self.sequences_dict = {}
        try:
            with open(pathway, 'r') as g:
                pass
        except Exception:
            raise FileNotFoundError(f'The file {pathway} did not found')
        with open(pathway, 'r') as f:
            lines = f.readlines()
            line_1 = lines[0].split("\n")
            line_1_clean = line_1[0].split(">")
            str_nucleotides = ""
            for i in range(1, len(lines)):
                line = lines[i].split("\n")
                str_nucleotides += line[0]
            if "U" in str_nucleotides:
                str_nucleotides = RNA(str_nucleotides)
            else:
                str_nucleotides = DNA(str_nucleotides)
            self.sequences_dict[line_1_clean[1]] = str_nucleotides

    def transcript(self, sequence_details):
        """
            The method receives sequence information as a string and checks if the sequence exists in the dictionary.
            If the mapped sequence For input it is of type RNA, it writes it to a file and returns True. If the sequence
            is of the DNA type, it checks if it can be converted to RNA, and if possible, it copies the sequence to RNA,
            writes it to a file and returns True. Otherwise, the method will return False
            :param sequence_details: A string
            :return: True or False
        """
        if sequence_details in self.sequences_dict:
            if isinstance(self.sequences_dict.get(sequence_details), RNA):
                str_1 = str(self.sequences_dict.get(sequence_details))
            if isinstance(self.sequences_dict.get(sequence_details), DNA):
                str_1 = str(self.sequences_dict.get(sequence_details)).replace("T", "U")
                try:
                    RNA(str_1)
                except Exception:
                    return False
            with open('sequence_transcription.fna', 'w') as f:
                f.write(f'>{sequence_details}\n')
                count_1 = 0
                for y in str_1:
                    if count_1 == 70:
                        f.write("\n")
                        count_1 = 0
                    f.write(y)
                    count_1 += 1
            return True
        else:
            return False

    def translate(self, sequence_details):
        """
            The method receives sequence information as a string and checks if the sequence exists in the dictionary.
            If the mapped sequence The input is of the RNA type, it encodes it into an amino acid, writes it to a file
            and returns True. If the sequence is of the DNA type, it checks if it can be converted to RNA, and if
            possible, it copies the sequence to RNA, encodes it into an amino acid, writes it in a file and returns
            True. Otherwise, the method will return False
            :param sequence_details: A string
            :return: True or False
        """
        if sequence_details in self.sequences_dict:
            if isinstance(self.sequences_dict.get(sequence_details), RNA):
                str_2 = str(self.sequences_dict.get(sequence_details))
            if isinstance(self.sequences_dict.get(sequence_details), DNA):
                str_2 = str(self.sequences_dict.get(sequence_details)).replace("T", "U")
                try:
                    rna = RNA(str_2)
                except Exception:
                    return False
            num = 3
            nucl_3 = ""
            str_3 = ""
            for i in str_2:
                if num == 0:
                    str_3 += RNA_to_Protien.get(nucl_3)
                    num = 2
                    nucl_3 = ""
                    nucl_3 += i
                else:
                    nucl_3 += i
                    num -= 1
            with open('sequence_translation.faa', 'w') as d:
                d.write(f'>{sequence_details}\n')
                count_1 = 0
                for y in str_3:
                    if count_1 == 70:
                        d.write("\n")
                        count_1 = 0
                    d.write(y)
                    count_1 += 1
            return True
        else:
            return False
