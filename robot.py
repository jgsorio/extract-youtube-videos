from selenium import webdriver
import time

class YoutubeRobot:
    def __init__(self):
        self.pages = 5
        self.search_term = input("Enter the search term: ")
        self.driver = webdriver.Chrome()
        self.search(self.search_term)
        time.sleep(2)
        self.get_results()


    def search(self, term):
        url = f"https://www.youtube.com/results?search_query={term}"
        self.driver.get(url)

    
    def get_results(self):
        page = 1
        while page < self.pages:
            links = self.driver.find_elements(by='id', value='video-title')
            for link in links:
                with open('./videos.txt', 'a', encoding='utf-8') as f:
                    if link.get_attribute('href') != None:
                        f.write(link.text + '\n' + ' - ' + str(link.get_attribute('href')) + '\n')
                        f.close()
                    continue
            page += 1
            self.next_page(page)
        print('concluindo....')


    def next_page(self, page):
        self.driver.execute_script(f"window.scrollTo(0, {page*10000})")
        time.sleep(2)

YoutubeRobot()