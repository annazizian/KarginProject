from unittest import TestCase
from unittest.mock import patch
from copy import deepcopy

from search_engine.typo_fixer_engine import TypoFixerEngine
from search_engine.processors import TypoFixerProcessor


class TypoFixerEngineTester(TestCase):
    def setUp(self):
        TypoFixerEngine.typo_fixer_processor = TypoFixerProcessor()

    def tearDown(self):
        TypoFixerEngine.typo_fixer_processor = TypoFixerProcessor()

    @patch("search_engine.processors.IGNORE_SYMBOLS", set(","))
    def test_typo_fixer_engine_check_line(self):
        self.assertTrue(TypoFixerEngine.check_line([["one", "two"]],
                                                   "one, two"))
    
    @patch("search_engine.processors.IGNORE_SYMBOLS", set(","))
    def test_add_data(self):
        engine = TypoFixerEngine()
        engine.feed_data({"script": ["one, two"]})
        self.assertSetEqual(engine.typo_fixer_processor.words(),
                            {"one", "two"})

    def test_tearDown(self):
        self.assertSetEqual(TypoFixerEngine.typo_fixer_processor.words(),
                            set())
