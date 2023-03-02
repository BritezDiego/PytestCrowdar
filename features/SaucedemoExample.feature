Feature:Login and add article


  @example
  Scenario Outline: The client log in
    Given The client set username <username> and <password>
    When The client click on the Login button
    Then He ill enter in the main page

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |


  Scenario Outline: Add a product to the shopping cart
    Given The client is already logged
    When The client click on Add to cart button
    Then The product must be add to the cart

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario: Buy a product
    Given The client have a product in the cart
    When  The client complete the checkout and finish the buy
    Then The webpage must show a message with the text thank you for your order