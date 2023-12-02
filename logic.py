from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]["home"]["front_default"])
        else:
            return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fanime-characters-fight.fandom.com%2Fru%2Fwiki%2F%25D0%259F%25D0%25B8%25D0%25BA%25D0%25B0%25D1%2587%25D1%2583_%25D0%25AD%25D1%2588%25D0%25B0&psig=AOvVaw1yfsbUcodkdWoOg2xezxA5&ust=1701087338889000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKjpq6bS4YIDFQAAAAAdAAAAABAE"

    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



