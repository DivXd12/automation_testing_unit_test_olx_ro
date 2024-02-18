# import modulele necesare
import unittest  #Importă modulul pentru crearea și rularea de teste
from selenium import webdriver  # Importă modulul pentru interacțiunea cu browserele web
from selenium.common.exceptions import NoSuchElementException  #Importă clasa pentru gestionarea excepției când un element nu este găsit

# definesc clasa de test pentru pagina principală OLX
class OLXHomePageTests(unittest.TestCase):

    # setUp se va executa înaintea fiecărui test
    def setUp(self):
        self.driver = webdriver.Chrome()  # initiez driverul de Chrome
        self.driver.get("https://www.olx.ro/")  # deschid pagina principală OLX

    # tearDown se va executa dupa fiecare test
    def tearDown(self):
        self.driver.quit()  # închid browserul

    #  test pentru verificarea titlului paginii
    def test_Title(self):
        title = self.driver.title  # obținem titlul paginii
        self.assertEqual(title, "OLX.ro - Anunțuri pe gratis")  # verificăm dacă titlul este cel asteptat

    # test pentru căutarea unui produs
    def test_Search(self):
        search_box = self.driver.find_element_by_id("search")  # Gasesc box-ul de cautare dupa id
        search_box.send_keys("bicicleta")  # Introduc textul "bicicleta" in campul de cautare
        search_button = self.driver.find_element_by_id("search-submit")  # Gasesc butonul de cautare
        search_button.click()  # Dau click pe butonul de căutare
        self.assertTrue("bicicleta" in self.driver.current_url)  # Verific dacă URL-ul contine cuvantul cautat

    # Test pentru verificarea accesului la pagina de autentificare
    def test_AccessLoginPage(self):
        login_button = self.driver.find_element_by_class_name("button-text-wrapper")  # Gasesc butonul de login dupa clasa
        login_button.click()  # Dau click pe butonul de login
        self.assertIn("account", self.driver.current_url)  # Verific daca am fost redirecționat pe pagina de login care conține "account" în URL

        # Test pentru verificarea existentei butonului "Adauga anunt nou"
    def test_SellButtonExists(self):
        try:
            sell_button = self.driver.find_element_by_id(
                "post-new-add-button")  # Incerc sa gasesc butonul de "Adauga anunt nou"
            exists = True
        except NoSuchElementException: # NoSuchElementException este folosit pentru a intercepta cazul în care un element nu este gasit. si este deja importata
            exists = False
        self.assertTrue(exists)  # assert ca butonul de "Adauga anunt nou" exista

        # Test pentru adaugare anunt fara a fi logat
    def test_AddAdWithoutLogin(self):
        sell_button = self.driver.find_element_by_class_name("css-2txnih")  # Gasesc butonul de "Adauga anunt nou"
        sell_button.click()  # Dau click pe butonul de adaugare anunt
        self.assertIn("login", self.driver.current_url)  # Verific ca sunt pe pagina de login

        # Test pentru selectarea unei categorii
    def test_SelectCategory(self):
        category_link = self.driver.find_element_by_link_text(
            "https://www.olx.ro/imobiliare/")  # Gasesc link-ul catre categoria "Imobiliare"
        category_link.click()  # Dau click pe link-ul catre categoria "Imobiliare"
        self.assertIn("imobiliare", self.driver.current_url)  # Verific ca URL-ul actual contine "imobiliare"


# daca rulez fisierul acesta, se vor executa toate testele
if __name__ == "__main__":
    unittest.main()