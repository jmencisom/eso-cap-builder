import unittest
from CAPJournal import CAPJournal


class TestCAPJournalMethods(unittest.TestCase):

    def setUp(self):
        self.capjournal = CAPJournal(24)
        self.capjournal.year = 2018
        self.capjournal.month = "October"
        self.capjournal.pages_path = "24.txt"
        self.capjournal.pdf_path = "24.pdf"

    def test_get_articles_count(self):
        self.assertEqual(self.capjournal.get_articles_count(), 8)


if __name__ == '__main__':
    unittest.main()