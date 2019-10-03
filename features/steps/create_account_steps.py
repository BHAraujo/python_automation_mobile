from behave import step
from time import sleep
from hamcrest import assert_that, equal_to
from faker import Faker

from pages.create_account_page import CreateAccountPage

faker = Faker()
create_account = CreateAccountPage()


@given(u'the tap in the menu SeuBarriga Híbrido')
def step_impl(context):
    create_account.menu_hidrido_tap()

@step('redirect to option SeuBarriga Híbrido')
def step_impl(context):
    create_account.wait_menu_create_account()

@step(u'tap in Novo usuário?')
def step_impl(context):
    create_account.new_user_tap()

@step(u'fill field name with value {value}')
def step_impl(context, value):
    context.get_name = faker.last_name()
    create_account.field_name_send_keys(context.get_name)

@step(u'fill field email with value {value}')
def step_impl(context, value):
    context.get_email = faker.email()
    create_account.field_email_send_keys(context.get_email)

@step(u'fill field senha with value {value}')
def step_impl(context, value):
    context.get_password = faker.hex_color()
    create_account.field_password_send_keys(context.get_password)

@step(u'tap in the button Cadastrar')
def step_impl(context):
    create_account.button_save_tap()

@step(u'screen create account must show message {message}')
def step_impl(context, message):
    sleep(3)
    if message in '"Bem vindo, $NAME_VALUE!"':
        message = f"Bem vindo, {context.get_name}!"

    assert_that(create_account.verify_text_in_screen(message), equal_to(True))

@step(u'do the login')
def step_impl(context):
    create_account.do_login(context.get_email, context.get_password)
