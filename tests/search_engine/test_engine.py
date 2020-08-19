from unittest import TestCase

from search_engine.engine import SearchEngine


class TestEngine(TestCase):
    first_datum = {
        "name": "first",
        "url": "first",
        "script": [
            {
                "start_time": "00:00:00",
                "end_time": "00:00:01",
                "character": "A",
                "text": "Find"
            },
            {
                "start_time": "00:00:02",
                "end_time": "00:00:03",
                "character": "B",
                "text": "Other phrase"
            },
            {
                "start_time": "00:00:04",
                "end_time": "00:00:05",
                "character": "A",
                "text": "Case sensitive find"
            },

        ],
        "characters": [
            {"character": "A", "actor": "A"},
            {"character": "B", "actor": "B"}
        ]
    }
    second_datum = {
        "name": "second",
        "url": "second",
        "script": [
            {
                "character": "A",
                "text": "Another Find",
                "start_time": "00:00:00",
                "end_time": "00:00:01"
            },
            {
                "character": "A",
                "text": "Yet Another Find",
                "start_time": "00:00:02",
                "end_time": "00:00:03"
            }
        ],
        "characters": [
            {"character": "A", "actor": "A"}
        ]
    }

    def test_search(self):
        engine = SearchEngine()
        self.assertListEqual(list(engine.search('Find')),
                             [],
                             "There should be no matches without data")
        engine.feed_data(self.first_datum)
        self.assertListEqual(list(engine.search('Find')),
                             [(self.first_datum['url'],
                               self.first_datum['script'][0])])
        engine.feed_data(self.second_datum)
        self.assertListEqual(
            list(engine.search('Find')),
            [(self.first_datum['url'], self.first_datum['script'][0]),
             (self.second_datum['url'], self.second_datum['script'][0]),
             (self.second_datum['url'], self.second_datum['script'][1])])
