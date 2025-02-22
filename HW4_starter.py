# SI 206 HW4
# Your name:
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.

import unittest

class Customer:
    """
    A class representing a customer who can place orders at restaurants.
    
    Attributes:
        name (str): The customer's name
        employer_id (int or None): If the customer works at a restaurant, this is that restaurant's ID
        account_balance (float): How much money the customer has available
    """
    
    def __init__(self, name, employer_id=None, account_balance=15.0):
        """
        Initialize a new Customer object.
        
        Args:
            name (str): The customer's name
            employer_id (int or None, optional): ID of restaurant they work for. Defaults to None.
            account_balance (float, optional): Starting balance. Defaults to 15.0.
        """
        self.name = name
        self.employer_id = employer_id
        self.account_balance = account_balance

    def __str__(self):
        """Return a string describing the customer and their balance."""
        return f"Customer {self.name} has ${self.account_balance:.2f} in their account"

    def deposit_funds(self, amount):
        """
        Add money to the customer's account.
        
        Args:
            amount (float): Amount of money to add
        """
        self.account_balance += amount

    def place_order(self, restaurant, order_dict):
        """
        Attempt to place an order at a restaurant.
        
        Args:
            restaurant (Restaurant): The restaurant to order from
            order_dict (dict): A dictionary where:
                - keys are MenuItem objects
                - values are dictionaries containing:
                    - 'quantity': number of items to order
                    - 'express': True/False for express service
        
        Returns:
            bool: True if order was successful, False otherwise
        
        Note:
            An order should only be successful if:
            1. The customer has enough money
            2. The restaurant has enough of each item in stock
            3. All items in the order are available at the restaurant
            
        TODO: Implement this method following these steps:
        1. Calculate the total cost of the order
        2. Check if customer has enough money
        3. Try to process the order through the restaurant
        4. If successful, deduct money and pay restaurant
        """
        pass  # Remove this line and write your code here

class MenuItem:
    """
    A class representing an item that can be ordered from a restaurant.

    Attributes:
        name (str): The name of the menu item
    """
    
    def __init__(self, name):
        """
        Initialize a MenuItem object.
        
        Args:
            name (str): The name of the menu item
        """
        self.name = name
    
    def __str__(self):
        """Return the item's name as a string."""
        return self.name

    def __eq__(self, other):
        """
        Check equality based on the item's name.
        
        Args:
            other (MenuItem): Another MenuItem instance to compare
        
        Returns:
            bool: True if names are the same, False otherwise
        
        TODO: Implement this method to compare MenuItem instances based on their 'name' attribute.
        """
        pass  # Remove this line and write your code here

    def __hash__(self):
        """
        Return the hash based on the item's name.
        
        Returns:
            int: The hash of the item's name
        
        TODO: Implement this method to return a hash based on the 'name' attribute. Use the hash() function, which is a built-in function in Python.
        """
        pass  # Remove this line and write your code here

class Restaurant:
    """
    A class representing a restaurant that can take orders and maintain inventory.
    
    Attributes:
        name (str): The restaurant's name
        restaurant_id (int): Unique identifier for the restaurant
        income (float): Money earned from orders
        menu (dict): Dictionary mapping MenuItem objects to their quantity in stock
        prices (dict): Dictionary mapping MenuItem objects to their prices at this restaurant
    """
    
    def __init__(self, name, restaurant_id, income=0.0):
        """
        Initialize a Restaurant object.
        
        Args:
            name (str): The restaurant's name
            restaurant_id (int): Unique identifier for the restaurant
            income (float, optional): Starting income. Defaults to 0.0.
        """
        self.name = name
        self.restaurant_id = restaurant_id
        self.income = income
        self.menu = {}    # Stores inventory of items
        self.prices = {}  # Stores prices of items

    def __str__(self):
        """Return a string showing the restaurant's name and income."""
        return f"{self.name} has earned ${self.income:.2f}"

    def set_price(self, item, price):
        """
        Set the price for a menu item at this restaurant.
        
        Args:
            item (MenuItem): The menu item
            price (float): The price to set for this item
        """
        self.prices[item] = price

    def get_price(self, item):
        """
        Get the price of a menu item at this restaurant.
        
        Args:
            item (MenuItem): The menu item to check
            
        Returns:
            float: The price of the item, or 20 if not found
        """
        return self.prices.get(item, 20)

    def accept_payment(self, amount):
        """
        Add to the restaurant's income.
        
        Args:
            amount (float): Amount of money to add
        """
        self.income += amount

    def calculate_item_cost(self, item, quantity, express, customer=None):
        """
        Calculate the cost for an order of items.
        
        Args:
            item (MenuItem): The item being ordered
            quantity (int): How many of the item are being ordered
            express (bool): Whether this is an express order
            customer (Customer, optional): The customer placing the order. Defaults to None.
        
        Returns:
            float: The total cost for this item
            
        Note:
            - Express orders cost 20% more (multiply by 1.2)
            - If the customer works at this restaurant (their employer_id matches
              this restaurant's restaurant_id), they get a 40% discount (multiply by 0.6)
            
        TODO: Implement this method following these steps:
        1. Get the base price for the item
        2. Multiply by quantity
        3. Apply express surcharge if applicable
        4. Apply employee discount if applicable
        """
        pass  # Remove this line and write your code here

    def stock_up(self, item, quantity):
        """
        Add items to the restaurant's inventory.
        
        Args:
            item (MenuItem): The item to add
            quantity (int): How many to add
            
        TODO: Implement this method following these steps:
        1. If the item is already in the menu, add to its quantity
        2. If it's not, set its quantity to the given amount
        """
        pass  # Remove this line and write your code here

    def process_order(self, order_dict):
        """
        Try to process an order and update inventory.
        
        Args:
            order_dict (dict): Dictionary where:
                - keys are MenuItem objects
                - values are dictionaries containing:
                    - 'quantity': number of items ordered
                    - 'express': True/False for express service
        
        Returns:
            bool: True if order was processed successfully, False otherwise
            
        TODO: Implement this method following these steps:
        1. Check if all items are available in sufficient quantity
        2. If they are, reduce inventory and return True
        3. If they aren't, return False
        """
        pass  # Remove this line and write your code here

class TestAllMethods(unittest.TestCase):
    """
    Test cases for the Restaurant Management System. 
    
    Within this class, only modify the test cases test_place_order() and test_place_order_2().

    You don't need to modify the other test cases, but studying them will help you understand how your code should work.
    """
    
    def setUp(self):
        """Create objects we need for all test methods."""
        # Create menu items
        self.burger = MenuItem("Cheeseburger")
        self.fries = MenuItem("Fries")
        self.shake = MenuItem("Milkshake")
        self.salad = MenuItem("Salad")

        # Create restaurants
        self.diner = Restaurant("Joe's Diner", 1)
        self.cafe = Restaurant("Campus Cafe", 2)

        # Set different prices for each restaurant
        self.diner.set_price(self.burger, 5.0)  # $5.00 at diner
        self.diner.set_price(self.fries, 2.5)   # $2.50 at diner
        self.cafe.set_price(self.burger, 6.5)   # $6.50 at cafe
        self.cafe.set_price(self.fries, 3.0)    # $3.00 at cafe

        # Create customers
        self.customer = Customer("Alice")
        self.employee = Customer("Bob", employer_id=1, account_balance=25.0)

    def test_restaurant_constructor(self):
        """Test Restaurant constructor."""
        self.assertEqual(self.diner.name, "Joe's Diner")
        self.assertAlmostEqual(self.diner.income, 0.0, 2)
        self.assertEqual(self.cafe.restaurant_id, 2)
        self.assertEqual(self.cafe.menu, {})

    def test_menuitem_constructor(self):
        """Test MenuItem constructor."""
        self.assertEqual(self.burger.name, "Cheeseburger")

    def test_restaurant_prices(self):
        """Test that restaurants can have different prices."""
        self.assertAlmostEqual(self.diner.get_price(self.burger), 5.0, 2)
        self.assertAlmostEqual(self.cafe.get_price(self.burger), 6.5, 2)
        self.assertAlmostEqual(self.diner.get_price(self.fries), 2.5, 2)
        self.assertAlmostEqual(self.cafe.get_price(self.fries), 3.0, 2)

    def test_customer_constructor(self):
        """Test Customer constructor."""
        self.assertEqual(self.customer.name, "Alice")
        self.assertAlmostEqual(self.customer.account_balance, 15.0, 2)
        self.assertEqual(self.employee.employer_id, 1)

    def test_stock_up(self):
        """Test adding inventory."""
        self.diner.stock_up(self.burger, 10)
        self.assertEqual(self.diner.menu[self.burger], 10)
        
        self.diner.stock_up(self.burger, 5)
        self.assertEqual(self.diner.menu[self.burger], 15)
        
        self.diner.stock_up(self.fries, 20)
        self.assertEqual(self.diner.menu[self.fries], 20)

    def test_calculate_item_cost(self):
        """Test price calculations."""
        # Test regular order
        self.assertAlmostEqual(self.diner.calculate_item_cost(
            self.burger, 2, False, None), 10.0, 2)
        
        # Test express order (20% more)    
        self.assertAlmostEqual(self.diner.calculate_item_cost(
            self.burger, 2, True, None), 12.0, 2)
        
        # Test employee discount (40% off)    
        self.assertAlmostEqual(self.diner.calculate_item_cost(
            self.burger, 2, False, self.employee), 6.0, 2)
        
        # Test express + employee discount    
        self.assertAlmostEqual(self.diner.calculate_item_cost(
            self.burger, 2, True, self.employee), 7.2, 2)

    def test_accept_payment(self):
        """Test restaurant receiving payment."""
        initial_income = self.diner.income
        self.diner.accept_payment(10.5)
        self.assertAlmostEqual(self.diner.income, initial_income + 10.5, 2)
        
        self.diner.accept_payment(5.75)
        self.assertAlmostEqual(self.diner.income, initial_income + 16.25, 2)

    def test_deposit_funds(self):
        """Test adding money to customer account."""
        initial_balance = self.customer.account_balance
        self.customer.deposit_funds(20.0)
        self.assertAlmostEqual(self.customer.account_balance, initial_balance + 20.0, 2)
        
        self.customer.deposit_funds(5.5)
        self.assertAlmostEqual(self.customer.account_balance, initial_balance + 25.5, 2)

    def test_process_order(self):
        """Test the Restaurant's process_order method."""
        # Test successful order processing
        self.diner.stock_up(self.burger, 5)
        self.diner.stock_up(self.fries, 10)
        order = {
            self.burger: {"quantity": 2, "express": False},
            self.fries: {"quantity": 3, "express": True}
        }
        self.assertTrue(self.diner.process_order(order))
        # Verify inventory was reduced
        self.assertEqual(self.diner.menu[self.burger], 3)  # 5 - 2 = 3
        self.assertEqual(self.diner.menu[self.fries], 7)   # 10 - 3 = 7

        # Test order with insufficient inventory
        order_too_large = {
            self.burger: {"quantity": 5, "express": False}  # Only 3 left
        }
        self.assertFalse(self.diner.process_order(order_too_large))
        # Verify inventory wasn't changed
        self.assertEqual(self.diner.menu[self.burger], 3)

        # Test order with unavailable item
        order_unavailable = {
            self.shake: {"quantity": 1, "express": False}  # Shake not in menu
        }
        self.assertFalse(self.diner.process_order(order_unavailable))

    def test_menuitem_equality(self):
        """Test that different MenuItem instances with the same name are equal."""
        burger1 = MenuItem("Cheeseburger")
        burger2 = MenuItem("Cheeseburger")
        fries1 = MenuItem("Fries")
        fries2 = MenuItem("Fries")

        # Check equality
        self.assertEqual(burger1, burger2)
        self.assertEqual(fries1, fries2)

        # Check hash equality
        self.assertEqual(hash(burger1), hash(burger2))
        self.assertEqual(hash(fries1), hash(fries2))

        # Use different instances as keys in a dictionary
        menu = {}
        menu[burger1] = 10.99
        menu[fries1] = 2.99

        # Access using different instances
        self.assertIn(burger2, menu)
        self.assertIn(fries2, menu)
        self.assertEqual(menu[burger2], 10.99)
        self.assertEqual(menu[fries2], 2.99)

        # Update price using burger2
        menu[burger2] = 11.99
        self.assertEqual(menu[burger1], 11.99)
        self.assertEqual(menu[burger2], 11.99)

        # The length should be 2
        self.assertEqual(len(menu), 2)
        
    def test_place_order(self):
        """
        Test different order placement scenarios. 
        
        This test method should verify three scenarios:
        1. Orders when customer has insufficient funds
        2. Orders when restaurant has insufficient inventory
        3. Orders for items that restaurant doesn't carry
        
        Important: Write test cases for all three scenarios described above.
        Each test case should verify that place_order returns False when:
        - Customer doesn't have enough money
        - Restaurant doesn't have enough inventory
        - Restaurant doesn't carry the ordered item

        NOTE: To test the place_order() method, you need to create an order dictionary that you then pass into place_order(). 
        For more information, see the assignment instructions.
        
        """
        # Some helpful setup code is provided - you'll need to add the test cases:
        
        # Scenario 1: Test order placement with insufficient funds
        # Setup: Create a customer with low balance and add some inventory
        customer_1 = Customer("Sam", account_balance=5.0)
        self.diner.stock_up(self.burger, 10)
        # TODO: Add your test case here - verify order fails due to insufficient funds
        
        # Scenario 2: Test order placement with insufficient inventory
        # Setup: Stock the restaurant with very limited inventory
        self.diner.stock_up(self.fries, 1)
        # TODO: Add your test case here - verify order fails due to insufficient inventory
        
        # Scenario 3: Test order placement for unavailable items
        # Setup: Try to order an item that exists but hasn't been stocked
        # TODO: Add your test case here - verify order fails for unavailable items

    def test_place_order_2(self):
        """
        Test order processing and payment flows.
        
        This test needs to be fixed! The current assertions are incorrect.
        The test should verify that after a successful order:
        1. The customer's account balance is reduced by the correct amount
        2. The restaurant's income increases by the correct amount
        
        Important: The values in the assertions below are wrong.
        """
        customer = Customer("Pat", account_balance=300)
        restaurant = Restaurant("Downtown Diner", 3)
        restaurant.stock_up(self.burger, 20)
        restaurant.stock_up(self.fries, 30)
        
        restaurant.set_price(self.burger, 7.0)  # $7.00 per Cheeseburger
        restaurant.set_price(self.fries, 3.5)   # $3.50 per Fries

        # Define the order
        order = {
            self.burger: {
                "quantity": 2,
                "express": False
            },
            self.fries: {
                "quantity": 3,
                "express": True
            }
        }

        # Place the order and assert that it is successful
        self.assertTrue(customer.place_order(restaurant, order))
         

        # Fix the incorrect assertions with the correct expected values
        self.assertAlmostEqual(customer.account_balance, 271.2, places=2) 
        self.assertAlmostEqual(restaurant.income, 25.4, places=2) 
        


def main():
    """Run the tests and print a summary."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAllMethods)
    
    total_tests = suite.countTestCases()
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n=== Test Case Summary ===")
    print(f"Total test cases: {total_tests}")
    print(f"Tests passed: {total_tests - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures)}")
    print(f"Tests with errors: {len(result.errors)}")
    print("========================")

if __name__ == "__main__":
    main()
