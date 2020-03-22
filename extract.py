from html.parser import HTMLParser
import sys

holidays = []
file_path = sys.argv[1]
with open(file_path, "r") as html_file:
    my_html = html_file.read()
    html_file.close()


class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.getting = False
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "h4":
            self.getting = True

    def handle_endtag(self, tag):
        if tag == "h4":
            self.getting = False

    def handle_data(self, data):
        if self.getting:
            holidays.append(data + "\n")


parser = MyHTMLParser()
parser.feed(my_html)
with open(file_path, "w") as html_file:
    html_file.writelines(holidays)
