from behave import step

from pages.swipe_page import SwipePage

swipe_page = SwipePage()


@step(u'the tap in the menu Swipe')
def step_impl(context):
    swipe_page.menu_swipe_tap()

@step(u'redirect to screen Swipe')
def step_impl(context):
    swipe_page.wait_menu_swipe()

@step(u'screen Swipe must get following message {message}')
def step_impl(context, message):
    swipe_page.verify_text_in_screen(message)

@step(u'tap and left swipe')
def step_impl(context):
    swipe_page.swipe_screen_tap([800, 300, 200, 0])
