"""Unit Tests"""

import re
import unittest


class TestData(unittest.TestCase):
    SP_DATA = {
        "Level 12": [],
        "Level 11": [
            ("Played", "2015-02-14")
        ],
        "Level 10": [
            ("Played", "2014-05-26")
        ],
        "Level 9": [
            ("Normal Clear", "2013-08-30"),
            ("Easy Clear", "2013-08-30"),
            ("Played", "2013-03-08")
        ],
        "Level 8": [
            ("Normal Clear", "2014-01-17"),
            ("Easy Clear", "2013-09-02"),
            ("Played", "2013-01-06")
        ],
        "Level 7": [
            ("Hard Clear", "2013-12-07"),
            ("Normal Clear", "2013-02-12"),
            ("Easy Clear", "2013-02-12"),
            ("Played", "2012-10-06"),
            ("A", "2013-09-29")
        ],
        "Level 6": [
            ("EX Hard Clear", "2014-12-22"),
            ("Hard Clear", "2013-03-17"),
            ("Normal Clear", "2013-01-07"),
            ("Easy Clear", "2013-01-07"),
            ("Played", "2012-09-23"),
            ("A", "2013-07-20")
        ],
        "Level 5": [
            ("EX Hard Clear", "2013-09-02"),
            ("Hard Clear", "2013-01-14"),
            ("Normal Clear", "2012-06-08"),
            ("Easy Clear", "2012-06-08"),
            ("Played", "2012-06-01"),
            ("AA", "2015-02-14"),
            ("A", "2013-06-08")
        ],
        "Level 4": [
            ("Full Combo", "2014-11-23"),
            ("EX Hard Clear", "2013-06-07"),
            ("Hard Clear", "2012-12-01"),
            ("Normal Clear", "2012-06-15"),
            ("Easy Clear", "2012-06-15"),
            ("Played", "2012-05-21"),
            ("AA", "2013-06-08"),
            ("A", "2013-06-08")
        ],
        "Level 3": [
            ("Full Combo", "2013-08-18"),
            ("EX Hard Clear", "2012-11-21"),
            ("Hard Clear", "2011-11-27"),
            ("Normal Clear", "2011-11-17"),
            ("Easy Clear", "2011-11-17"),
            ("Played", "2011-11-13"),
            ("AA", "2013-06-08"),
            ("A", "2013-06-08")
        ],
        "Level 2": [
            ("Full Combo", "2012-11-15"),
            ("EX Hard Clear", "2012-11-15"),
            ("Hard Clear", "2011-08-03"),
            ("Normal Clear", "2011-08-03"),
            ("Easy Clear", "2011-08-03"),
            ("Played", "2011-08-03"),
            ("AA", "2013-06-08"),
            ("A", "2013-06-08")
        ],
        "Level 1": [
            ("Full Combo", "2012-11-12"),
            ("EX Hard Clear", "2012-11-12"),
            ("Hard Clear", "2011-07-16"),
            ("Normal Clear", "2011-07-16"),
            ("Easy Clear", "2011-07-16"),
            ("Played", "2011-06-19"),
            ("AAA", "2013-09-08"),
            ("AA", "2013-06-08"),
            ("A", "2013-06-08")
        ],
        "First AAA": [
            ("Level 9", "2014-10-19", "the trigger of innocence [A]"),
            ("Level 8", "2013-11-10", "PROMISE FOR LIFE [A]"),
            ("Level 1", "2012-06-03", "I FIGHT ME [N]")
        ],
        "First Full Combo": [
            ("Level 9", "2014-05-11", "We are Disっ娘よっつ打ち命 [A]"),
            ("Level 8", "2013-02-25", "One of A Kind [H]"),
            ("Level 1", "2011-07-21", "FLOWERS for ALBION [N]")
        ],
        "First New Level": [
            ("Level 12", "2015-10-03", "Innocent Walls [H]"),
            ("Level 11", "2013-05-23", "Halfway of promise [A]"),
            ("Level 10", "2013-02-05", "PHOTONGENIC [H]"),
            ("Level 9", "2013-01-15", "quasar [H]"),
            ("Level 8", "2012-06-23", "ЁVOLUTIΦN [H]")
        ]
    }


    DP_DATA = {
        "Level 12": [],
        "Level 11": [],
        "Level 10": [],
        "Level 9": [],
        "Level 8": [],
        "Level 7": [
            ("Easy Clear", "2014-06-21"),
            ("Played", "2014-01-23")
        ],
        "Level 6": [
            ("Hard Clear", "2013-12-19"),
            ("Normal Clear", "2013-12-18"),
            ("Easy Clear", "2013-12-18"),
            ("Played", "2013-02-22")
        ],
        "Level 5": [
            ("Hard Clear", "2013-10-19"),
            ("Normal Clear", "2013-05-24"),
            ("Easy Clear", "2013-05-24"),
            ("Played", "2013-01-24"),
            ("A", "2013-10-19")
        ],
        "Level 4": [
            ("Hard Clear", "2013-02-05"),
            ("Normal Clear", "2013-02-05"),
            ("Easy Clear", "2013-02-05"),
            ("Played", "2012-12-25"),
            ("A", "2013-09-15")
        ],
        "Level 3": [
            ("EX Hard Clear", "2014-12-21"),
            ("Hard Clear", "2013-02-01"),
            ("Normal Clear", "2013-02-01"),
            ("Easy Clear", "2013-02-01"),
            ("Played", "2012-12-22"),
            ("AA", "2013-09-14"),
            ("A", "2013-08-23")
        ],
        "Level 2": [
            ("Full Combo", "2013-03-19"),
            ("EX Hard Clear", "2013-03-19"),
            ("Hard Clear", "2013-01-24"),
            ("Normal Clear", "2012-12-21"),
            ("Easy Clear", "2012-12-21"),
            ("Played", "2012-12-21"),
            ("AA", "2013-09-14"),
            ("A", "2013-07-01")
        ],
        "Level 1": [
            ("Full Combo", "2013-01-24"),
            ("EX Hard Clear", "2013-01-24"),
            ("Hard Clear", "2013-01-24"),
            ("Normal Clear", "2012-12-21"),
            ("Easy Clear", "2012-12-21"),
            ("Played", "2012-12-21"),
            ("AA", "2013-09-14"),
            ("A", "2013-07-01")
        ],
        "First AAA": [
            ("Level 1", "2013-05-15", "8bit Princess [N]")
        ],
        "First Full Combo": [
            ("Level 8", "2014-12-21", "M.D.Injection [H]"),
            ("Level 7", "2013-12-28", "EXTREMA PT.2 [H]"),
            ("Level 1", "2012-12-21", "GAMBOL [N]")
        ],
        "First New Level": [
            ("Level 9", "2013-11-27", "MAX LOVE [H]"),
            ("Level 8", "2013-09-15", "Survival Games [H]"),
            ("Level 7", "2013-02-22", "Drive Me Crazy [H]")
        ]
    }


    def _parse_file(self, filename):
        parsed = {}

        section_header = "# (Level \d+|First .*)$"
        clear_data = "(\w+(?: \w+)*) +\| (\d+-\d+-\d+)$"
        first_data = "(Level \d+) +\| (\d+-\d+-\d+) \| (.*)$"

        with open(filename, "r", encoding="UTF-8") as lines:
            def found(pattern, line):
                nonlocal match
                match = re.search(pattern, line)
                return match

            section = None
            match = None

            for line in lines:
                if found(section_header, line):
                    section = match.group(1)
                    parsed[section] = []
                elif found(clear_data, line):
                    parsed[section].append(match.group(1, 2))
                elif found(first_data, line):
                    parsed[section].append(match.group(1, 2, 3))
                else:
                    pass

        return parsed


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_data(self):
        play_data = [
            [TestData.SP_DATA, "sp_1_12.md", "sp_first.md"],
            [TestData.DP_DATA, "dp_1_12.md", "dp_first.md"]
        ]

        for data, file1, file2 in play_data:
            parsed_data = {**self._parse_file(file1), **self._parse_file(file2)}

            self.assertEqual(data, parsed_data)

            # just in case the assertion above isn't enough
            for k, v in data.items():
                self.assertIn(k, parsed_data)
                self.assertEqual(v, parsed_data[k])


if __name__ == "__main__":
    unittest.main()
