import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def test_konstruktori_luo_tyhjan_varaston(self):
        varasto = Varasto(15)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        varasto = Varasto(10)
        self.assertAlmostEqual(varasto.tilavuus, 10)

    def test_konstruktori_ei_luo_neg_tilavuutta(self):
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_ei_luo_neg_saldoa(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)
    
    def test_konstruktori_ei_luo_ylisuurta_saldoa(self):
        varasto = Varasto(5, 10)
        self.assertAlmostEqual(varasto.saldo, 5)

    def test_lisays_lisaa_saldoa(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(varasto.paljonko_mahtuu(), 2)
    
    def test_lisays_ei_lisaa_negatiivista(self):
        varasto = Varasto(10, 8)
        varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(varasto.saldo, 8)

    def test_lisays_ei_lisaa_ylitayteen(self):
        varasto = Varasto(10, 8)
        varasto.lisaa_varastoon(4)
        self.assertAlmostEqual(varasto.saldo, 10)
    
    def test_ottaminen_palauttaa_oikean_maaran(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(8)
        saatu_maara = varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(8)
        varasto.ota_varastosta(2)
        self.assertAlmostEqual(varasto.paljonko_mahtuu(), 4)
    
    def test_ottaminen_ei_ota_negatiivista(self):
        varasto = Varasto(10, 5)
        varasto.ota_varastosta(-5)
        self.assertAlmostEqual(varasto.saldo, 5)
    
    def test_ottaminen_ei_ota_liikaa(self):
        varasto = Varasto(10, 5)
        varasto.ota_varastosta(10)
        self.assertAlmostEqual(varasto.saldo, 0)
    
    def test_merkkijonoksi_muuntaminen(self):
        varasto = Varasto(10, 5)
        self.assertAlmostEqual(
            str(varasto),
            "saldo = 5, vielä tilaa 5"
        )