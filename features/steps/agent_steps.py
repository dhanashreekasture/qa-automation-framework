from behave import *
from utils.data_reader import DataReader
from utils.validator import Validator
from utils.api_client import APIClient
from utils.db_client import DBClient
from utils.logger import Logger
from utils.payload_builder import PayloadBuilder


@given('I load data for "{scenario_id}" "{test_case_id}"')
def step(context, scenario_id, test_case_id):
    # get the sheet name from feature tag
    sheet_tag = [tag for tag in context.feature.tags if tag.startswith("sheet:")]
    if not sheet_tag:
        raise Exception("Sheet name tag missing. Use @sheet:<SheetName>")
    sheet_name = sheet_tag[0].split(":")[1]

    # read the data from the test data file and mentioned sheet
    data = DataReader.get(sheet_name, scenario_id, test_case_id)
    context.data = data

    # Build payload (only for API use)
    context.payload = PayloadBuilder.build(data)

    for key, value in data.items():
        setattr(context, key.lower(), value)
    Logger.info(f"[{sheet_name}] Loaded data: {data}")
    Logger.info(f"Payload: {context.payload}")


@when("I validate data")
def step(context):
    context.errors = Validator.validate(context.data)


@then('validation result should be as expected')
def step(context):
    if context.expected == "pass":
        assert not context.errors, f"Validation errors: {context.errors}"
    else:
        assert context.errors


@when("I call backend")
def step(context):
    if not context.payload:
        raise Exception("Payload is empty")
    response = APIClient.request("POST",context.base_url + "/orders",context.payload)
    context.response = response
    context.order_id = response.json().get("id")


@then("data should be stored in DB")
def step(context):
    if context.env == "dev":
        return
    db = DBClient(context.db_config)
    db.connect()
    record = db.fetch_order(context.order_id)
    db.close()
    assert record is not None


@then("sensitive data should be masked")
def step(context):
    ssn = getattr(context, "ssn", None) or context.data.get("ssn")
    assert ssn is not None, "SSN not found in context"
    assert "***" in ssn, f"SSN not masked: {ssn}"