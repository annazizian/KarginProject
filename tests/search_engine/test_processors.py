from unittest import TestCase
from unittest.mock import patch

from search_engine.basic_engines import CaseInsensitiveEngine
from search_engine.basic_engines import IgnoreSymbolsEngine
from search_engine.basic_engines import BaseEngine


class TestCaseInsensitiveEngine(TestCase):
    def test_check_line(self):
        self.assertTrue(CaseInsensitiveEngine.check_line(
            "phrase",
            "The phrase in the text."))
        self.assertTrue(CaseInsensitiveEngine.check_line(
            "phrase",
            "Phrase in the beginning."))
        self.assertTrue(CaseInsensitiveEngine.check_line(
            "phrase",
            "This sentence ends with the phrase."))
        self.assertFalse(CaseInsensitiveEngine.check_line(
            "phrase",
            "You won't find here what you are looking for."))
        self.assertFalse(CaseInsensitiveEngine.check_line(
            "phrase",
            "This phra~se won't match."))


class TestIgnoreSymbolsEngine(TestCase):
    @patch("search_engine.processors.IGNORE_SYMBOLS", set("~."))
    def test_check_line(self):
        self.assertTrue(IgnoreSymbolsEngine.check_line(
            "phrase",
            "This phra~se will match."))
        self.assertFalse(IgnoreSymbolsEngine.check_line(
            "phrase",
            "Phrases in wrong case won't match."))
        self.assertTrue(IgnoreSymbolsEngine.check_line(
            "phrase",
            "But p.h.r.a.s.e~s containing ignored symbols will."))


class TestBaseEngine(TestCase):
    @patch("search_engine.processors.IGNORE_SYMBOLS", set("~."))
    def test_check_line(self):
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "This phra~se will match."))
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "Phrases in wrong case won't match."))  # It's a joke. Haha
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "But p.h.r.a.s.e~s containing ignored symbols will."))
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "The phrase in the text."))
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "Phrase in the beginning."))
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "This sentence ends with the phrase."))
        self.assertTrue(BaseEngine.check_line(
            "phrase",
            "This phra~se won't match."))  # It's a joke. Haha
        self.assertFalse(BaseEngine.check_line(
            "phrase",
            "You won't find here what you are looking for."))
