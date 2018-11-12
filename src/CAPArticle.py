#!/usr/bin/python
# -*- coding: utf-8 -*-

from CAPAuthor import CAPAuthor
import pyPdf
import subprocess

class CAPArticle:

    title = ""
    start_page = 0
    end_page = 0
    abstract = ""
    pdf_path = ""
    jpg_path = ""
    url = ""
    authors = []

    def __init__(self, start_page, end_page):
        self.start_page = int(start_page)
        self.end_page = int(end_page)

    def add_author(self, author):
        self.authors.append(author)

    
    def pdf_to_text(self, pdf):
        # args = ['pdftotext', '-x', '35', '-y', '30', '-W', '250', '-H', '25', '-q', pdf, '-']
        # args = ['pdftotext', '-x', '35', '-y', '30', '-W', '250', '-H', '30', '-q', pdf, '-']
        args = ['pdftotext', '-x', '35', '-y', '30', '-W', '350', '-H', '30', '-q', pdf, '-']
        text = subprocess.check_output(args, universal_newlines=True)
        # print("text")
        # print(text)
        text = text.strip()
        last_index = text.find('\n')
        text = text[:last_index]
        return text


    def set_title(self):
        pdf_path = self.pdf_path
        self.title = self.pdf_to_text(pdf_path)


        # print("self.title")
        # print(self.title)

        # in_file = self.pdf_path
        # out_file = self.pdf_path + "-title.pdf"

        # with open(in_file, 'rb') as infp:
        #     reader = pyPdf.PdfFileReader(infp)
        #     page = reader.getPage(0)
        #     writer = pyPdf.PdfFileWriter()
        #     page.mediaBox.lowerLeft = 30, 750
        #     page.mediaBox.upperRight = 570, 800
        #     # you could do the same for page.trimBox and page.cropBox
        #     writer.addPage(page)
        #     with open(out_file, 'wb') as outfp:
        #         writer.write(outfp)
        #         title = self.pdf_to_text(out_file)
        #         print(title)



        