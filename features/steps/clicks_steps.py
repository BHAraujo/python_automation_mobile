from behave import step

from pages.clicks_page import ClicksPage

clicks_page = ClicksPage()


@step(u'the tap in the menu Clicks')
def step_impl(context):
    clicks_page.menu_clicks_tap()

@step(u'redirect to option Clicks')
def step_impl(context):
    clicks_page.wait_menu_click()

@step(u'tap long click')
def step_impl(context):
    clicks_page.long_click_tap()

@step(u'tap double click')
def step_impl(context):
    clicks_page.double_click_tap()

@step(u'tap double lazy click')
def step_impl(context):
    clicks_page.lazy_double_click_tap()

@step(u'tap in clear')
def step_impl(context):
    clicks_page.btn_clear_tap()
