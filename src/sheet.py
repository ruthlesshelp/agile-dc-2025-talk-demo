"""Sheet implementation for the spreadsheet engine."""


class Sheet:
    def get(self, cell_ref: str) -> str:
        """Get the calculated value of a cell."""
        return ""

    def set(self, cell_ref: str, value: str) -> None:
        """Set the value of a cell."""
        raise NotImplementedError("Sheet.set() not implemented")

    def get_literal(self, cell_ref: str) -> str:
        """Get the raw/literal value of a cell for editing."""
        raise NotImplementedError("Sheet.get_literal() not implemented")