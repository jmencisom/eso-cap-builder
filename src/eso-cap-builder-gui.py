#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
from subprocess import call
import datetime
from CAPJournal import CAPJournal
from CAPArticle import CAPArticle

class Application(Frame):

    def get_current_month(self):
        INDEX_CORRECTION = 1
        now = datetime.datetime.now()
        return now.month - INDEX_CORRECTION

    def get_current_year(self):
        now = datetime.datetime.now()
        return now.year

    
    def make_article_url(self, number, start_page):
        start_page = int(start_page)
        if start_page < 10:
            start_page = "0%s" % str(start_page)
        url = "https://www.capjournal.org/issues/%s/%s_%s.pdf" % (number, number, start_page)
        # print(url)
        return url

    def make_article_grid(self, capjournal):
        
        COL_WIDTH_S = 5
        COL_WIDTH_M = 10
        COL_WIDTH_L = 15
        
        self.cap_article_id_label = Label(self.cap_articles_frame, text="Id", anchor="w", width=COL_WIDTH_S)
        self.cap_article_id_label.grid(row=0, column=0)
        self.cap_article_title_label = Label(self.cap_articles_frame, text="Title", anchor="w", width=COL_WIDTH_M)
        self.cap_article_title_label.grid(row=0, column=1)
        self.cap_article_authors_label = Label(self.cap_articles_frame, text="Authors", anchor="w", width=COL_WIDTH_M)
        self.cap_article_authors_label.grid(row=0, column=2)
        self.cap_article_abstract_label = Label(self.cap_articles_frame, text="Abstract", anchor="w", width=COL_WIDTH_L)
        self.cap_article_abstract_label.grid(row=0, column=3)
        self.cap_article_start_page_label = Label(self.cap_articles_frame, text="Start", anchor="w", width=COL_WIDTH_S)
        self.cap_article_start_page_label.grid(row=0, column=4)
        self.cap_article_end_page_label = Label(self.cap_articles_frame, text="End", anchor="w", width=COL_WIDTH_S)
        self.cap_article_end_page_label.grid(row=0, column=5)
        self.cap_article_url_label = Label(self.cap_articles_frame, text="URL", anchor="w", width=COL_WIDTH_M)
        self.cap_article_url_label.grid(row=0, column=6)
        self.cap_article_pdf_path_label = Label(self.cap_articles_frame, text="PDF", anchor="w", width=COL_WIDTH_M)
        self.cap_article_pdf_path_label.grid(row=0, column=7)


        articles_count = capjournal.get_articles_count()

        self.cap_article_id_label = []
        self.cap_article_title_entry = []
        self.cap_article_authors_entry = []
        self.cap_article_abstract_entry = []
        self.cap_article_start_page_entry = []
        self.cap_article_end_page_entry = []
        self.cap_article_url_entry = []
        self.cap_article_pdf_path_entry = []

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

            url_entry = Entry(self.cap_articles_frame)
            url_entry.grid(row=i+1, column=6)
            cap_number = self.cap_number_entry.get()
            start_page = start_page_entry.get()
            capjournal.articles[i].url = self.make_article_url(cap_number, start_page)
            url_entry.insert(0, capjournal.articles[i].url)
            self.cap_article_url_entry.append(url_entry)

            pdf_path_entry = Entry(self.cap_articles_frame)
            pdf_path_entry.grid(row=i+1, column=7)
            self.cap_article_pdf_path_entry.append(pdf_path_entry)
            

        self.extract_pdf_button = Button(self.cap_articles_frame, text="Extract PDF", command=self.extract_pdf)
        self.extract_pdf_button.grid(row=articles_count + 1, column=0)

        self.extract_jpg_button = Button(self.cap_articles_frame, text="Extract JPG", command=self.extract_jpg)
        self.extract_jpg_button.grid(row=articles_count + 1, column=1)

        self.extract_jpg_button = Button(self.cap_articles_frame, text="Write ADS", command=self.write_ads)
        self.extract_jpg_button.grid(row=articles_count + 1, column=2)

        self.extract_jpg_button = Button(self.cap_articles_frame, text="Get PDF Texts", command=self.get_pdf_text)
        self.extract_jpg_button.grid(row=articles_count + 1, column=3)

        #TODO: Add columns for PDF and JPG


    def make_cap_from_gui(self):
        cap_number = self.cap_number_entry.get()

        cap_journal = CAPJournal(cap_number)
        cap_journal.pdf_path = self.cap_pdf_path_entry.get()
        cap_journal.pages_path = self.cap_pages_path_entry.get()
        cap_journal.year = self.cap_year_entry.get()
        cap_journal.month = self.cap_month.cget('text')

        return cap_journal

    def make_articles_from_gui(self):
        cap_journal = self.make_cap_from_gui()
        cap_journal.articles = [] # prevent index duplication

        articles_count = len(self.cap_article_title_entry)

        # print("articles_count")
        # print(articles_count)
        
        for i in range(articles_count):
            # print(i)
            title = self.cap_article_title_entry[i].get()
            authors = self.cap_article_authors_entry[i].get()
            abstract = self.cap_article_abstract_entry[i].get()
            start_page = self.cap_article_start_page_entry[i].get()
            end_page = self.cap_article_end_page_entry[i].get()
            url = self.cap_article_url_entry[i].get()
            pdf_path = self.cap_article_pdf_path_entry[i].get()
            
            if start_page:
                cap_article = CAPArticle(start_page, end_page)
                cap_article.title = title
                cap_article.authors = authors
                cap_article.abstract = abstract
                # print("start_page")
                # print(start_page)
                cap_article.start_page = int(start_page)
                cap_article.end_page = int(end_page)
                cap_article.url = url
                cap_article.pdf_path = pdf_path
                cap_journal.articles.append(cap_article)

        return cap_journal



    def write_ads(self):
        cap_journal = self.make_articles_from_gui()
        cap_journal.write_ads()

    def extract_pdf(self):

        cap_journal = self.make_articles_from_gui()
        articles_count = cap_journal.get_articles_count()

        for i in range(articles_count):
            cap_journal.write_pdf(i)
            article_pdf_path = cap_journal.articles[i].pdf_path
            self.cap_article_pdf_path_entry[i].insert(0, article_pdf_path)

    def get_pdf_text(self):

        cap_journal = self.make_articles_from_gui()
        articles_count = cap_journal.get_articles_count()

        self.cap_article_title_entry[i].insert(0, "Editorial")
        for i in range(1, articles_count):
            cap_journal.articles[i].set_title()
            article_title = cap_journal.articles[i].title
            self.cap_article_title_entry[i].insert(0, article_title)



    def extract_jpg(self):
        
        cap_journal = self.make_articles_from_gui()
        articles_count = cap_journal.get_articles_count()

        cap_journal.write_jpg_cover()
        
        for i in range(articles_count):
            cap_journal.write_jpg(i)

        

    def load_article_frame(self):
        
        cap_journal = self.make_cap_from_gui()
        
        cap_number = str(cap_journal.number)
        cap_month = cap_journal.month
        cap_year = cap_journal.year

        cap_journal.load_articles()

        self.cap_articles_frame['text'] = "Articles for issue %s - %s %s" % (cap_number, cap_month, cap_year)
        self.make_article_grid(cap_journal)
        

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

        self.cap_pdf_path_entry = Entry(self.cap_information_frame)
        self.cap_pdf_path_entry.insert(0, "/Users/javier/Workspaces/eso-cap-builder-ve/eso-cap-builder/src/24.pdf")
        self.cap_pdf_path_entry.grid(row=CONTROL_ROW,column=1)

        self.cap_pdf_browse = Button(self.cap_information_frame, text="...", command=self.get_pdf_path)
        self.cap_pdf_browse.grid(row=CONTROL_ROW,column=2)
        
        CONTROL_ROW += 1

        self.cap_pages_label = Label(self.cap_information_frame, text="Pages:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_pages_label.grid(row=CONTROL_ROW,column=0)

        self.cap_pages_path_entry = Entry(self.cap_information_frame)
        self.cap_pages_path_entry.insert(0, "/Users/javier/Workspaces/eso-cap-builder-ve/eso-cap-builder/src/24.txt")
        self.cap_pages_path_entry.grid(row=CONTROL_ROW,column=1)

        self.cap_pages_browse = Button(self.cap_information_frame, text="...", command=self.get_pages_path)
        self.cap_pages_browse.grid(row=CONTROL_ROW,column=2)        
        CONTROL_ROW += 1

        self.cap_number_label = Label(self.cap_information_frame, text="Number:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_number_label.grid(row=CONTROL_ROW,column=0)

        self.cap_number_entry = Entry(self.cap_information_frame)
        self.cap_number_entry.insert(0, 24)
        self.cap_number_entry.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1

        self.cap_year_label = Label(self.cap_information_frame, text="Year:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_year_label.grid(row=CONTROL_ROW,column=0)

        self.cap_year_entry = Entry(self.cap_information_frame)
        self.cap_year_entry.insert(0, self.get_current_year())
        self.cap_year_entry.grid(row=CONTROL_ROW,column=1)
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

        self.load_articles_button = Button(self.cap_information_frame, text="Load Articles", command=self.load_article_frame)
        self.load_articles_button.grid(row=CONTROL_ROW,column=1)

        self.cap_articles_frame = LabelFrame(self, text="Articles for issue ")
        self.cap_articles_frame.grid(row=0, column=1)

        self.QUIT = Button(self, text="Quit", fg="red", command=self.quit)
        self.QUIT.grid(row=3, column=0)
        
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()