import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_backet_on_form(browser):
    browser.get(link)
    time.sleep(60)
    text_submit = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']").text
    print(text_submit)
    assert "Ajouter au panier" == text_submit, "Submit is not present"

