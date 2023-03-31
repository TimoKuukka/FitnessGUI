# KUNTOILIJAN TIEDOT OLIO OHJELMOINTINA
# ======================================

# KIRJASTOT JA MODULIT
# --------------------

import fitness

# Luokkamääritykset
# -----------------

# Kuntoilija-luokka Yliluokka JunioriKuntoilijalle (super class)
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    # Olionmuodostin eli konstruktori, self -> tuleva olio
    def __init__(self, nimi, pituus, paino, ika, sukupuoli, paiva):
        
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.pituus, self.paino)
        self.punnitus_paiva = paiva

    # Metodi rasvaprosentin laskemiseen (aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

    # Metodi rasvaprosentin laskemiseen USA:n armeijan metodeilla
    def usa_rasvaprosentti_mies(self, pituus, vyotaron_ymparys, kaulan_ymparys):
        """ summary

        Args:
            pituus(float): pituus (cm)
            vyotaron_ymparys (float)): vyötarön ympärysmitta (cm)
            kaulan_ymparys (float): kaulan ympärysmitta (cm)

        Returns:
            float: rasvaprosentti
        """
        usa_rasvaprosentti = fitness.usarasvaprosentti_mies(pituus, vyotaron_ymparys,kaulan_ymparys)
        return usa_rasvaprosentti

    def usa_rasvaprosentti_nainen(self, pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
        """laskee kehon rasvaprosentin USA:n armeijan kaavalla

        Args:
            pituus(float): pituus (cm)
            vyotaron_ymparys (float)): vyötarön ympärysmitta (cm)
            kaulan_ymparys (float): kaulan ympärysmitta (cm)
            lantion_ymparys (float): lantion ympärysmitta (cm)

        Returns:
            float: rasvaprosentti
        """
        usa_rasvaprosentti = fitness.usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys)
        return usa_rasvaprosentti

#  JunioriKuntoilija-luokka Kuntoilija-luokan aliluokka (subclass) 

class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään periytyminen, mitä ominaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli)

        # Metodi rasvaprosentin laskemiseen (ylikirjoitettu lapsen metodilla)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti


if __name__ == "__main__":
    
    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    # print('painoindeksi on', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija('Aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, 'painaa', juniorikuntoilija.paino, 'kg')
    # print('painoindeksi on ', kuntoilija.paino())
    print('rasvaprosentti on', juniorikuntoilija.rasvaprosentti())