import requests
from bs4 import BeautifulSoup

# Send a GET request to the Open Litter Map website
response = requests.get("https://openlittermap.com/")

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the desired elements and extract the data
data_elements = soup.find_all("div", class_="data-element")

# Iterate over the data elements and extract the relevant information
for element in data_elements:
    name = element.find("h3").text
    value = element.find("p").text

    print(f"{name}: {value}")
