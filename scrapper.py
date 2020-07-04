# Written By - Debabrata Panigrahi
# DATE: 5th July 2020
# Code Review Requested.

from scrapers.helpers import Webrequests
from bs4 import BeautifulSoup
import csv


# Get the fashion entity from a database
# Get all the reviews regarding the entity from desired website
# Preprocess and save the same to disc

# testing for a single entity
# TODO: write a function to get the drug name dynamically from a source

def get_all_urls(html):
    """
    gets the url of all the comments in a page
    @params:
    html: BeautifulSoup object
    entity: String
    @returns: list()
    """
    urls = list()
    for title in html.find_all("span", class_="post-title"):
        urls.append(title.a['href'])

    return urls


def get_text_from_url(url):
    """get the text from a given comment url
    @params: url - String (here I assume that it is in the same format as the 'urls' of the return value of get_all_urls
    @returns: String - text corpus
    """
    full_url = "webpage_url" + url
    w = Webrequests()
    raw_html = w.simple_get(full_url)
    html = BeautifulSoup(raw_html, 'html.parser')

    first_content = html.find("span", class_="first_content")
    if first_content is not None:
        first_content_text = first_content.p.text
    else:
        return None

    more_content = html.find("span", class_="more_content")
    if more_content is not None:
        more_content_text = more_content.p.text
    else:
        return None

    return first_content_text + more_content_text


def get_comments(entity):
    """Get the discussions and comments on the website about the given entity
    @params:
        entity - String representing the particular apparel
    @returns:
        list() of all text based comments on the given entity
    """

    w = Webrequests()
    apparel = entity
    url = "" + apparel
    raw_html = w.simple_get(url)
    text_corpus = list()
    if raw_html is not None:
        html = BeautifulSoup(raw_html, 'html.parser')

        # list of all urls that posts titles of the given apparel
        urls = get_all_urls(html)

        for url in urls:
            text = get_text_from_url(url)
            if text is not None:
                text_corpus.append(text)
            else:
                continue
    else:
        # raise an exception if we failed to get any data from url
        raise Exception("Error retrieving contents from {}".format(url))

    return text_corpus


def save_to_disk(text_corpus, entity):
    """save the scrapped text to csv
    @params:
    """
    with open("path", 'a') as file:
        for i in range(len(text_corpus)):
            row = [i, entity, text_corpus[i]]
            writer = csv.writer(file)
            writer.writerow(row)
    file.close()


# Driver Code
apparel_list = ["t-shirt", "saree", "jeans"]
for apparel apparel_list:
    comments = get_comments(apparel)
    save_to_disk(comments, apparel)
