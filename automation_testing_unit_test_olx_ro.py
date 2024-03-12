# import modulele necesare
import time
import unittest  #Importă modulul pentru crearea și rularea de teste
from selenium import webdriver  # Importă modulul pentru interacțiunea cu browserele web
from selenium.common.exceptions import NoSuchElementException  #Importă clasa pentru gestionarea excepției când un element nu este găsit
from selenium.webdriver.common.by import By


# definesc clasa de test pentru pagina principală OLX
class OLXHomePageTests(unittest.TestCase):

    # setUp se va executa înaintea fiecărui test
    def setUp(self):
        self.driver = webdriver.Chrome()  # initiez driverul de Chrome
        self.driver.get("https://www.olx.ro/")  # deschid pagina principală OLX
        self.driver.maximize_window() #maximizez ecranul
        #acceptam modulele "Cookies": css.BY id="onetrust-accept-btn-handler"
        self.driver.find_element(By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]').click()
        #configuram wait-ul implicit
        self.driver.implicitly_wait(3)

    # tearDown se va executa dupa fiecare test
    def tearDown(self):
        self.driver.quit()  # închid browserul

    #  test pentru verificarea titlului paginii
    def test_Title(self):
        title = self.driver.title  # obținem titlul paginii
        self.assertEqual(title, "Anunturi Gratuite - Peste 4 milioane anunturi - OLX.ro")  # verificăm dacă titlul este cel asteptat

    # test pentru căutarea unui produs
    def test_Search(self):
        time.sleep(2)
        search_box = self.driver.find_element(By.ID, "search")  # Gasesc box-ul de cautare dupa id
        search_box.send_keys("bicicleta")  # Introduc textul "bicicleta" in campul de cautare
        time.sleep(2)
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="searchBtn"]') # Caut butonul de cautare folosind un CSS Selector care filtreaza dupa 'Tag button" si valoare atribut: name="searchBtn"
        search_button.click()  # Dau click pe butonul de căutare
        time.sleep(2)
        self.assertTrue("bicicleta" in self.driver.current_url)  # Verific dacă URL-ul contine cuvantul cautat


    # Test pentru verificarea accesului la pagina de autentificare
    def test_AccessLoginPage(self):
        login_button = self.driver.find_element (By.CLASS_NAME,"css-12l1k7f")  # Gasesc butonul de login dupa clasa
        time.sleep(4)
        login_button.click()  # Dau click pe butonul de login
        time.sleep(3)
        self.assertIn("login", self.driver.current_url)  # Verific daca am fost redirecționat pe pagina de login care conține "login" în URL

        # Test pentru verificarea existentei butonului "Adauga anunt nou"
    def test_SellButtonExists(self):
        try:
            sell_button = self.driver.find_element (By.CLASS_NAME, "css-2txnih")  # Incerc sa gasesc butonul de "Adauga anunt nou"
            exists = True
        except NoSuchElementException: # NoSuchElementException este folosit pentru a intercepta cazul în care un element nu este gasit. si este deja importata
            exists = False
        self.assertTrue(exists)  # assert ca butonul de "Adauga anunt nou" exista

        # Test pentru adaugare anunt fara a fi logat
    def test_AddAdWithoutLogin(self):
        sell_button = self.driver.find_element(By.CLASS_NAME, "css-2txnih")  # Gasesc butonul de "Adauga anunt nou"
        sell_button.click()  # Dau click pe butonul de adaugare anunt
        time.sleep(4)
        self.assertIn("login", self.driver.current_url)  # Verific ca sunt pe pagina de login

        # Test pentru selectarea unei categorii
    def test_SelectCategory(self):
        category_links = self.driver.find_elements(By.CSS_SELECTOR, '[class="css-1gpccxq"]')  # Gasesc link-ul catre categoria "Imobiliare"
        category_links[1].click()  # Dau click pe link-ul catre categoria "Imobiliare"
        #alegem "Case de vanzare" din subcategoria Imobiliare
        imobiliare = self.driver.find_elements(By.CSS_SELECTOR, '[class="css-f0mzyq"]')
        imobiliare[2].click()
        #print("Category links:", category_links[1].get_attribute("href") )
        #print(len(category_links))
        time.sleep(5)
        self.assertIn("imobiliare", self.driver.current_url)  # Verific ca URL-ul actual contine "imobiliare"

     # Test pentru actualizarea unei resurse cu cererea PATCH
    def test_PatchResource(self):
        # Aici adaugă codul pentru a efectua o cerere PATCH către server
        # Verifică dacă actualizarea s-a făcut cu succes
        pass


# daca rulez fisierul acesta, se vor executa toate testele
if __name__ == "__main__":
    unittest.main()
