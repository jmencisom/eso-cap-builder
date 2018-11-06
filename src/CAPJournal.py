from CAPArticle import CAPArticle

class CAPJournal:

    number = 0
    year = 0
    month = ""
    pages_path = ""
    pdf_path = ""
    outputpath = ""
    outputpathimages = ""
    articles = []
    
    def __init__(self, number):
        self.number = number
        self.outputpath = "output/" + str(self.number) + "/"
        self.outputpathimages = self.outputpath + "images/"

    
    def add_articles(self):
        openfile = open(self.pages_path, 'r')
        for row in openfile:
            start_page, end_page = row.strip().split(',')
            # print("--")
            # print(start_page)
            # print(end_page)
            cap_article = CAPArticle(start_page, end_page)
            self.articles.append(cap_article)

    def get_articles_count(self):
        self.add_articles()
        return len(self.articles)


    



