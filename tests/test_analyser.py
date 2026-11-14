
import unittest

from dna_analyser import (
    validate_sequence,
    count_nucleotides,
    sequence_length,
    gc_content,
    reverse_complement,
    transcribe_dna,
)


class TestDNAAnalyser(unittest.TestCase):

    def test_validate_sequence(self):
        self.assertEqual(validate_sequence("atgc"), "ATGC")
        self.assertEqual(validate_sequence("  ACGT  "), "ACGT")

    def test_reject_invalid_sequences(self):
        for sequence in ("", "   ", "ATXB", "123"):
            with self.subTest(sequence=sequence):
                with self.assertRaises(ValueError):
                    validate_sequence(sequence)

    def test_count_nucleotides(self):
        self.assertEqual(
            count_nucleotides("ATGCCAT"),
            {"A": 2, "C": 2, "G": 1, "T": 2},
        )

    def test_sequence_length(self):
        self.assertEqual(sequence_length("ATGC"), 4)

    def test_gc_content(self):
        self.assertAlmostEqual(gc_content("AAAA"), 0.0)
        self.assertAlmostEqual(gc_content("ATGC"), 50.0)
        self.assertAlmostEqual(gc_content("GGCC"), 100.0)

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("ATGC"), "GCAT")
        self.assertEqual(reverse_complement("AAAA"), "TTTT")

    def test_reverse_complement_twice(self):
        sequence = "ATGCCAT"
        result = reverse_complement(reverse_complement(sequence))
        self.assertEqual(result, sequence)

    def test_transcription(self):
        self.assertEqual(transcribe_dna("ATGC"), "AUGC")
        self.assertEqual(transcribe_dna("CCCC"), "CCCC")


if __name__ == "__main__":
    unittest.main()
