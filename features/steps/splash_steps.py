from behave import step
from hamcrest import assert_that, equal_to

from pages.splash_page import SplashPage

splash_page = SplashPage()


@step(u'the tap in the menu Splash')
def step_impl(context):
    splash_page.menu_splash_tap()

@step(u'redirect to option Splash')
def step_impl(context):
    splash_page.wait_message_splash()
