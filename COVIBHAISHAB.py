from tkinter import Label

import requests
import bs4
import tkinter as tk
from tkinter import *

def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for block in info_div:

        found_h1 = block.find("h1")
        text = found_h1.get_text() if found_h1 else ""
        found_span = block.find("span", class_=None)
        count = found_span.get_text() if found_span else ""

        all_data = all_data + text + " " + count + "\n"

    return all_data


def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")

    all_data = ""

    for block in info_div:

        found_h1 = block.find("h1")
        text = found_h1.get_text() if found_h1 else ""
        found_span = block.find("span", class_=None)
        count = found_span.get_text() if found_span else ""

        all_data = all_data + text + " " + count + "\n"

    mainLabel['text']=all_data


def reload():
    new_data = get_covid_data()
    mainLabel['text']=new_data


get_covid_data()

root = tk.Tk()
root.geometry("0x0")
root.title("Covid19 update")
f = ("Rockwell", 20, "bold")


banner = tk.PhotoImage(file="COVI-update.png")
bannerLabel: Label = tk.Label(root, image=banner)
bannerLabel.pack()


textfield = tk.Entry(root, width=50)
textfield.pack()


mainLabel = tk.Label(root, text=get_covid_data(), font=f)
mainLabel.pack()

gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=get_country_data)
gbtn.pack()


rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()


root.mainloop()