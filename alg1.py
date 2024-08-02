from bs4 import BeautifulSoup

# Path to your HTML file
file_path = "abc.html"

# Open and read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <tr> elements with class 'dxgvDataRow'
rows = soup.find_all('tr', class_='dxgvDataRow')
total= 0
def converta(s):
    if s == 'A+':
        return 4.0
    elif s == 'A':
        return 4.0
    elif s == 'B+':
        return 3.5
    elif s == 'B':
        return 3.0
    elif s == 'C+':
        return 2.5
    elif s == 'C':
        return 2.0
    elif s == 'D+':
        return 1.5
    elif s == 'D':
        return 1.0
    elif s == 'F':
        return 0.0
    else:
        print("err")
        return None  # or you can raise an exception or return a default value

totalCre = 0
# Iterate over the rows and print them
for row in rows:
    credit = 0
    score = 0
    credit = float(row.find_all('td')[3].get_text(strip=True))
    score = converta(row.find_all('td')[4].get_text(strip=True))
    # print(score)
    total += credit*score
    totalCre+=credit

print(total,totalCre)
