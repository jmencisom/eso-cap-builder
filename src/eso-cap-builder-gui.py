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

    
    def load_articles(self):
        cap = CAPJournal()
        cap.pdf = self.cap_pdf_path.get()
        cap.pages = self.cap_pages_path.get()
        cap.number = self.cap_number.get()
        cap.year = self.cap_year.get()
        cap.month = self.cap_month.cget('text')

        self.cap_articles_frame['text'] = "Articles for issue " + str(cap.number)
        self.cap_articles_frame_entry.delete(0, END)
        self.cap_articles_frame_entry.insert(0, cap.number)
        # call(["open", "."])

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

        self.cap_pdf_label = Label(self, text="PDF:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_pdf_label.grid(row=CONTROL_ROW,column=0)
        self.cap_pdf_path = Entry(self)
        self.cap_pdf_path.grid(row=CONTROL_ROW,column=1)
        self.cap_pdf_browse = Button(self, text="...", command=self.get_pdf_path)
        self.cap_pdf_browse.grid(row=CONTROL_ROW,column=2)
        self.cap_articles_frame = LabelFrame(self, text="Articles for issue ")
        self.cap_articles_frame.grid(row=CONTROL_ROW,column=3)
        self.cap_articles_frame_entry = Entry(self.cap_articles_frame)
        self.cap_articles_frame_entry.pack()
        CONTROL_ROW += 1

        self.cap_pages_label = Label(self, text="Pages:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_pages_label.grid(row=CONTROL_ROW,column=0)
        self.cap_pages_path = Entry(self)
        self.cap_pages_path.grid(row=CONTROL_ROW,column=1)
        self.cap_pages_browse = Button(self, text="...", command=self.get_pages_path)
        self.cap_pages_browse.grid(row=CONTROL_ROW,column=2)        
        CONTROL_ROW += 1

        self.cap_number_label = Label(self, text="Number:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_number_label.grid(row=CONTROL_ROW,column=0)
        self.cap_number = Entry(self)
        self.cap_number.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1

        self.cap_year_label = Label(self, text="Year:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_year_label.grid(row=CONTROL_ROW,column=0)
        self.cap_year = Entry(self)
        self.cap_year.insert(END, self.get_current_year())
        self.cap_year.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1
        
        self.cap_month_label = Label(self, text="Month:", anchor="w", width=LABEL_COL_WIDTH)
        self.cap_month_label.grid(row=CONTROL_ROW,column=0)
        
        month_list = ('January', 'February', 'March', 'May', 'April', 'June','July',
            'August', 'September', 'October', 'November', 'December')
        
        self.cap_month_options = StringVar()
        self.cap_month_options.set(month_list[self.get_current_month()])
        self.cap_month = OptionMenu(self, self.cap_month_options, *month_list)
        self.cap_month.grid(row=CONTROL_ROW,column=1)
        CONTROL_ROW += 1

        self.open_finder_button = Button(self, text="Load Articles", command=self.load_articles)
        self.open_finder_button.grid(row=CONTROL_ROW,column=1)

        self.QUIT = Button(self, text="Quit", fg="red", command=self.quit)
        self.QUIT.grid(row=CONTROL_ROW,column=2)
        
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()