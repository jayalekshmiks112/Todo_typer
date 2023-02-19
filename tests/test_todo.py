import json

import pytest
from typer.testing import CliRunner
from todo import (
    DB_READ_ERROR,
    SUCCESS,
    __app_name__,
    __version__,
    cli,
    todo,
)

runner= CliRunner()

def test_version():
    result= runner.invoke(cli.app,["--version"])
    assert result.exit_code ==0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

@pytest.fixture
def mock_json_file(tmp_path):
    todo1 = [{"Description": "Get some milk.", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo1, db, indent=4)
    return db_file

test_data1 = {
    "description": ["Clean", "the", "house"],
    "priority": 1,
    "todo": {
        "Description": "Clean the house.",
        "Priority": 1,
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "priority": 2,
    "todo": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}