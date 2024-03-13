# Proiect-final
Proiectul final folosind libraria Unit Test

Structura proiectului:
- [x] Write general information
- [x] Short presentation of each term used in the project
- [x] Update the website

​Proiectul este creat folosind framework-ul unittest al limbajului Python pentru a crea teste automatizate pentru site-ul OLX.ro. Proiectul are o clasa numită OLXHomePageTests, care mosteneste de la unittest.TestCase și contine mai multe metode:

setUp(self): Această metodă este folosită pentru a initia driverul de Chrome si pentru a deschide pagina principala OLX înainte de fiecare test individual.
tearDown(self): Aceasta inchide browserul după fiecare test, asigurand că fiecare test ruleaza într-un mediu curat.
Metode de test incepand cu 'test_': Fiecare dintre aceste metode reprezinta un caz de test specific.
Testele făcute:

test_Title: Verifica dacă titlul paginii corespunde cu titlul asteptat.
test_Search: Simuleaza o cautare de produs ('bicicleta') si verifica daca cuvantul cautat apare în URL-ul paginii de rezultate.
test_AccessLoginPage: Verifica daca utilizatorul este redirecaionat catre pagina de autentificare atunci când se incearca logarea.
test_SellButtonExists: Verifica daca butonul de "Adauga anunt nou" exista pe pagina.
test_AddAdWithoutLogin: Incearca să adauge un anunț fara a fi logat si verifică dacă este redirectionat catre pagina de login.
test_SelectCategory: Selecteaza o categorie ('Imobiliare') si verifica daca URL-ul actual contine cuvantul respectiv.

FRAMEWORK-UL FOLOSIT

unittest: Un framework de testare ce vine incorporat în limbajul Python, utilizat pentru crearea de teste, asertiuni și organizarea rularii lor.
Rezultatele obtinute:

test_Title: Acest test ar trebui să treaca daca titlul paginii corespunde cu cel așteptat ("OLX.ro - Anunțuri Gratuite").

test_Search: Testul va trece daca cautarea pentru "bicicleta" în fapt actualizeaza URL-ul cu query-ul de căutare si te duce la pagina de rezultate corespunzatoare.

test_AccessLoginPage: Acest test va trece daca dupa ce apăsarea pe butonul de login te redirectioneaza catre pagina de autentificare cu "account" în URL.

test_SellButtonExists: Testul va trece dacă butonul de "Adaugă anunt nou" este prezent pe pagina.

test_AddAdWithoutLogin: Testul va trece daca incercarea de a adauga un anunț fara a fi logat te redirectionează catre pagina de autentificare.

test_SelectCategory: Testul ar debea trece daca esti redirectionat catre sectiunea "Imobiliare" după ce dai click pe link-ul categoriei respective
