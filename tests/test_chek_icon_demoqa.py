


def test_chek_icon(browser):

    browser.get('http://demoqa.com/')

    icon = browser.find_element(By.CSS_SELECTOR, '"#app" > header > a')

    if icon is None:
        print('Не найден')
        print('Найден')


