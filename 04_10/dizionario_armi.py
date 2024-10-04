import random

#inizializzo un dizionario armi
armi = {
    "coltello": {
        "danni_min": 10,
        "danni_max": 15
    },
    "ascia": {
        "danni_min": 5,
        "danni_max": 25
    }
}

#funzione per scegliere randomicamente il danno
def danni(arma):
    if arma in armi:
        danni_min = armi[arma]["danni_min"]
        danni_max = armi[arma]["danni_max"]
        danno_casuale = random.randint(danni_min, danni_max)
        return danno_casuale
    else:
        return "Arma non valida!"

# # Esempio di utilizzo
# arma_scelta = "coltello"
# danni_coltello = danni(arma_scelta)
# print(f"Danni inflitti con il {arma_scelta}: {danni_coltello}")

# arma_scelta = "ascia"
# danni_ascia = danni(arma_scelta)
# print(f"Danni inflitti con l'{arma_scelta}: {danni_ascia}")
