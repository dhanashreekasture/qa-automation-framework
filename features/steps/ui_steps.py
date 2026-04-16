from behave import *
from pages.upload_page import UploadPage


@given("user opens application")
def step(context):
    context.page = UploadPage(context.driver)


@when("user uploads invalid file")
def step(context):
    context.page.upload_file("invalid.txt")


@then("error message should appear")
def step(context):
    error = context.page.get_error_message()
    assert "Invalid" in error, f"Unexpected error: {error}"