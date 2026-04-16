from behave import *
from utils.data_reader import DataReader
from utils.model_simulator import predict_risk
from utils.db_client import DBClient
from utils.logger import Logger


@when("I send data to model")
def step(context):
    context.result = predict_risk(context.input_text)
    Logger.info(f"Model output: {context.result}")
    Logger.info(f"Input: {context.input_text} | Output: {context.result}")


@then("output should not be empty")
def step(context):
    assert context.result is not None, "Model output is None"


@then("output should be valid")
def step(context):
    valid = ["HighRisk", "MediumRisk", "LowRisk", "Unknown"]
    assert context.result in valid, f"Invalid output: {context.result}"


@then('output should be as expected')
def step(context):
    assert context.result.lower() == context.expected.lower(), f"Expected {context.expected}, got {context.result}"


@then("model output should be stored in DB")
def step(context):

    if context.env == "dev":
        return
    db = DBClient(context.db_config)
    db.connect()
    record = db.fetch_order("MODEL_RESULT")
    db.close()
    assert record is not None

