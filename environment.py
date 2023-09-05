from browser import Browser

def before_all(context):
    """
    Vom defini toate instructiunile care trebuie
    executate inainte rularii tuturor pasilor
    """
    context.browser = Browser()

def after_all(context):
    """
    Vom defini toate instructiunile care trebuie
    executate dupa rularea tuturor pasiilor
    """
    context.browser.close()