from unittest import TestCase

from yaml_parser.reader import read_yaml


class TestYamlReader(TestCase):
    def test_read_yaml(self):
        d = read_yaml('tests/data/yaml_test.yaml')
        self.assertTrue(set(d) == {'a', 'b', 'c'})
        self.assertIsInstance(d['c'], list)
        self.assertListEqual(d.pop('c'), [1, 2])
        self.assertDictEqual(d, {'a': 1, 'b': "00:00"})
