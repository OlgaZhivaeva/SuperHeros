class SuperHero:
    def __init__(self, id):
        self.id = id
    def get_intelligence(self):
        """Метод возвращает значение intelligence"""
        url_to_request = BASEURL + f'/powerstats/{self.id}.json'
        response = requests.get(url=url_to_request)
        return response.json()['intelligence']

if __name__ == '__main__':
    import requests
    BASEURL = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    hulk = SuperHero('332')
    thanos = SuperHero('655')
    cap_am = SuperHero('149')
    hulk_int = hulk.get_intelligence()
    thanos_int = thanos.get_intelligence()
    cap_am_int = cap_am.get_intelligence()
    print(f'Hulk intelligence {hulk_int}')
    print(f'Thanos intelligence {thanos_int}')
    print(f'Captain America intelligence {cap_am_int}')

