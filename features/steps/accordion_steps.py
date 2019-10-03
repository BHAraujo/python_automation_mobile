from behave import step
from hamcrest import assert_that, equal_to

from pages.accordion_page import AccordionPage

accordion_page = AccordionPage()


@step(u'the tap in the menu Accordion')
def step_impl(context):
    accordion_page.menu_accordion_tap()

@step(u'redirect to option Accordion')
def step_impl(context):
    accordion_page.wait_accordion()

@step(u'screen accordion must get following message {message}')
def step_impl(context, message):
    assert_that(accordion_page.verify_text_in_screen(message), equal_to(False))

@step('tap in the following Opção 1')
def step_impl(context):
    accordion_page.options_one_tap()

@step('tap in the following Opção 2')
def step_impl(context):
    accordion_page.options_two_tap()

@step('tap in the following Opção 3')
def step_impl(context):
    accordion_page.options_three_tap()

@step('tap in the following Opção 4')
def step_impl(context):
    accordion_page.options_four_tap()

@step('tap in the following Opção 5')
def step_impl(context):
    accordion_page.options_five_tap()

@step('tap in the following Opção 6')
def step_impl(context):
    accordion_page.options_six_tap()
