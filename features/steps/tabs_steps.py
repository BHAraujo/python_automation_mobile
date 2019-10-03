from behave import step
from hamcrest import assert_that, equal_to

from pages.tabs_page import TabsPage

tabs_page = TabsPage()


@step(u'the tap in the menu Tabs')
def step_impl(context):
    tabs_page.menu_tabs_tap()

@step(u'redirect to option Tabs')
def step_impl(context):
    tabs_page.wait_tabs()

@step(u'tap in the second tab')
def step_impl(context):
    tabs_page.tab_second_tap()
