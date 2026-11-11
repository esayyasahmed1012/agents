from calculator import calculate_total
def agent(user_request:str):
    print("User request:", user_request)
    # simulate the llm decicion
    decision={
        "tool":"calculate_total",
        "arguments":{
            "price": 10.0,
            "quantity": 5
        }
    }
    print("\nAgent selected tool:", decision["tool"])
    #excute the selected tool
    if decision["tool"]=="calculate_total":
        arguments=decision["arguments"]
        result=calculate_total(price=arguments["price"], quantity=arguments["quantity"])
    else:
        raise ValueError("Unknown tool selected by the agent.")
    #observe the total result
    response =f"the total cost is: ${result:.2f}"
    return response
if __name__ == "__main__":
    question="What is the total cost for 50 items priced at $10 each?"
    print("User question:", question)
    response=agent(question)
    print("Agent response:", response)