import pytest

from pydotfiles.models.validator import Validator, ConfigMapper
from pydotfiles.models.exceptions import ValidationError
from tests.test_models.validation import load_test_data


"""
ConfigMapper tests
"""


def test_successful_loading_schema_alpha_core():
    # System under test
    schema = ConfigMapper.get_schema("alpha", "core")

    # Verification
    assert schema is not None
    assert schema.get("type") == "object"

    assert schema.get("allOf") is not None
    assert len(schema.get("allOf")) == 2

    assert schema.get("allOf")[0] is not None
    assert schema.get("allOf")[0].get("$ref") is not None
    assert schema.get("allOf")[0].get("$ref") == "./common.json"

    assert schema.get("allOf")[1] is not None
    assert schema.get("allOf")[1].get("properties") is not None

    assert schema.get("allOf")[1].get("properties").get("os") is not None
    assert schema.get("allOf")[1].get("properties").get("actions") is not None
    assert schema.get("allOf")[1].get("properties").get("environments") is not None


"""
Validator tests
"""


def test_invalid_schema_no_version():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_no_version.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_no_schema_type():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_no_schema_type.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_action_no_action():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_actions_no_action.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_action_no_files():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_actions_no_files.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_action_invalid_action():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_actions_invalid_action.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_environments_no_name():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_environments_no_name.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_environments_invalid_name():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_environments_invalid_name.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_os_no_name():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_os_no_name.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_invalid_schema_os_invalid_name():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "invalid_schema_os_invalid_name.json")

    # System under test
    with pytest.raises(ValidationError):
        validator.validate_data(data)


def test_valid_schema_actions():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "valid_schema_actions.json")

    # System under test
    validator.validate_data(data)


def test_valid_schema_os():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "valid_schema_os.json")

    # System under test
    validator.validate_data(data)


def test_valid_schema_environments():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "valid_schema_environments.json")

    # System under test
    validator.validate_data(data)


def test_valid_schema_all():
    # Setup
    validator = Validator()
    data = load_test_data("alpha.core", "valid_schema_all.json")

    # System under test
    validator.validate_data(data)
