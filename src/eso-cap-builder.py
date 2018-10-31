#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import os
from PIL import Image
import sys
# import argparse

from CAPJournal import CAPJournal

def resize_image(inimage):
    new_width = 200
    img = Image.open(inimage)
    width = img.size[0]
    height = img.size[1]
    ratio = (new_width/float(width))
    new_height = int((float(height)*float(ratio)))
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(inimage)


def name_output(capnumber, start_page):
    
    number = capnumber

    if start_page == 1:
        output_filename = "%s_cover" % (number)
    else:

        if start_page < 10:
            output_filename = "%s_0%s" % (number, start_page)
        else:
            output_filename = "%s_%s" % (number, start_page)

    return output_filename


def write_jpg(capjournal, start_page):
    
    pages = convert_from_path(capjournal.pdf, 
        dpi=200, 
        first_page=start_page, 
        last_page=start_page)

    output_filename = name_output(capjournal.number, start_page)
    output = capjournal.outputpathimages + output_filename + ".jpg"

    for page in pages:
        page.save(output, 'JPEG')
        resize_image(output)



def write_pdf(capjournal, start_page, end_page):
    INDEX_CORRECTION = 1
    inputpdf = PdfFileReader(open(capjournal.pdf, "rb"))
    
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

    output_filename = name_output(capjournal.number, start_page)

    outputStream = file(capjournal.outputpath + output_filename + ".pdf", "wb")
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
    cap = CAPJournal()
    
    print("PDF file name: ")
    cap.pdf = raw_input()
    
    print("Pages file name: ")
    cap.pages = raw_input()

    print("Number: ")
    cap.number = int(raw_input())

    print("Year: ")
    cap.year = int(raw_input())

    print("Month: ")
    cap.month = raw_input()

    return cap

if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='Extracts PDF and thumbnails for CAPJournal issues.')
    # parser.add_argument('-pdf','--pdf_file', help='Input PDF file name',required=True)
    # parser.add_argument('-pages','--pages_file',help='Input Pages file name', required=True)
    # args = parser.parse_args()


    # pdf_file = args.pdf_file
    # pages_file = args.pages_file


    cap = CAPJournal()
    # cap = interactive_input()

    
    # print("cap.number")
    # print(cap.number)
    if not os.path.exists(cap.outputpathimages):
        os.makedirs(cap.outputpathimages)

    list_of_pages = read_pages(cap.pages)
    total_files = len(list_of_pages)

    # print("total_files")
    # print(total_files)

    
    write_jpg(cap, 1) # Cover image

    for i in range(total_files):
        start_page = list_of_pages[i][0]
        end_page = list_of_pages[i][1]
        write_pdf(cap, start_page, end_page)
        write_jpg(cap, start_page)
