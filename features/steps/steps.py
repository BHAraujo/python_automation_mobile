import sys
sys.path.append('..')

from behave import step
from hamcrest import assert_that, equal_to

from pages.base_page import BasePage
from time import sleep

@step(u'the activity must get message "{message}"')
def step_impl(context, message):
    if message in "Você achou essa opção" or "Negado":
        sleep(2)
    assert_that(BasePage().verify_text_in_activity(message), equal_to(True))


@step(u'the activity must not get message {message}')
def step_impl(context, message):
    assert_that(BasePage().verify_text_in_activity(message), equal_to(False))
