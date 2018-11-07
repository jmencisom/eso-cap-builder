#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
from subprocess import call
import datetime
from CAPJournal import CAPJournal

class Application(Frame):

    def get_current_month(self):
        INDEX_CORRECTION = 1
        now = datetime.datetime.now()
        return now.month - INDEX_CORRECTION

    def get_current_year(self):
        now = datetime.datetime.now()
        return now.year

    
    def make_article_grid(self, capjournal):
        
        ARTICLE_COL_WIDTH = 10
        
        self.cap_article_id_label = Label(self.cap_articles_frame, text="Id", anchor="w", width=ARTICLE_COL_WIDTH)
        self.cap_article_id_label.grid(row=0, column=0)
        self.cap_article_title_label = Label(self.cap_articles_frame, text="Title", anchor="w", width=ARTICLE_COL_WIDTH)
        self.cap_article_title_label.grid(row=0, column=1)
        self.cap_article_authors_label = Label(self.cap_articles_frame, text="Authors", anchor="w", width=ARTICLE_COL_WIDTH)
        self.cap_article_authors_label.grid(row=0, column=2)
        self.cap_article_abstract_label = Label(self.cap_articles_frame, text="Abstract", anchor="w", width=ARTICLE_COL_WIDTH)
        self.cap_article_abstract_label.grid(row=0, column=3)
        self.cap_article_start_page_label = Label(self.cap_articles_frame, text="Start", anchor="w", width=ARTICLE_COL_WIDTH)
        self.cap_article_start_page_label.grid(row=0, column=4)
        self.cap_article_end_page_label = Label(self.cap_articles_frame, text="End", anchor="w", width=ARTICLE_COL_WIDTH)
        self.cap_article_end_page_label.grid(row=0, column=5)

        articles_count = capjournal.get_articles_count()

        self.cap_article_id_label = []
        self.cap_article_title_entry = []
        self.cap_article_authors_entry = []
        self.cap_article_abstract_entry = []
        self.cap_article_start_page_entry = []
        self.cap_article_end_page_entry = []

        for i in range(articles_count):
            id_label = Label(self.cap_articles_frame)
            id_label.grid(row=i+1, column=0)
            id_label["text"] = i + 1
            self.cap_article_id_label.append(id_label)

            title_entry = Entry(self.cap_articles_frame)
            title_entry.grid(row=i+1, column=1)
            self.cap_article_title_entry.append(title_entry)

            authors_entry = Entry(self.cap_articles_frame)
            authors_entry.grid(row=i+1, column=2)
            self.cap_article_authors_entry.append(authors_entry)

            abstract_entry = Entry(self.cap_articles_frame)
            abstract_entry.grid(row=i+1, column=3)
            self.cap_article_abstract_entry.append(abstract_entry)

            start_page_entry = Entry(self.cap_articles_frame)
            start_page_entry.grid(row=i+1, column=4)
            start_page_entry.insert(0, capjournal.articles[i].start_page)
            self.cap_article_start_page_entry.append(start_page_entry)

            end_page_entry = Entry(self.cap_articles_frame)
            end_page_entry.grid(row=i+1, column=5)
            end_page_entry.insert(0, capjournal.articles[i].end_page)
            self.cap_article_end_page_entry.append(end_page_entry)

        self.extract_pdf_button = Button(self.cap_articles_frame, text="Extract PDF", command=self.load_articles)
        self.extract_pdf_button.grid(row=articles_count + 1, column=0)

        self.extract_jpg_button = Button(self.cap_articles_frame, text="Extract JPG", command=self.load_articles)
        self.extract_jpg_button.grid(row=articles_count + 1, column=1)


    def load_articles(self):
        
        cap_number = self.cap_number.get()

        capjournal = CAPJournal(cap_number)
        capjournal.pdf_path = self.cap_pdf_path.get()
        capjournal.pages_path = self.cap_pages_path.get()
        capjournal.year = self.cap_year.get()
        capjournal.month = self.cap_month.cget('text')

        capjournal.load_articles()
        self.cap_articles_frame['text'] = "Articles for issue " + str(cap_number)
        self.make_article_grid(capjournal)

        

    def get_pdf_path(self):
        pdf_path = tkFileDialog.askopenfilename()
        self.cap_pdf_path.delete(0, END)
        self.cap_pdf_path.insert(0, pdf_path)

        
    def get_pages_path(self):
        pages_path = tkFileDialog.askopenfilename()
        self.cap_pages_path.delete(0, END)
        self.cap_pages_path.insert(0, pages_path)
    
    def createWidgets(self):

        LABEL_COL_WIDTH = 10
        INPUT_COL_WIDTH = 10
        CONTROL_ROW = 0

        self.cap_information_frame = LabelFrame(self, text="CAPJournal Information:")
        self.cap_information_frame.grid(row=CONTROL_ROW, column=0)

        self.cap_pdf_label = Label(self.cap_information_frame, text="PDF:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_pdf_label.grid(row=CONTROL_ROW,column=0)

        self.cap_pdf_path = Entry(self.cap_information_frame)
        self.cap_pdf_path.insert(0, "/Users/javier/Workspaces/eso-cap-builder-ve/eso-cap-builder/src/24.pdf")
        self.cap_pdf_path.grid(row=CONTROL_ROW,column=1)

        self.cap_pdf_browse = Button(self.cap_information_frame, text="...", command=self.get_pdf_path)
        self.cap_pdf_browse.grid(row=CONTROL_ROW,column=2)
        
        self.cap_articles_frame = LabelFrame(self, text="Articles for issue ")
        self.cap_articles_frame.grid(row=CONTROL_ROW,column=3)
        
        CONTROL_ROW += 1

        self.cap_pages_label = Label(self.cap_information_frame, text="Pages:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_pages_label.grid(row=CONTROL_ROW,column=0)

        self.cap_pages_path = Entry(self.cap_information_frame)
        self.cap_pages_path.insert(0, "/Users/javier/Workspaces/eso-cap-builder-ve/eso-cap-builder/src/24.txt")
        self.cap_pages_path.grid(row=CONTROL_ROW,column=1)

        self.cap_pages_browse = Button(self.cap_information_frame, text="...", command=self.get_pages_path)
        self.cap_pages_browse.grid(row=CONTROL_ROW,column=2)        
        CONTROL_ROW += 1

        self.cap_number_label = Label(self.cap_information_frame, text="Number:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_number_label.grid(row=CONTROL_ROW,column=0)

        self.cap_number = Entry(self.cap_information_frame)
        self.cap_number.insert(0, 24)
        self.cap_number.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1

        self.cap_year_label = Label(self.cap_information_frame, text="Year:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_year_label.grid(row=CONTROL_ROW,column=0)

        self.cap_year = Entry(self.cap_information_frame)
        self.cap_year.insert(0, self.get_current_year())
        self.cap_year.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1
        
        self.cap_month_label = Label(self.cap_information_frame, text="Month:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_month_label.grid(row=CONTROL_ROW,column=0)
        
        month_list = ('January', 'February', 'March', 'May', 'April', 'June','July',
            'August', 'September', 'October', 'November', 'December')
        
        self.cap_month_options = StringVar()
        self.cap_month_options.set(month_list[self.get_current_month()])
        self.cap_month = OptionMenu(self.cap_information_frame, self.cap_month_options, *month_list)
        self.cap_month.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1

        self.open_finder_button = Button(self.cap_information_frame, text="Load Articles", command=self.load_articles)
        self.open_finder_button.grid(row=CONTROL_ROW,column=3)

        self.QUIT = Button(self, text="Quit", fg="red", command=self.quit)
        self.QUIT.grid(row=CONTROL_ROW,column=0)
        
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()