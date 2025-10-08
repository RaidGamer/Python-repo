# from Tutorials.modules.min_module import kalk 
from modules import min_module as m
import pytest

#assert är ett sätt att testa kod på ens egna project, genom assert kan man bestämma att den specifierade funktionen ska ge ut output at True om inte blir det AssertionError, då vet man vad som är fel i ens kod!
#Assert tar inte emot side effects tex print statements, den tar bara return values! Detta kan göra med strings också, så länge det är en return value! Folders kan också testas.

# def main():
#     test_kalk()

# def test_kalk():
#     try:
#         assert m.kalk(2) == 4
#     except AssertionError:
#         print("2 i kvadrat är inte 4")

#     try:
#         assert m.kalk(3) == 9
#     except AssertionError:
#         print("3 i kvadrat är inte 9")

#     try:
#         assert m.kalk(-2) == 4
#     except AssertionError:
#         print("-2 i kvadrat är inte 4")

#     try:
#         assert m.kalk(-3) == 9
#     except AssertionError:
#         print("-3 i kvadrat är inte 9")

#     try:
#         assert m.kalk(0) == 0
#     except AssertionError:
#         print("0 i kvadrat är inte 0")

#baserat på try och except kan vi se att den ger en error bara då 3 ska vara upphöjt och ge 9 men av nåt skäl ger den inte det dock så ger 2 upphöjt i 2, 4.
#Det betyder att vi har istället råkat skriva plus så att det blir 3+3 som ger 6 istället för 9 men 2+2 ger fortfarande 4.


def test_pos_kalk():
    assert m.kalk(2) == 4
    assert m.kalk(3) == 9

def test_neg_kalk():
    assert m.kalk(-2) == 4
    assert m.kalk(-3) == 9

def test_noll_kalk():
    assert m.kalk(0) == 0

def str_error():
    with pytest.raises(TypeError):
        m.kalk("kat")

#baserat på dessa funktioner kan vi också hitta vad som är fel med kalk funktionen, här behöver man inte kalla på funktionen, bara skriv pytest och namnet på filen.

# if __name__ == "__main__":
#     main()