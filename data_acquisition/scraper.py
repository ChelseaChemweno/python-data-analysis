import requests #requests library , which allows your python script to make HTTP Requests (like fetching webpagee)
from bs4 import BeautifulSoup #Imprts BeautifulSoup class from beautifulsoup4 library (It is used to parase html and xml documents , making it easy to navigateand extract data from them )
import csv #tools for working with csv files 

url = "http://books.toscrape.com/" # Replace with the actual URL

try:
    response = requests.get(url) #sends a http get request to the url stored in the URL(Thereafter the response from the server is stored in the response variable)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    soup = BeautifulSoup(response.content, "html.parser")

    books = [] # An empty list that is used to store the scrapped book data (title ad price)

    # Find the book items (This part depends on the website's HTML)
    # Example:
    book_items = soup.find_all("article", class_="product_pod")
    #this is used to find all the html articles wlwmwnts with the class attribute product_pod

    for item in book_items:
        try:
            a_tag =item.find("h3").find("a")
            if a_tag: #check if <a> tag exists
                title= a_tag["title"].strip()
                price = item.find("p",class_ ="price_color").text.strip()
                books.append({"title": title ,"price":price}) # creates a dictionary containingthe books#s title and adds it to the books list
        except AttributeError:
            # Handle missing data (if the find metjod doesnot catch the expected element)
            print("Missing data for a business item.")

    # Save the data to a CSV file.
    with open("data/books.csv", "w", newline="", encoding="utf-8") as csvfile:#opens a file named books.csv in write mood . The new line prevents extra blank lines from being added to CSV file . The encoding ensures that the file is encoded using utf-8
        fieldnames = ["title", "price"]  # Adjust fields as needed
       #creates a list nnames filednames containinng column heads for the CSV file 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #creates a csv.discWriter object , which is used to write dictionaries to the CSV file 
        writer.writeheader()# writes the header row to the csv file
        for book in books:
            writer.writerow(book) # writes the current book data to csv file 

    print("Data scraped and saved to data/businesses.csv")
# prints out that the data was scrapped succesfully
except requests.exceptions.RequestException as e:#begins an except block that catcher exceptions related to the requestd library (network errors , invalid urls)
    print(f"Error fetching URL: {e}") # capture error mesage ifa request exception occurs
except Exception as e:
    print(f"An error occurred: {e}")