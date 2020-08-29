
from .processors import ProcessorMeta  # noqa
from .typo_fixer_processor import TypoFixerProcessor  # noqa


IGNORE_SYMBOLS = set("՜,՞՛;․՝-~.")


def case_insensitive(s, *, is_phrase=None):
    return s.lower()


def ignore_symbols(s, *, is_phrase=None):
    return ''.join(i for i in s if i not in IGNORE_SYMBOLS)


def splitter(s, *, is_phrase=None):
    return s.split()


def phrase_checking_processor(processor, *, is_phrase=None):
    fis_phrase = is_phrase

    def process(s, *, is_phrase=None):
        if fis_phrase is not None and is_phrase != fis_phrase:
            return s
        return processor(s)
    return process
