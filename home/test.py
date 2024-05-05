from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

driver = webdriver.Chrome()

class Historia(LiveServerTestCase):
    driver.get("http://127.0.0.1:8000")