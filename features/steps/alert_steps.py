from behave import step
from hamcrest import assert_that, equal_to

from pages.alerts_page import AlertsPage

alerts_page = AlertsPage()


@step(u'the tap in the menu Alerts')
def step_impl(context):
    alerts_page.menu_alerts_tap()

@step(u'redirect to option Alerts')
def step_impl(context):
    alerts_page.wait_element_alert()

@step(u'tap in the following button Simple Alert')
def step_impl(context):
    alerts_page.simple_alerts_tap()

@step(u'must show the message {message}')
def step_impl(context, message):
    assert_that(alerts_page.verify_alert_text(message), equal_to(True))

@step(u'tap button ok')
def step_impl(context):
    alerts_page.button_ok_simple_alert_click()

@step(u'tap int the Restrict Alert')
def step_impl(context):
    alerts_page.restrict_alert_tap()

@step(u'tap in the button sair')
def step_impl(context):
    alerts_page.button_sair_tap()

@step(u'tap int the Confirm Alert')
def step_impl(context):
    alerts_page.confirm_alert_tap()

@step(u'tap in the button confirmar')
def step_impl(context):
    alerts_page.button_ok_tap()

@step(u'tap in the button deny')
def step_impl(context):
    alerts_page.button_ok_tap()
