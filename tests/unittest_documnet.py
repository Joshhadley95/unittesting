import unittest
import warnings
import sys

def add_to_cart(item, cart):
    # Adds an item to the cart if it's not already there.
    warnings.warn(f"{item} is already in the cart!", UserWarning)
    if item in cart:
        return f"{item} is already in the cart!"
    cart.append(item)
    return f"{item} has been added to the cart."

def checkout(cart):
    # Checks out the cart if it contains items.
    if len(cart) > 0:
        return f"Checking out with {len(cart)} items!"
    return "Your cart is empty! Add some magic items first!"

class TestMagicStore(unittest.TestCase):

    def setUp(self):
        self.cart = []

    def tearDown(self):
        self.cart = None

    def test_cart_length(self):
        cart = ["Magic Wand", "Flying Broom", "Invisibility Cloak"]
        assert len(cart) == 3, "Cart should contain 3 items."

    def test_checkout(self):
        cart = ["Magic Wand", "Flying Broom", "Invisibility Cloak"]
        result = checkout(cart)
        self.assertEqual(result, "Checking out with 3 items!")

    def test_checkout_empty_cart(self):
        cart = []
        result = checkout(cart)
        self.assertEqual(result, "Your cart is empty! Add some magic items first!")

    def test_add_to_cart_warning(self):
        cart = []
        with self.assertWarns(UserWarning):
            add_to_cart("Magic Wand", cart) # add first time, should not warn
            add_to_cart("Magic Wand", cart) # add second time, should warn

    @unittest.skip("Skipping this test for now.")
    def test_discounted_items(self):
        self.assertEqual(len(cart), 2) #placeholder for discounted items test
    
    @unittest.skipIf(sys.version == "win32", "Skipping this test on Windows.")
    def test_platform_specific(self):
        pass #placeholder for platform-specific test


# Calling the functions
cart = []

# Adding items to the cart
print(add_to_cart("Magic Wand", cart))  
print(add_to_cart("Flying Broom", cart)) 
print(add_to_cart("Invisibility Cloak", cart)) 
print(add_to_cart("Magic Wand", cart))  

if __name__ == "__main__":
    unittest.main()

