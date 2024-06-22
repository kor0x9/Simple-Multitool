import requests
from bs4 import BeautifulSoup
import webbrowser

def recherche_discord_id(id_discord):
    # Recherche sur Discord
    url_discord = f"https://discord.com/users/{id_discord}"
    response_discord = requests.get(url_discord)
    soup_discord = BeautifulSoup(response_discord.text, 'html.parser')
    results_discord = soup_discord.find_all('div', class_='username')

    # Résultats de recherche
    print(f"Résultats de la recherche pour l'ID Discord {id_discord} :")
    print("")

    # Discord
    print("Discord :")
    for result in results_discord:
        username = result.text
        print(f"  - Pseudo : {username}")

    # Recherche sur les réseaux sociaux
    print("\nRéseaux sociaux :")
    instagram_url = f"https://www.instagram.com/{username}/" if username else ""
    snapchat_url = f"https://www.snapchat.com/add/{username}" if username else ""
    facebook_url = f"https://www.facebook.com/{username}" if username else ""
    print(f"  - Instagram : {instagram_url}")
    print(f"  - Snapchat : {snapchat_url}")
    print(f"  - Facebook : {facebook_url}")

    # Ouvrir les résultats dans les navigateurs
    webbrowser.open(url_discord)
    if instagram_url:
        webbrowser.open(instagram_url)
    if snapchat_url:
        webbrowser.open(snapchat_url)
    if facebook_url:
        webbrowser.open(facebook_url)

def recherche_amis(nom, prenom):
    # Recherche sur Google
    url_google = f"https://www.google.fr/search?q={nom}+{prenom}"
    response_google = requests.get(url_google)
    soup_google = BeautifulSoup(response_google.text, 'html.parser')
    results_google = soup_google.find_all('div', class_='g')

    # Recherche sur Bing
    url_bing = f"https://www.bing.com/search?q={nom}+{prenom}"
    response_bing = requests.get(url_bing)
    soup_bing = BeautifulSoup(response_bing.text, 'html.parser')
    results_bing = soup_bing.find_all('li', class_='b_algo')

    # Recherche sur DuckDuckGo
    url_duckduckgo = f"https://duckduckgo.com/html?q={nom}+{prenom}"
    response_duckduckgo = requests.get(url_duckduckgo)
    soup_duckduckgo = BeautifulSoup(response_duckduckgo.text, 'html.parser')
    results_duckduckgo = soup_duckduckgo.find_all('a', class_='result__a')

    # Recherche sur StartPage
    url_startpage = f"https://www.startpage.com/do/search?q={nom}+{prenom}"
    response_startpage = requests.get(url_startpage)
    soup_startpage = BeautifulSoup(response_startpage.text, 'html.parser')
    results_startpage = soup_startpage.find_all('div', class_='result')

    # Résultats de recherche
    print(f"Résultats de la recherche pour {nom} {prenom} :")
    print("")

    # Google
    print("Google :")
    for result in results_google:
        title = result.find('h3').text
        link= result.find('a')['href']
        print(f"  - {title} ({link})")

    # Bing
    print("\nBing :")
    for result in results_bing:
        title = result.find('h2').text
        link = result.find('a')['href']
        print(f"  - {title} ({link})")

    # DuckDuckGo
    print("\nDuckDuckGo :")
    for result in results_duckduckgo:
        title = result.text
        link = result['href']
        print(f"  - {title} ({link})")

    # StartPage
    print("\nStartPage :")
    for result in results_startpage:
        title = result.find('h2').text
        link = result.find('a')['href']
        print(f"  - {title} ({link})")

    # Recherche sur les réseaux sociaux
    print("\nRéseaux sociaux :")
    instagram_url = f"https://www.instagram.com/{nom}{prenom}/"
    snapchat_url = f"https://www.snapchat.com/add/{nom}{prenom}"
    facebook_url = f"https://www.facebook.com/{nom}.{prenom}"
    print(f"  - Instagram : {instagram_url}")
    print(f"  - Snapchat : {snapchat_url}")
    print(f"  - Facebook : {facebook_url}")

    # Ouvrir les résultats dans les navigateurs
    webbrowser.open(url_google)
    webbrowser.open(url_bing)
    webbrowser.open(url_duckduckgo)
    webbrowser.open(url_startpage)

def recherche_amis_pseudo(pseudo):
    # Recherche sur les réseaux sociaux
    instagram_url = f"https://www.instagram.com/{pseudo}/"
    snapchat_url = f"https://www.snapchat.com/add/{pseudo}"
    facebook_url = f"https://www.facebook.com/{pseudo}"
    print(f"Résultats de la recherche pour {pseudo} :")
    print("")
    print(f"  - Instagram : {instagram_url}")
    print(f"  - Snapchat : {snapchat_url}")
    print(f"  - Facebook : {facebook_url}")

    # Ouvrir les résultats dans les navigateurs
    webbrowser.open(instagram_url)
    webbrowser.open(snapchat_url)
    webbrowser.open(facebook_url)

def main():
    while True:
        print("\nOptions de recherche :")
        print("1. Rechercher par pseudo Discord")
        print("2. Rechercher par ID Discord")
        print("3. Rechercher par nom et prénom")
        print("4. Retour")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            pseudo = input("Entrez le pseudo Discord de votre ami : ")
            recherche_discord(pseudo)
        elif choix == "2":
            id_discord = input("Entrez l'ID Discord de votre ami : ")
            recherche_discord_id(id_discord)
        elif choix == "3":
            nom = input("Entrez le nom de votre ami : ")
            prenom = input("Entrez le prénom de votre ami : ")
            recherche_amis(nom, prenom)
        elif choix == "4":
            return
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()