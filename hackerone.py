from bs4 import BeautifulSoup

f = open('hacktivity')
html = f.read()
f.close()

try:
    f = open('./data.txt')
    data = f.read()
except: 
    data = '0'
f.close()


soup = BeautifulSoup(html, 'html.parser')
reports_resolved = soup.find(string='Reports resolved').find_next('span').text
if int(data) != int(reports_resolved):
    to_gen = int(reports_resolved) - int(data)
    print(str(to_gen) + " new reports.")
else:
    print("No new reports.")
    exit (-1)

hacktivity = []
for div in soup.find_all('div'):
    if to_gen == 0:
        break
    try:
        if div.get('class')[0] == 'daisy-helper-text':
            if div.parent.text.find('By') != -1:
                hacktivity.append(div.parent.text)
                to_gen = to_gen - 1
    except:
        continue

f = open("./data.txt", "w")
f.write(reports_resolved)
f.close()

f = open("./commit-message.txt", "w")
for activity in hacktivity:
    message = 'New report disclosed ' + activity + '\n'
    f.write(message)

f.write("[SKIP CI]")
f.close()
