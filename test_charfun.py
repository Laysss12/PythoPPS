import unittest
from charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    def test_palindromos(self):
        # Cadenas palíndromas
        self.assertEqual(esPalindromo("Amo la pacífica paloma"), True)
        self.assertEqual(esPalindromo("Yo hago yoga hoy"), True)
    
    def test_no_palindromos(self):
        # Cadenas no palíndromas
        self.assertEqual(esPalindromo("Ciberseguridad"), False)
        self.assertEqual(esPalindromo("MiguelAngel"), False)

    def test_cadena_vacia(self):
        # Cadena vacía
        self.assertEqual(esPalindromo(""), False)

    def test_cadena_espacio(self):
        # Cadena de solo espacios
        self.assertEqual(esPalindromo("    "), False)

    def test_un_caracter(self):
        # Cadena con solo un carácter
        self.assertEqual(esPalindromo("m"), False)

    def test_cadenas_con_tildes_y_simbolos(self):
        # Cadenas con tildes y caracteres especiales
        self.assertTrue(esPalindromo("ÁÉÍÚ úíéá"))
        self.assertEqual(esPalindromo("Átale, demoníaco Caín, o me delata"), True)
        self.assertTrue(esPalindromo("Allá"))

if __name__ == "__main__":
    unittest.main()

