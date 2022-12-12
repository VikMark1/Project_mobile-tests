import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

@allure.tag("mobile")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "VikaMark")
@allure.feature("Settings")
@allure.story("Settings tab displaying")
def test_1_settings_tab():
    with allure.step("Click on action menu"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')).click()
    with allure.step("Click on Settings"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_settings')).click()
    with allure.step("Return to main page"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.ImageButton")).click()

@allure.tag("mobile")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "VikaMark")
@allure.feature("Search")
@allure.story("Search results displaying")
def test_2_search_content():
    with allure.step("Click on Search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    with allure.step("Type search word"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')
    with allure.step("Verify found results"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
    with allure.step("Return to main page"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.ImageButton")).click()

@allure.tag("mobile")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "VikaMark")
@allure.feature("Search")
@allure.story("Search results displaying")
def test_3_search_content_in_turn():
    with allure.step("Click on Search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    with allure.step("Type search word"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')
    with allure.step("Clear found results"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).clear()
    with allure.step("Type another search word"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('API')
    with allure.step("Verify found results"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
    with allure.step("Return to main page"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.ImageButton")).click()

@allure.tag("mobile")
@allure.severity(Severity.MINOR)
@allure.label("owner", "VikaMark")
@allure.feature("Additional features")
@allure.story("'Hide this card' feature")
def test_4_hide_card():
    with allure.step("Click on action menu"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_list_card_header_menu')).click()
    with allure.step("Click on 'Hide this card'"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/title')).click()

@allure.tag("mobile")
@allure.severity(Severity.MINOR)
@allure.label("owner", "VikaMark")
@allure.feature("Additional features")
@allure.story("Voice search feature")
def test_5_voice_search():
    with allure.step("Click on voice search button"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/voice_search_button')).click()

#@allure.tag("mobile")
#@allure.severity(Severity.MINOR)
#@allure.label("owner", "VikaMark")
#@allure.feature("Settings")
#@allure.story("'Support Wikipedia' tab'")
#def test_2_support_wikipedia():
   # with allure.step("Click on action menu"):
        #browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')).click()
    #with allure.step("Click on 'Support Wikipedia' tab'"):
        #browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_donate')).click()