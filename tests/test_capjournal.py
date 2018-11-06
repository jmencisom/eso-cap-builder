import unittest


class TestCAPJournalMethods(unittest.TestCase):

    def setUp(self):
        capjournal = CAPJournal(24)
        self.year = 2018
        self.month = "October"
        self.pages = "24.txt"
        self.pdf = "24.pdf"

    def test_number_of_articles_from_pages_file(self):
        self.assertEqual(self.capjournal.get_article_count(), 8)


if __name__ == '__main__':
    unittest.main()