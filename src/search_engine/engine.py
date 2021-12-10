from .processors import ProcessorMeta


class SearchEngine(metaclass=ProcessorMeta):
    processors = []

    def __init__(self):
        self.data = []

    def feed_data(self, datum):
        self.data.append(datum)

    def search(self, phrase):
        phrase = self.process(phrase, is_phrase=True)
        print(phrase)
        for datum in self.data:
            for line in datum['script']:
                if not self.check_line(phrase, line['text']):
                    continue
                yield datum['url'], line

    @classmethod
    def process(cls, text, *, is_phrase=None):
        for processor in cls.processors:
            text = processor(text, is_phrase=is_phrase)
        return text

    @classmethod
    def check_line(cls, phrase, text):
        return cls._check_line(phrase, cls.process(text, is_phrase=False))

    @classmethod
    def _check_line(cls, phrase, text):
        return phrase in text
