import sys
import json
import requests
from bs4 import BeautifulSoup

def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar contribuições: status {response.status_code}")
        
    soup = BeautifulSoup(response.text, "html.parser")
    days = soup.find_all("td", class_="ContributionCalendar-day")
    
    contrib_data = []
    for day in days:
        date = day.get("data-date")
        level = day.get("data-level", "0")
        if date:
            contrib_data.append({
                "date": date,
                "level": int(level)
            })
            
    output_file = "data/contributions.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(contrib_data, f, indent=2)
        
    print(f"Dados de contribuição obtidos ({len(contrib_data)} dias) e salvos em {output_file}")

if __name__ == "__main__":
    username = "LeunamGuilherme"
    fetch_contributions(username)
