from bs4 import BeautifulSoup

with open('sample_xml_file.xml', 'r') as f:
    data = f.read()

print(data)

print("============================================================================")
soup = BeautifulSoup(data, 'xml')
# print(soup.prettify())

food_name_tag = soup.find('name', string='Belgian Waffles')
food_item = food_name_tag.findParent('food')
# print(food_item.prettify())
# print(food_item)

food_items = soup.find_all('food')
for item in food_items:
    print(item.prettify())

food_items = soup.find_all('name')
for item in food_items:
    print(item.prettify())

food_name = soup.find('name').get_text()
print(food_name)

food_item.price.string = '$6.5'
print(food_item.prettify())

food_name_tag = soup.find('name', string='Homestyle Breakfast')
food_item = food_name_tag.findParent('food')
food_item.decompose()
with open('updated_sample_xmlfile.xml', 'w') as f:
    f.write(str(soup))

