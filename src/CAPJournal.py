#!/usr/bin/python
# -*- coding: utf-8 -*-

from CAPArticle import CAPArticle
from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

class CAPJournal:

    number = 0
    year = 0
    month = ""
    pages_path = ""
    pdf_path = ""
    jpg_cover_path = ""
    output_path = ""
    images_path = ""
    articles = []
    
    def __init__(self, number):
        self.number = number
        self.output_path = "output/" + str(self.number) + "/"
        self.images_path = self.output_path + "images/"

    
    def load_articles(self):
        # Prevent duplication
        self.articles = []

        # print("self.pages_path")
        # print(self.pages_path)
        
        openfile = open(self.pages_path, 'r')
        for row in openfile:
            start_page, end_page = row.strip().split(',')
            # print("--")
            # print(start_page)
            # print(end_page)
            cap_article = CAPArticle(start_page, end_page)
            self.articles.append(cap_article)

    def get_articles_count(self):
        return len(self.articles)

    

    def name_output(self, cap_number, start_page):
    
        number = cap_number

        if start_page < 10:
            filename = "%s_0%s" % (number, start_page)
        else:
            filename = "%s_%s" % (number, start_page)

        return filename

    
    
    def resize_image(self, large_image):
        new_width = 200
        img = Image.open(large_image)
        
        width = img.size[0]
        height = img.size[1]
        ratio = (new_width/float(width))
        
        new_height = int((float(height)*float(ratio)))

        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(large_image)


    def write_jpg(self, index):

        pdf_path = self.pdf_path
        images_path = self.images_path
        cap_number = self.number
        start_page = self.articles[index].start_page
    
        pages = convert_from_path(pdf_path, dpi=200, first_page=start_page, last_page=start_page)

        filename = self.name_output(cap_number, start_page)
        jpg_path = images_path + filename + ".jpg"
        self.articles[index].jpg_path = jpg_path

        for page in pages:
            page.save(jpg_path, 'JPEG')
            self.resize_image(jpg_path)


    def write_jpg_cover(self):

        pdf_path = self.pdf_path
        images_path = self.images_path
        cap_number = self.number
        start_page = 1 # Index of cover page
    
        pages = convert_from_path(pdf_path, dpi=200, first_page=start_page, last_page=start_page)

        filename = str(cap_number) + "_cover"
        jpg_cover_path = images_path + filename + ".jpg"

        for page in pages:
            page.save(jpg_cover_path, 'JPEG')
            self.resize_image(jpg_cover_path)

        self.jpg_cover_path = jpg_cover_path



    def write_pdf(self, index):

        articles_count = self.get_articles_count()

        if index < articles_count:
            # Since PDF pages start from index 0
            PAGE_INDEX_CORRECTION = 1

            cap_number = self.number
            start_page = self.articles[index].start_page
            end_page = self.articles[index].end_page
            
            inputpdf = PdfFileReader(open(self.pdf_path, "rb"))
            
            start_page_corrected = start_page - PAGE_INDEX_CORRECTION
            # print("start_page")
            # print(start_page)
            
            end_page_corrected = end_page - PAGE_INDEX_CORRECTION
            # print("end_page")
            # print(end_page)
            
            total_pages = end_page - start_page + PAGE_INDEX_CORRECTION
            # print("total_pages")
            # print(total_pages)

            output = PdfFileWriter()
            for i in range(total_pages):
                current_page = start_page_corrected + i
                output.addPage(inputpdf.getPage(current_page))

            filename = self.name_output(cap_number, start_page)

            pdf_path = self.output_path + filename + ".pdf"
            self.articles[index].pdf_path = pdf_path
            outputStream = file(pdf_path, "wb")
            output.write(outputStream)
            outputStream.close()
        else:
            print("Index out of range.")



    



