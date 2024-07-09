import unittest
import bank_account


class TestBank(unittest.TestCase):
    def setUp(self):
        self.account = bank_account.Account(0, "Tom", "1234")

    def test_depo_negative(self):
        self.assertNotEqual(self.account.Depo(-100), -100)

    def test_depo_positive(self):
        self.assertEqual(self.account.Depo(100), 100)
        self.assertEqual(self.account.Depo(50 + 100), 250)

    def test_depo_float(self):
        self.assertNotEqual(self.account.Depo(0.9), 0.9)
        self.assertNotEqual(self.account.Depo(-0.9), 0.9)

    def test_withdraw_positive(self):
        self.account.Depo(10000)
        self.assertEqual(self.account.With(100), 9900)
        self.assertNotEqual(self.account.With(1000), 100)
        self.assertEqual(self.account.With(8900), 0)

    def test_withdraw_negative(self):
        self.account.Depo(10000)
        self.assertNotEqual(self.account.With(-100), 110000)
        self.assertNotEqual(self.account.With(-1000), 100)
        self.assertEqual(self.account.With(-373), "Error: Withdraw can't be negative")

    def test_withdraw_float(self):
        self.account.Depo(10000)
        self.assertNotEqual(self.account.With(-10.2), 110000)
        self.assertNotEqual(self.account.With(0.2), 100)
        self.assertEqual(
            self.account.With(0.2), "Error: Withdraw must be a whole number"
        )


if __name__ == "__main__":
    unittest.main()
