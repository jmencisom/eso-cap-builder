#!/usr/bin/python
# -*- coding: utf-8 -*-

from CAPAuthor import CAPAuthor

class CAPArticle:

    title = ""
    start_page = 0
    end_page = 0
    abstract = ""
    pdf_path = ""
    jpg_path = ""
    authors = []

    def __init__(self, start_page, end_page):
        self.start_page = int(start_page)
        self.end_page = int(end_page)

    def add_author(self, author):
        self.authors.append(author)