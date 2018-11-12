#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from CAPJournal import CAPJournal
from CAPArticle import CAPArticle


class TestCAPJournalMethods(unittest.TestCase):

    def setUp(self):
        self.capjournal = CAPJournal(24)
        self.capjournal.year = 2018
        self.capjournal.month = "October"
        self.capjournal.pages_path = "24.txt"
        self.capjournal.pdf_path = "24.pdf"

        self.capjournal.load_articles()

    # def test_get_articles_count(self):
    #     self.assertEqual(self.capjournal.get_articles_count(), 8)

    # def test_write_single_pdf(self):
    #     ARTICLE_INDEX = 0
    #     self.capjournal.write_pdf(ARTICLE_INDEX)
    #     expected_pdf_path = "output/24/24_03.pdf"
    #     real_pdf_path = self.capjournal.articles[ARTICLE_INDEX].pdf_path
    #     self.assertEqual(expected_pdf_path, real_pdf_path)

    #     ARTICLE_INDEX = 4
    #     self.capjournal.write_pdf(ARTICLE_INDEX)
    #     expected_pdf_path = "output/24/24_17.pdf"
    #     real_pdf_path = self.capjournal.articles[ARTICLE_INDEX].pdf_path
    #     self.assertEqual(expected_pdf_path, real_pdf_path)

    #     ARTICLE_INDEX = 7
    #     self.capjournal.write_pdf(ARTICLE_INDEX)
    #     expected_pdf_path = "output/24/24_40.pdf"
    #     real_pdf_path = self.capjournal.articles[ARTICLE_INDEX].pdf_path
    #     self.assertEqual(expected_pdf_path, real_pdf_path)

    # def test_write_single_jpg(self):
    #     ARTICLE_INDEX = 0
    #     self.capjournal.write_jpg(ARTICLE_INDEX)
    #     expected_jpg_path = "output/24/images/24_03.jpg"
    #     real_jpg_path = self.capjournal.articles[ARTICLE_INDEX].jpg_path
    #     self.assertEqual(expected_jpg_path, real_jpg_path)

    #     ARTICLE_INDEX = 4
    #     self.capjournal.write_jpg(ARTICLE_INDEX)
    #     expected_jpg_path = "output/24/images/24_17.jpg"
    #     real_jpg_path = self.capjournal.articles[ARTICLE_INDEX].jpg_path
    #     self.assertEqual(expected_jpg_path, real_jpg_path)

    #     ARTICLE_INDEX = 7
    #     self.capjournal.write_jpg(ARTICLE_INDEX)
    #     expected_jpg_path = "output/24/images/24_40.jpg"
    #     real_jpg_path = self.capjournal.articles[ARTICLE_INDEX].jpg_path
    #     self.assertEqual(expected_jpg_path, real_jpg_path)

    # def test_write_jpg_cover(self):
    #     self.capjournal.write_jpg_cover()
    #     expected_jpg_cover_path = "output/24/images/24_cover.jpg"
    #     real_jpg_cover_path = self.capjournal.jpg_cover_path
    #     self.assertEqual(expected_jpg_cover_path, real_jpg_cover_path)

    # def test_write_ads(self):
    #     self.capjournal.write_ads()
    #     expected_path = "output/24/ads.txt"
    #     real_path = self.capjournal.ads_path
    #     self.assertEqual(expected_path, real_path)

    def test_write_title_8_from_pdf(self):
        cap_article = CAPArticle(40, 49)
        cap_article.pdf_path = "output/24/24_40.pdf"
        cap_article.set_title()
        expected_title = "Your Night out under the Stars: Reaching beyond Native Audiences"
        real_title = cap_article.title
        self.assertEqual(expected_title, real_title)

    def test_write_title_7_from_pdf(self):
        cap_article = CAPArticle(32, 39)
        cap_article.pdf_path = "output/24/24_32.pdf"
        cap_article.set_title()
        expected_title = "Videos for Astronomy Education and Outreach"
        real_title = cap_article.title
        self.assertEqual(expected_title, real_title)

    def test_write_title_6_from_pdf(self):
        cap_article = CAPArticle(25, 31)
        cap_article.pdf_path = "output/24/24_25.pdf"
        cap_article.set_title()
        expected_title = "Engaging the Public with Supernova and Supernova Remnant Research Using Virtual Reality"
        real_title = cap_article.title
        self.assertEqual(expected_title, real_title)

    

if __name__ == '__main__':
    unittest.main()