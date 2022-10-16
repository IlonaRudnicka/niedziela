import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#PARAMETRY TESTU
caps={}
caps['browserName']= 'edge'

GRID_HUB_URL = "http://127.0.0.1/wd/hub"

# DANE TESTOWE
haslo = "DSfbv76564@@@"

class RejestracjaNowegoUzytkownika(unittest.TestCase):
    def setUp(self):
        # WARUNKI WSTĘPNE
        # 1. Otwarta strona główna
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.EDGE)
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")
        # (2. Użytkownik niezalogowany)
        # Zamknij alert o ciasteczkach
        self.driver.find_element(By.CLASS_NAME, "e-button--type-primary.e-button--color-brand.e-consents-alert__button.e-button").click()

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testBrakPodaniaImienia(self):
        sleep(5)
        # 1. Kliknij „Zarejestruj”
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zarejestruj").click()
        # 2.Wpisz nazwisko
        nazwisko = self.driver.find_element(By.ID, "lastname")
        nazwisko.send_keys("Nowak")
        # 3. Wpisz adres e-mail
        adres_mail = self.driver.find_element(By.ID, "email_address")
        adres_mail.send_keys("jannowak12341234@gmail.com")
        # 4. Wpisz hasło (co najmniej 6 znaków)
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(haslo)
        # 5. Wpisz ponownie hasło w celu potwierdzenia
        passwordconf = self.driver.find_element(By.ID, "confirmation")
        passwordconf.send_keys(haslo)
        # 6. Zaznacz „Oświadczam, że zapoznałem się z treścią Regulaminu serwisu i akceptuję
        # jego postanowienia.”
        self.driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
        # OSTROŻNIE!!!!
        # 7. Kliknij „Załóż nowe konto” (tylko dla przypadków niegatywnych!)
        self.driver.find_element(By.XPATH, '//button[@data-testid="register-create-account-button"]').click()


        sleep(4)

# Jeśli uruchamiam z tego pliku
if __name__ == '__main__':
    # to uruchom testy
    unittest.main()

