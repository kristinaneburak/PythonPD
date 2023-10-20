import os
import requests
import time
import cloudscraper
from bs4 import BeautifulSoup

user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36"
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    ]

def save_reviews(a, agentIndex):
    base_url = f"https://www.kinopoisk.ru/film/535341/reviews/"

    
    folder_path = f"dataset/"
    os.makedirs(folder_path, exist_ok=True)
    exitFlag = False
    agentIndex = 0
    
    scraper = cloudscraper.create_scraper()
    
    for page in range(1, 10 + 1):
        if exitFlag:
            return
        url = base_url + str(page)
        
        try:
            response = scraper.get(url, headers={"User-Agent":user_agents[agentIndex]})
            if response.status_code != 200:
                print(response.text)
            
            while 'captcha' in response.url and agentIndex < user_agents.count():
                agentIndex += 1
                response = scraper.get(url, headers={"User-Agent":user_agents[agentIndex]})
                input()

            soup = BeautifulSoup(response.text, 'html.parser')
            reviews = soup.find_all('div', class_='brand_words')
            
            if reviews.__len__() == 0:
                exitFlag = True
            for i, review in enumerate(reviews):
                review_text = review.get_text(strip=True)
                movie_name = soup.title.text.split('—')[0].strip()
                
                
                file_number = str(i).zfill(4)
                
                
                with open(f"{folder_path}/{file_number}.txt", 'w', encoding='utf-8') as file:
                    file.write(f"Название фильма: {movie_name}\n")
                    file.write(review_text)
                    
                time.sleep(100) 
        
        except Exception as e:
            print("Ошибка при запросе страницы:", e)


save_reviews("", 0)
