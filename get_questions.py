from selenium import webdriver
from sys import argv
from time import sleep
from lib_mailer.lib_mailer import send_email

# Constants
DRIVER = webdriver.Chrome()
BASE_URL = "https://www.hackerrank.com/"
EMAIL = "<YOUR HACKERRANK EMAIL>"
PASSWORD = "<YOUR HACKERRANK PASSWORD>"
QUESTION_COUNT = argv[2]
TOPICS = argv[3:]


if not QUESTION_COUNT or not TOPICS:
    print("Usage: python3 get_question.py <number of questions to send> <Topics>")


def login():
    login_url = f"{BASE_URL}auth/login"
    DRIVER.get(login_url)
    email_field = DRIVER.find_element_by_id('input-1')
    email_field.send_keys(EMAIL)
    password_field = DRIVER.find_element_by_id("input-2")
    password_field.send_keys(PASSWORD)
    login_btn = DRIVER.find_element_by_xpath('//*[@id="tab-1-content-1"]/div[1]/form/div[4]/button')
    login_btn.click()


def get_question():
    questions = {}
    question_base_url = f"{BASE_URL}domains/"
    for topic in TOPICS:
        topic_url = f"{question_base_url}{topic}?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bdifficulty%5D%5B%5D=easy"
        DRIVER.get(topic_url)
        sleep(5)
        question_tiles = DRIVER.find_elements_by_xpath('//*/div[@class="challenges-list"]/a[@class="js-track-click challenge-list-item"]')
        question_tiles = question_tiles[:QUESTION_COUNT]
        questions[topic] = [x.get_attribute('href') for x in question_tiles]

    return questions


def run():
    login()
    sleep(5)
    q_dict = get_question()
    send_email(questions_dict=q_dict)
    DRIVER.quit()


if __name__ == "__main__":
    run()
