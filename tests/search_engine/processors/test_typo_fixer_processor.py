from unittest import TestCase
from search_engine.processors import TypoFixerProcessor


class TestTypoFixerProcessor(TestCase):
    def test_typo_fixer_without_phrase_check(self):
        processor = TypoFixerProcessor()

        processor.add_word("first")
        processor.add_word("second")
        processor.add_word("third")
        processor.add_word("bird")

        self.assertIn("first", processor.typo_fixer("first"))
        self.assertIn("second", processor.typo_fixer("secnd"))
        self.assertIn("third", processor.typo_fixer("trd"))

        self.assertListEqual(processor("first"), ["first"])
        self.assertListEqual(processor(["first", "secnd"]),
                             [["first", "second"]])
        self.assertSetEqual(set(processor("bhird")), {"bird", "third"})
