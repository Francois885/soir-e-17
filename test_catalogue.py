import unittest
import catalogue
from livre_s17 import Livre

CATALOGUE = [
Livre("1984", "Orwell", "9780451524935", 328, 1949),
Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
]
DOUBLON = Livre("1984 (réédition)", "Orwell", "9780451524935", 328, 1949)
AVEC_DOUBLON = CATALOGUE + [DOUBLON]

class Test(unittest.TestCase):


    def test_ordre(self):
        self.assertEqual([l.titre for l in catalogue.trier_par_titre(CATALOGUE)], ['1984', 'Fahrenheit 451', 'La Ferme des animaux', 'Le Meilleur des mondes'])
        self.assertEqual([l.annee for l in catalogue.trier_par_annee(CATALOGUE)], [1949, 1953, 1945, 1932])
        self.assertEqual([(l.auteur, l.annee) for l in catalogue.trier_par_auteur_puis_annee_recente(CATALOGUE)], [('Bradbury', 1953), ('Huxley', 1932), ('Orwell', 1949), ('Orwell', 1945)])
        self.assertEqual(len(catalogue.rechercher_par_auteur(CATALOGUE, "Orwell")), 2)
        self.assertEqual(catalogue.rechercher_par_isbn(CATALOGUE, "9780451524935").titre, "1984")
        self.assertEqual(catalogue.compter_distincts(AVEC_DOUBLON),4 ) 
        self.assertEqual(catalogue.dedoublonner(AVEC_DOUBLON)[0].titre, "1984")
        g = catalogue.regrouper_par_auteur(CATALOGUE)
        self.assertEqual([l.titre for l in g["Orwell"]], ['1984', 'La Ferme des animaux'])  

    def test_non_modif(self):
        [l.titre for l in catalogue.trier_par_titre(CATALOGUE)]
        self.assertEqual(CATALOGUE, [
            Livre("1984", "Orwell", "9780451524935", 328, 1949),
            Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
            Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
            Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
            ])

    def test_stabilite(self):
        livre1 = Livre("2000", "Orwell", "9780451524935", 328, 1949)
        livre2 = Livre("1984", "Orwell", "9780451524935", 328, 1949)
        
        liste = [livre1, livre2]
        self.assertEqual(catalogue.trier_par_annee(liste), [livre1, livre2])
    
    def test_regrouper_par_auteur(self):
        liste = catalogue.regrouper_par_auteur(CATALOGUE)

        self.assertIn("Orwell", liste)
        self.assertIn("Huxley", liste)
        self.assertIn("Bradbury", liste)

        self.assertEqual(len(liste["Orwell"]), 2)
        self.assertEqual(len(liste["Huxley"]), 1)
        self.assertEqual(len(liste["Bradbury"]), 1)

if __name__ == "__main__":
    unittest.main()