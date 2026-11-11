
from decimal import Decimal
from inspect import signature

from tools import (
    calculate_subtotal,
    calculate_vat,
    calculate_total,
)


# Only these functions are available to our agent.
TOOL_REGISTRY = {
    "calculate_subtotal": calculate_subtotal,
    "calculate_vat": calculate_vat,
    "calculate_total": calculate_total,
}


# Arguments that must be converted to Decimal.
DECIMAL_FIELDS = {
    "price",
    "amount",
    "vat_rate",
    "subtotal",
    "vat",
}

def execute_tool(tool_name: str, arguments: dict):

    # 1. Check whether the requested tool exists.
    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        raise ValueError(f"Unknown tool: {tool_name}")

    # 2. Check the argument structure.
    if not isinstance(arguments, dict):
        raise TypeError("Tool arguments must be a dictionary.")

    # 3. Convert financial values into Decimal.
    converted_arguments = {}

    for key, value in arguments.items():
        if key in DECIMAL_FIELDS:
            converted_arguments[key] = Decimal(str(value))
        else:
            converted_arguments[key] = value
    # 4. Validate required and unexpected arguments.
    signature(tool).bind(**converted_arguments)

    # 5. Execute the approved function.
    return tool(**converted_arguments)
