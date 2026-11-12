
from calculator_agent.llm_client import ask_llm
from calculator_agent.tool_registry import execute_tool


MAX_TOOL_ROUNDS = 6


def run_agent(user_request: str) -> str:

    messages = [
        {
            "role": "user",
            "content": user_request
        }
    ]

    for round_number in range(MAX_TOOL_ROUNDS):

        print(f"\n--- Agent Round {round_number + 1} ---")

        # Step 1: Ask the LLM what to do next
        assistant_message = ask_llm(messages)

        # Step 2: Save the assistant's response
        messages.append(assistant_message)

        # Step 3: Check whether the LLM requested tools
        tool_calls = assistant_message.get("tool_calls", [])

        # Step 4: If no tools are requested, return the final answer
        if not tool_calls:
            return assistant_message.get("content", "")

        # Step 5: Execute each requested tool
        for tool_call in tool_calls:

            function_info = tool_call["function"]

            tool_name = function_info["name"]
            arguments = function_info["arguments"]

            print(f"Executing tool: {tool_name}")
            print(f"Arguments: {arguments}")

            try:
                result = execute_tool(tool_name, arguments)
                tool_result = str(result)

                print(f"Tool result: {tool_result}")

            except Exception as error:
                tool_result = (
                    f"Tool execution failed: "
                    f"{type(error).__name__}: {error}"
                )

                print(tool_result)

            # Step 6: Send the tool result back to the LLM
            messages.append(
                {
                    "role": "tool",
                    "content": tool_result
                }
            )

    raise RuntimeError(
        "Agent stopped because it exceeded the maximum tool rounds."
    )


if __name__ == "__main__":

    question = (
        "Calculate the VAT at 20% for 15 items priced at $800 each, "
        "and then calculate the total amount including VAT."
    )

    answer = run_agent(question)

    print("\n========== FINAL ANSWER ==========")
    print(answer)
