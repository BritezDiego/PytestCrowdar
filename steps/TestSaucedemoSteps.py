from core.steps.BaseSteps import BaseStep
from pages import SaucedemoPage as page


class TestSaucedemoSteps(BaseStep):

    def setUsername(cls, text):
        user = page.inputUsername()
        user.setText(text)

    def setPassword(cls, text):
        password = page.inputPassword()
        password.setText(text)

    def loginbtn(self):
        loginbtn = page.loginBtn()
        loginbtn.click()

    def mainPage(self):
        mainpage = page.headerContainer()
        mainpage.isPresent()

    def addToCart(self):
        addtocart = page.addToCartBtn()
        addtocart.click()

    def cartShopping(self):
        cart = page.cartShopBtn()
        cart.click()

    def itemOnCart(self):
        itemoncart = page.itemOnCart()
        itemoncart.isPresent()

    def checkoutBtn(self):
        checkout = page.checkoutBtn()
        checkout.click()

    def completeForm(self):
        firstname = page.firstName()
        lastname = page.lastName()
        zip = page.zipCode()
        firstname.setText("Diego")
        lastname.setText("Britez")
        zip.setText("1437")

    def continueCheckout(self):
        continuecheckout = page.continueBtn()
        continuecheckout.click()

    def finishBuy(self):
        finish = page.finshBtn()
        finish.click()

    def completeCheckout(self):
        complete = page.checkoutComplete()
        complete.isPresent()
