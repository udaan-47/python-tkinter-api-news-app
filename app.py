from tkinter import *
import requests


class News:

    def __init__(self):
        self.root = Tk()

        self.root.title("News Application")
        self.root.minsize(900, 500)
        self.root.maxsize(900, 500)

        self.root.configure(background="white")

        self.label = Label(self.root, text="Apnanewz 24*7", bg="#fff")
        self.label.configure(font=("Times", 30, "bold"))
        self.label.pack(pady=(30, 30))

        self.label1 = Label(self.root, text="Enter the topic", bg="#fff")
        self.label1.configure(font=("Times", 15, "bold"))
        self.label1.pack(pady=(10, 20))

        self.topic = Entry(self.root)
        self.topic.pack(pady=(5, 10), ipadx=30, ipady=3)

        self.click = Button(self.root, text="search", bg="#000", fg="#fff", command=lambda: self.fetch())
        self.click.pack(pady=(5, 5))

        self.root.mainloop()

    def fetch(self):
        term = self.topic.get()  # fetch the search term

        url = "https://newsapi.org/v2/everything?q={}&apiKey=28d624ac06c1485ea9b8afe370e61490".format(term)

        response = requests.get(url)  # hit the api
        self.response = response.json()
        self.data=self.response['articles']
        self.extract()

    def extract(self,index=0):
        news = []
        news.append(self.data[index]['title'])
        news.append(self.data[index]['source']['name'])
        news.append(self.data[index]['description'])

        self.clear()
        self.display(news,index=index)

    def display(self,news,index):
        title = Label(self.root,text=news[0],fg="#000",bg="#fff")
        title.pack()

        source = Label(self.root,text=news[1],fg="#000",bg="#fff")
        source.pack()

        desc = Label(self.root,text=news[2],fg="#000",bg="#fff")
        desc.pack()

        frame=Frame(self.root)
        frame.pack()
        if index!=0:
            previous=Button(frame, text="Previous",command=lambda: self.extract(index=index-1))
            previous.pack(side='left')

        if index!=19:
            next = Button(frame, text="Next",command=lambda: self.extract(index=index+1))
            next.pack(side='right')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


obj = News()
