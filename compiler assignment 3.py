
from xml.dom import minidom
import openpyxl

doc = minidom.parse("compiler.xml")

books = doc.getElementsByTagName("book")
for book in books:
    book_id = book.getAttribute("id")
    author = book.getElementsByTagName("author")[0]
    title = book.getElementsByTagName("title")[0]
    genre = book.getElementsByTagName("genre")[0]
    price = book.getElementsByTagName("price")[0]
    publish_date = book.getElementsByTagName("publish_date")[0]
    description = book.getElementsByTagName("description")[0]
    print("id: % s\nauthor: % s\ntitle: % s\ngenre: % s\nprice: % s\npublish_date: % s\ndescription: % s\n\n" %
          (book_id, author.firstChild.data, title.firstChild.data, genre.firstChild.data, price.firstChild.data, publish_date.firstChild.data, description.firstChild.data))
