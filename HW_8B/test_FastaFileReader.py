from unittest import TestCase
from FastaFileReader import FastaFileReader


class TestFasta(TestCase):
    def test_init(self):
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/fasta')
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/file1_empty')
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/file2_just_detiles')
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/file3_just_detiles_2')
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/file4_just_detiles_3')
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/file5_just_n')
        self.assertRaises(ValueError, FastaFileReader, 'firefortest/file6_incorrect_dna')

    def test_transcript(self):
        assert False

    def test_translate(self):
        assert False
