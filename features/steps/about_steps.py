import sys
sys.path.append('..')

from behave import step
from hamcrest import assert_that, equal_to
from time import sleep

from pages.about_page import AboutPage, BasePage

about_page = AboutPage()
base_page = BasePage()

@step(u'the tap in the menu About')
def step_impl(context):
    about_page.menu_about_tap()

@step(u'seen the image of course')
def step_impl(context):
    about_page.screenshot_image_course("image_course.png")

@step(u'tap in the link {message}')
def step_impl(context, message):
    about_page.show_course_tap()

@step(u'must be open webbrowser Chrome')
def step_impl(context):
    sleep(5)
    base_page.take_screenshot("about", "chrome.png")
    assert_that('.WebViewBrowserActivity',
                    equal_to(base_page.get_current_activity()))
