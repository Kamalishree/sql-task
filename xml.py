from bs4 import BeautifulSoup
xml_data = """
<library>
    <book>
        <title>Python Basics</title>
        <author>Kamali</author>
        <year>2024</year>
    </book>
    <book>
        <title>Data Science Essentials</title>
        <author>Ravi</author>
        <year>2023</year>
    </book>
</library>
"""

#Parse the XML using BeautifulSoup
soup = BeautifulSoup(xml_data, "xml")

#Extract all books and display info
books = soup.find_all("book")

print("Library Book List:\n")
for book in books:
    title = book.find("title").text
    author = book.find("author").text
    year = book.find("year").text
    print(f"Title: {title}\nAuthor: {author}\nYear: {year}\n")
