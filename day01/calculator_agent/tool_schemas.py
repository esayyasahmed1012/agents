
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate_subtotal",
            "description": (
                "Calculate the subtotal by multiplying"
                "the unit price by the quantity."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "price": {
                        "type": "number",
                        "description": "Unit price"
                    },
                    "quantity": {
                        "type": "integer",
                        "description": "Number of items"
                    }
                },
                "required": ["price", "quantity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_vat",
            "description": (
                "Calculate VAT from an amount and VAT percentage."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number"
                    },
                    "vat_rate": {
                        "type": "number"
                    }
                },
                "required": ["amount", "vat_rate"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_total",
            "description": (
                "Add the subtotal and VAT to calculate "
                "the final amount."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "subtotal": {
                        "type": "number"
                    },
                    "vat": {
                        "type": "number"
                    }
                },
                "required": ["subtotal", "vat"]
            }
        }
    }
]
