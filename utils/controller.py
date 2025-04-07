def get_user_info(users_data:list[dict])->None:
    for user in users_data:
        print(f'Twoj znajomy: {user["name"]} z {user["location"]} opublikowal {user["posts"]}')