users:list[dict]=[
    {'name':'Martyna','location':'Zabki',"posts":5,},
    {'name':'Wiktoria','location':'Radzymin',"posts":10,},
    {'name':'Daria','location':'Losice',"posts":15,}
]

for user in users:
    print(f'Twoj znajomy: {user["name"]} z {user["location"]} opublikowal {user["posts"]}')




