html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>html demo</title>
</head>
<body>
    <h1 id="Header">  demo v1  </h1>
    <div class = "Group 1">
        <h2>
            programlama
        </h2>
        <ul>
            <li> menü 1 </li>
            <li> menü 2 </li> 
            <li> menü 3 </li>
        </ul>
    </div>
    <div class = "Group 2">
        <h2>
            modüller
        </h2>
        <ul>
            <li> menü 1 </li>
            <li> menü 2 </li> 
            <li> menü 3 </li>
        </ul>
    </div>

</body>
</html>


"""
from unittest import result
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify() #düzenleme işlemi
result = soup.title
result = soup.head

result = soup.title.name
result = soup.title.string
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()


print(result)

