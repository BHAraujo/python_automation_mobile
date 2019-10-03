from behave import step

from pages.swipe_list_page import SwipeListPage

swipe_list = SwipeListPage()


@step(u'the tap in the menu Swipe List')
def step_impl(context):
    swipe_list.menu_swipe_list_tap()

@step(u'redirect to options Swipe List')
def step_impl(context):
    swipe_list.wait_swipe_list()

@step(u'tap and left swipe all eight option and tap in the button less')
def step_impl(context):
    swipe_list.swipe_and_button_plus_tap()
