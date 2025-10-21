# Import the Sheet class
from src.sheet import Sheet


def test_cell_returns_empty_string_by_default():
    # Arrange
    sheet = Sheet()

    # Act
    value = sheet.get('A1')

    # Assert
    assert value == ""
