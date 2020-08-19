class SearchEngine:
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
    
    def check_line(self, phrase, text):
        return phrase in text
