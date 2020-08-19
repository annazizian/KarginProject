from .processors import ProcessorMeta


class SearchEngine(metaclass=ProcessorMeta):
    processors = set()

    def __init__(self):
        self.data = []

    def feed_data(self, datum):
        self.data.append(datum)

    def search(self, phrase):
        for datum in self.data:
            for line in datum['script']:
                if not self.check_line(phrase, line['text']):
                    continue
                yield datum['url'], line
    
    @classmethod
    def check_line(cls, phrase, text):
        for processor in cls.processors:
            text = processor(text)
            phrase = processor(phrase)
        return cls._check_line(phrase, text)

    @classmethod
    def _check_line(cls, phrase, text):
        return phrase in text
