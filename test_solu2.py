import pytest
from SolutionDebug2 import retrait

def test_retarit1():
    #arrange
    solde = 1000
    montant = 500
    resultat_attendu = 500

    #act
    resultat_obtenu = retrait(solde,montant)

    #assert
    assert resultat_attendu == resultat_obtenu

def test_retarit2():
    #arrange
    solde = 1000
    montant = 900
    resultat_attendu = 100

    #act
    resultat_obtenu = retrait(solde,montant)

    #assert
    assert resultat_attendu == resultat_obtenu