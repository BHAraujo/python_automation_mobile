from behave import step
from pages.option_page import OptionPage

option_page = OptionPage()


@step(u'the tap in the menu Option Successifuly')
def step_impl(context):
    option_page.menu_option_tap()
