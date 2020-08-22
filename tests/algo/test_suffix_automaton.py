from unittest import TestCase

from algo.suffix_automaton import longest_common_substring


class TestSuffixAutomaton(TestCase):
    def test_longest_common_substring(self):
        self.assertEqual(
            longest_common_substring("zabcdefq", "cdefghx"),
            "cdef")
        self.assertEqual(
            longest_common_substring("zabcdefq", "wcdefghx"),
            "cdef")
        self.assertEqual(
            longest_common_substring("zabcdef", "wcdefghx"),
            "cdef")
    
    def test_longest_common_subsentence(self):
        self.assertListEqual(
            longest_common_substring("Here is a long sentence".split(),
                                     "Here is a short one".split()),
            ["Here", "is", "a"])
        self.assertListEqual(
            longest_common_substring("Come on you can find it".split(),
                                     "Here comes the sun".split()),
            [])
        self.assertListEqual(
            longest_common_substring(
                "If I were alone, I would cry".lower().split(),
                "And if I were with you, I'd be home and dry".lower().split()),
            ["if", "i", "were"])
