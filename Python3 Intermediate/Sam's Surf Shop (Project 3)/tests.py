import unittest
import surfshop
import datetime


class TestSurf(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        self.assertEqual(self.cart.add_surfboards(1),
                         f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for boards in [2, 3, 4]:
            with self.subTest(boards):
                self.assertEqual(self.cart.add_surfboards(
                    boards), f'Successfully added {boards} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    @unittest.skip
    def test_add_surfboards_too_many(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    def test_apply_locals_discount(self):
        self.assertTrue(self.cart.apply_locals_discount())

    def test_set_checkout_date(self):
        self.assertRaises(surfshop.CheckoutDateError,
                          self.cart.set_checkout_date, datetime.datetime.now())



unittest.main()
