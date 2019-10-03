from behave import step
from hamcrest import equal_to, assert_that

from pages.forms_page import FormsPage

forms_page = FormsPage()


@step(u'the click in the menu Forms')
def step_impl(context):
    forms_page.menu_forms_tap()

@step(u'the title screen must be {title}')
def step_impl(context, title):
    assert_that(forms_page.get_title_forms(title), equal_to(True))

@step(u'fill of field name {name}')
def step_impl(context, name):
    forms_page.name_field_fill(name)

@step(u'select the option {console}')
def step_impl(context, console):
    forms_page.console_select(console)

@step(u'tap checkbox of date')
def step_impl(context):
    assert_that(forms_page.check_date_tap(), equal_to('true'))

@step(u'disable switch of time')
def step_impl(context):
    assert_that(forms_page.switch_time_tap(), equal_to('false'))

@step(u'tap in the button Lazy save')
def step_impl(context):
    forms_page.save_lazy_tap()

@step(u'validate following values')
def step_impl(context):
    for row in context.table:
        for keys in range(0, len(row)):
            assert_that(forms_page.verify_text_in_screen(row[keys]), equal_to(True))

@step(u'tap in the button clear')
def step_impl(context):
    forms_page.button_clear_tap()

@step(u'the grade must be cleaned')
def step_impl(context):
    assert_that(forms_page.verify_data_screen_clear("Nome:"), equal_to(False))
