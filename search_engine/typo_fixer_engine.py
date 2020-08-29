from .basic_engines import BaseEngine
from .processors import splitter
from .processors import TypoFixerProcessor
from .processors import phrase_checking_processor


class TypoFixerEngine(BaseEngine):
    typo_fixer_processor = TypoFixerProcessor()
    processors = [phrase_checking_processor(
                      splitter, is_phrase=True),
                  phrase_checking_processor(
                      typo_fixer_processor, is_phrase=True)]

    def feed_data(self, data):
        super().feed_data(data)

        for line in data['script']:
            line = self.process(line, is_phrase=False)
            for word in line.split():
                self.typo_fixer_processor.add_word(word)

    @classmethod
    def _check_line(cls, phrases, text):
        return any(' '.join(phrase) in text for phrase in phrases)
