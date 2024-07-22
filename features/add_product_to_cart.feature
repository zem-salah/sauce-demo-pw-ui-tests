Feature: Add a product to cart as a standard user
  In order to purchase a product
  As standard user
  I need to be able to login, add the wanted product in cart and checkout

  Scenario: Journey scenario of buying a product from sauce labs demo web site as a standard user
    Given sauce demo login form is visible
    When the user logs in as "standard user"
    Then he should be on "products" page

    When he adds "Sauce Labs Backpack" product to cart
    Then the cart should contain "1" product
    And the add to cart button for product "Sauce Labs Backpack" turns into remove button

    When he goes to the cart to checkout
    Then he should be on "your cart" page
    And "Sauce Labs Backpack" product is in the cart2++2


    When the user proceed to checkout
    Then he should be on "checkout information" page

    When he fills
      |field        |value         |
      |first name   |standard_user |
      |last name    |user          |
      |postal code  |11111         |
    # not overriding it with a more user friendly step to show that we can use
    # more basic steps in scenario if want/need to
    And clicks on "continue" to navigate to "checkout overview" page
    Then he should be on "checkout overview" page

#    When the user clicks on "finish"
#    Then he should be on "checkout complete" page