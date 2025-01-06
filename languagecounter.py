import requests
from collections import Counter

# Substitua 'SeuNome' pelo seu nome de usuário do GitHub
username = 'SeuNome'
url = f'https://api.github.com/users/SeuNome/repos'

response = requests.get(url)
repos = response.json()

languages = []

for repo in repos:
    if repo['language']:
        languages.append(repo['language'])

language_count = Counter(languages)

for language, count in language_count.items():
    print(f'{language}: {count}')
