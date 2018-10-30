#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import os
from PIL import Image
import sys
import argparse


def resize_image(inimage):
    new_width = 200
    img = Image.open(inimage)
    width = img.size[0]
    height = img.size[1]
    ratio = (new_width/float(width))
    new_height = int((float(height)*float(ratio)))
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(inimage)


def name_output(filename, start_page):
    
    name_no_extension = os.path.splitext(filename)[0]

    if start_page == 1:
        output_filename = "%s_cover" % (name_no_extension)
    else:

        if start_page < 10:
            output_filename = "%s_0%s" % (name_no_extension, start_page)
        else:
            output_filename = "%s_%s" % (name_no_extension, start_page)

    return output_filename


def write_jpg(pdf_file, start_page):
    
    pages = convert_from_path(pdf_file, dpi=200, first_page=start_page, last_page=start_page)

    output_filename = name_output(pdf_file, start_page)
    output = output_filename + ".jpg"

    for page in pages:
        page.save(output, 'JPEG')
        resize_image(output)



def write_pdf(pdf_file, start_page, end_page):
    INDEX_CORRECTION = 1
    inputpdf = PdfFileReader(open(pdf_file, "rb"))
    
    start_page_corrected = start_page - INDEX_CORRECTION
    # print("start_page")
    # print(start_page)
    
    end_page_corrected = end_page - INDEX_CORRECTION
    # print("end_page")
    # print(end_page)
    
    total_pages = end_page - start_page + INDEX_CORRECTION
    # print("total_pages")
    # print(total_pages)

    output = PdfFileWriter()
    for i in range(total_pages):
        current_page = start_page_corrected + i
        output.addPage(inputpdf.getPage(current_page))

    output_filename = name_output(pdf_file, start_page)

    outputStream = file(output_filename + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    


def text_to_int(list_of_text):
    FIRST_PAGE_INDEX = 0
    LAST_PAGE_INDEX = 1
    list_of_int = list_of_text
    list_of_text_len = len(list_of_text)
    # print(list_of_text_len)
    # print(list_of_text[0][0])
    for i in range(list_of_text_len):
        # print(i)        
        list_of_int[i][FIRST_PAGE_INDEX] = int(list_of_text[i][FIRST_PAGE_INDEX])
        list_of_int[i][LAST_PAGE_INDEX] = int(list_of_text[i][LAST_PAGE_INDEX])
    return list_of_int

def read_pages(pages_file):
    list_of_pages_text = []
    openfile = open(pages_file, 'r')
    for row in openfile:
        row_item = row.strip().split(',')
        list_of_pages_text.append(row_item)
    
    list_of_pages = text_to_int(list_of_pages_text)
    return list_of_pages

def interactive_input():
    print("PDF file name: ")
    pdf_file = raw_input()
    print("Pages file name: ")
    pages_file = raw_input()

    return pdf_file, pages_file

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Extracts PDF and thumbnails for CAPJournal issues.')
    parser.add_argument('-pdf','--pdf_file', help='Input PDF file name',required=True)
    parser.add_argument('-pages','--pages_file',help='Input Pages file name', required=True)
    args = parser.parse_args()


    pdf_file = args.pdf_file
    pages_file = args.pages_file

    list_of_pages = read_pages(pages_file)
    total_files = len(list_of_pages)

    # print("total_files")
    # print(total_files)

    write_jpg(pdf_file, 1) # Cover image

    for i in range(total_files):
        start_page = list_of_pages[i][0]
        end_page = list_of_pages[i][1]
        write_pdf(pdf_file, start_page, end_page)
        write_jpg(pdf_file, start_page)

