from .engine import SearchEngine
from .processors import case_insensitive, ignore_symbols


class CaseInsensitiveEngine(SearchEngine):
    processors = {case_insensitive}


class IgnoreSymbolsEngine(SearchEngine):
    processors = {ignore_symbols}


class BaseEngine(IgnoreSymbolsEngine, CaseInsensitiveEngine):
    """This is the engine which will be mainly used and derived from"""
