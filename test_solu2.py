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
    montant = 800
    resultat_attendu = 200

    #act
    resultat_obtenu = retrait(solde,montant)

    #assert
    assert resultat_attendu == resultat_obtenu


def test_retarit3():
    #arrange
    solde = 1000
    montant = 300
    resultat_attendu = 700

    #act
    resultat_obtenu = retrait(solde,montant)

    #assert
    assert resultat_attendu == resultat_obtenu