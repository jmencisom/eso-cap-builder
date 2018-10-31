class CAPJournal:

    number = 0
    year = 0
    month = ""
    pages = ""
    pdf = ""
    outputpath = ""
    outputpathimages = ""
    
    def __init__(self):
        self.number = 24
        self.year = 2018
        self.month = "October"
        self.pages = "24.txt"
        self.pdf = "24.pdf"
        self.outputpath = "output/" + str(self.number) + "/"
        self.outputpathimages = self.outputpath + "images/"
