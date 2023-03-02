from _pytest import mark
from pytest_bdd import then, scenarios, given, when
from steps.TestSaucedemoSteps import TestSaucedemoSteps as steps

scenarios('../features/SaucedemoExample.feature')


@given('The client set username <username> and <password>')
def validatePage(username, password):
    steps().setUsername(username)
    steps().setPassword(password)


@when('The client click on the Login button')
def loginbutton():
    steps().loginbtn()


@then('He ill enter in the main page')
def mainPage():
    steps().mainPage()




@given('The client is already logged')
def loginPage():
    steps().mainPage()


@when('The client click on Add to cart button')
def addToShoprCart():
    steps().addToCart()


@then('The product must be add to the cart')
def checkItem():
    steps().cartShopping()
    steps().itemOnCart()


@given('The client have a product in the cart')
def itemOnCartCheck():
    steps().itemOnCart()


@when('The client complete the checkout and finish the buy')
def startCheckout():
    steps().checkoutBtn()
    steps().completeForm()
    steps().continueCheckout()
    steps().finishBuy()


@then('The webpage must show a message with the text thank you for your order')
def checkItem():
    steps().completeCheckout()



# def teardown():
#     steps().closeBrowser()
