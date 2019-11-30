from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.talgov.com/animals/kennel-dogs.aspx').text
soup = BeautifulSoup(source, 'lxml')
pets = soup.find('table', class_='table_data')
pet_data = pets.tbody.find('td', valign='top')
pet_description = str(pet_data).split('<br/>')[1]
parsebycommas = pet_description.split(',')
parsebyspace = parsebycommas[0].split(' ')
sex = parsebyspace[len(parsebyspace) - 1]
spayed = parsebyspace[len(parsebyspace) - 2]
breed = parsebycommas[1].split('.')[0][1:]
color = parsebycommas[1].split('generally ')[1].split(' in')[0]
pet_name_text = pet_data.strong.text.split('-')[0]
petid_text = pet_data.strong.text.split('-')[1]
pet_name = pet_name_text[0:len(pet_name_text)]
petid = petid_text[1:len(petid_text)+1]
pet_image_link = 'http://www.petharbor.com:80/get_image.asp?RES=thumb&ID=' + str(petid) + '&LOCATION=TLLS'

print(pet_description)

