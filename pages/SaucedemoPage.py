from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


def inputUsername():
    return UIElement(By.ID, "user-name")


def inputPassword():
    return UIElement(By.ID, "password")


def loginBtn():
    return UIElement(By.ID, "login-button")


def headerContainer():
    return UIElement(By.ID,"header_container")


def addToCartBtn():
    return UIElement(By.ID, "add-to-cart-sauce-labs-backpack")


def cartShopBtn():
    return UIElement(By.ID, "shopping_cart_container")


def itemOnCart():
    return UIElement(By.ID, "item_4_title_link")


def checkoutBtn():
    return UIElement(By.ID, "checkout")


def firstName():
    return UIElement(By.ID, "first-name")


def lastName():
    return UIElement(By.ID, "last-name")


def zipCode():
    return UIElement(By.ID, "postal-code")


def continueBtn():
    return UIElement(By.ID, "continue")


def finshBtn():
    return UIElement(By.ID, "finish")


def checkoutComplete():
    return UIElement(By.ID, "checkout_complete_container")