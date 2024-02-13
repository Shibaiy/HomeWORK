from selene import be, have


def test_search1(browser_chrome):
    browser_chrome.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser_chrome.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search2(browser_chrome):
    browser_chrome.element('[name="q"]').should(be.blank).type('77fgfgfgfg666566').press_enter()
    browser_chrome.element('[class="v3jTId"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
