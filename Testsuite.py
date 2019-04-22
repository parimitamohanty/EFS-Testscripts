from unittest import TestLoader, TestSuite, TextTestRunner
from WebAutomation.Test.Scripts.CustomerTest import Customer
from WebAutomation.Test.Scripts.InvestmentTest import Investment
from WebAutomation.Test.Scripts.StockTest import Stock

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Customer),
        loader.loadTestsFromTestCase(Investment),
        loader.loadTestsFromTestCase(Stock),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
