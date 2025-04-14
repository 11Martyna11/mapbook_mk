users:list[dict]=[
    {'name':'Martyna','location':'Zabki',"posts":5,},
    {'name':'Wiktoria','location':'Radzymin',"posts":10,},
    {'name':'Daria','location':'Losice',"posts":15,}
]


def update_user(users_data:list[dict]) -> None:
    user_name=input('podaj imię użytkownika do zmodyfikowania: ')
    for user in users_data:
        if user['name'] == user_name:

            user['name'] = input('Podaj nowe imię: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj nową liczbę postów: ')

update_user(users)
print(users)
