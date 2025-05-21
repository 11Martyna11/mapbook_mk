import requests
import folium
from bs4 import BeautifulSoup

users: list[dict] = [
    {'name': 'Kinga', 'location': 'Kozienice', 'posts': 500, },
    {'name': 'Wika', 'location': 'Radzyń Podlaski', 'posts': 400, },
    {'name': 'Daria', 'location': 'Łosice', 'posts': 200, }
]
def get_coordinates(location_name:str)->list:
    adres_url:str=f'https://pl.wikipedia.org/wiki/{ location_name}'
    response_html=BeautifulSoup(requests.get(adres_url).text, 'html.parser')
    # print(longitude)
    # print(latitude)
    return [
        float(response_html.select('.latitude')[1].text.replace(',','.')),
        float(response_html.select('.longitude')[1].text.replace(',', '.')),

    ]

coordinates:list=get_coordinates('Kozienice')
map=folium.Map(location=coordinates, zoom_start=6,tiles='OpenStreetMap')
for user in users:
    folium.Marker(
        location=get_coordinates(user ['location']),
        popup=f'<h5>{user['location']}</h5><br/>{user['name']}<br/>{user['posts']}'
    ).add_to(map)
map.save('mapa.html')