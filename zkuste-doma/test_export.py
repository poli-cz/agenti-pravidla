import unittest

from export import export_mesice, nacti


class TestExport(unittest.TestCase):
    def setUp(self):
        self.radky = export_mesice(nacti(), 2026, 10)

    def test_vraci_radky_za_mesic(self):
        self.assertTrue(self.radky)
        self.assertTrue(all(r["datum"].startswith("2026-10") for r in self.radky))

    def test_sloupce(self):
        self.assertEqual(set(self.radky[0]), {"cislo", "datum", "zakaznik", "castka_kc"})


if __name__ == "__main__":
    unittest.main()
