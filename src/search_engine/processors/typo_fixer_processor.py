from trie.trie import Trie


class TypoFixerProcessor:
    def __init__(self):
        self.trie = Trie(zero_complete=False)

    def typo_fixer(self, text, *, is_phrase=None):
        return self.trie.autocomplete(text)

    def add_word(self, word):
        self.trie[word] = None

    def words(self):
        return set(self.trie.keys())

    def __call__(self, text, *, is_phrase=None):
        if isinstance(text, str):
            return self.typo_fixer(text, is_phrase=is_phrase)
        if len(text) == 1:
            return [[word]
                    for word in self.typo_fixer(text[0], is_phrase=is_phrase)]
        return [[fixed_word] + fixed_rest
                for fixed_word in self.typo_fixer(text[0], is_phrase=is_phrase)
                for fixed_rest in self(text[1:], is_phrase=is_phrase)]
