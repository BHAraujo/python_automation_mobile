import sys
sys.path.append('..')

from behave import step
from hamcrest import assert_that, equal_to

from pages.about_page import AboutPage

about_page = AboutPage()


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
    assert_that('org.chromium.chrome.browser.ChromeTabbedActivity',
                 equal_to(about_page.button_notification_browser_tap()))
