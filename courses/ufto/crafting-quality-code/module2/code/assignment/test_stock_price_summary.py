import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty(self):
          """ Test test_stock_price_summary when empty """
          actual = a1.stock_price_summary([])
          expected = (0,0)
          self.assertEqual(actual, expected)

    def test_stock_price_summary_just_one_gain(self):
          """ Test test_stock_price_summary when there are just gains in price changes """
          actual = a1.stock_price_summary([0.01])
          expected = (0.01,0)
          self.assertEqual(actual, expected)
    
    def test_stock_price_summary_just_one_loss(self):
          """ Test test_stock_price_summary when there are just gains in price changes """
          actual = a1.stock_price_summary([-0.02])
          expected = (0, -0.02)
          self.assertEqual(actual, expected)

    def test_stock_price_summary_just_gains(self):
          """ Test test_stock_price_summary when there are just gains in price changes """
          actual = a1.stock_price_summary([0.01, 0.03, 0.02, 0.14, 0, 0, 0.10, 0.01])
          expected = (0.31,0)
          self.assertEqual(actual, expected)

    def test_stock_price_summary_just_loss(self):
          """ Test test_stock_price_summary when there are just loss in price changes """
          actual = a1.stock_price_summary([-0.01, -0.03, -0.02, -0.14, 0, 0, -0.10, -0.01])
          expected = (0,-0.31)
          self.assertEqual(actual, expected)
    
    def test_stock_price_summary_gains_and_loss(self):
          """ Test test_stock_price_summary when there are gains and loss in price changes """
          actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
          expected = (0.14, -0.17)
          self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)