from behave import step

from pages.drag_drop_page import DragDropPage

drag_drop = DragDropPage()


@step(u'the tap in the menu Drag Drop')
def step_impl(context):
    drag_drop.menu_drag_drop_tap()

@step(u'redirect to option Drag Drop')
def step_impl(context):
    drag_drop.wait_drag_drop()

@step(u'Drag {first_message} and Drop {second_message}')
def step_impl(context, first_message, second_message):
    drag_drop.drag_and_drop_elements(first_message, second_message)

@step(u'take a screenshot e compare with screenshot origin')
def step_impl(context):
    drag_drop.take_screenshot_save()
