
import requests
r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
json = r.json()

char_list = ['Hulk', 'Captain America', 'Thanos']
char_lst_2 = []
stats = []
lst_int = []

for char in char_list:
    for i in json:
        if i['name'] == char:
            char_lst_2.append(i)

for g in char_lst_2:
    for i in g:
        if i  == 'powerstats':
            stats.append(g[i])

for g in stats:
    for i in g:
        if i == 'intelligence':
            lst_int.append(g[i])

final_lst = list(zip(char_list, lst_int))
int = 0

for i, g  in final_lst:
    if g >= int:
        int = g

for i, g in final_lst:
    if g == int:
        print(i)