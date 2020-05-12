from bs4 import BeautifulSoup

f = open('hacktivity')
html = f.read()
f.close()

try:
    f = open('hacktivity_old')
    data = f.read()
except: 
    data = '0'
f.close()


soups = []
soups.append(BeautifulSoup(html, 'html.parser'))
soups.append(BeautifulSoup(data, 'html.parser'))

reports_resolved = []
for soup in soups:
    reports_resolved.append(int(soup.find(string='Reports resolved').find_next('span').text))

hacktivity_l = []
for soup in soups:
    hacktivity = []
    for div in soup.find_all('div'):
        try:
            if div.get('class')[0] == 'daisy-helper-text':
                if div.parent.text.find('By') != -1:
                    hacktivity.append(div.parent.text)
        except:
            continue
    hacktivity_l.append(hacktivity)

if reports_resolved[0] != reports_resolved[1]:
    to_gen = reports_resolved[0] - reports_resolved[1]

elif hacktivity_l[0] != hacktivity_l[1]:
    from collections import Counter
    c1 = Counter(hacktivity_l[0])
    c2 = Counter(hacktivity_l[1])
    diff = c2 - c1
    to_gen = len(list(diff.elements()))

else:
    print("No new reports.")
    exit (-1)

print(str(to_gen) + " new reports.")

f = open("./hacktivity_old", "w")
f.write(hacktivity_l[0])
f.close()

f = open("./commit-message.txt", "w")
for i in range(to_gen):
    if hacktivity_l[0][i]:
        message = 'New report disclosed ' + hacktivity_l[0][i] + '\n'
        f.write(message)

f.write("[SKIP CI]") 
f.close()
