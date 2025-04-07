users:list[dict]=[
    {'name':'Martyna','location':'Zabki',"posts":5,},
    {'name':'Wiktoria','location':'Radzymin',"posts":10,},
    {'name':'Daria','location':'Losice',"posts":15,}
]


def get_user_info(users_data:list[dict])->None:
    for user in users_data:
        print(f'Twoj znajomy: {user["name"]} z {user["location"]} opublikowal {user["posts"]}')

get_user_info(users)


