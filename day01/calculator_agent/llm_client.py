# import requests
# OLLAMA_URL = "http://localhost:11434/api/chat"
# MODEL = "qwen2.5:3b"
# def chat(user_massage:str)->str:
#     payload = {
#         "model": MODEL,
#         "messages": [
#             {"role": "user", "content": user_massage}
#         ],
#         "stream": False
#     }
#     response=requests.post(
#         OLLAMA_URL,
#         json=payload,
#         timeout=180
#     )
#     response.raise_for_status()
#     data=response.json()
#     return data["message"]["content"], data["message"]["role"]
# if __name__ == "__main__":

#     question = "Explain what an AI agent is."
   
#     answer = chat(question)

#     print("\nLLM RESPONSE:")
#     print(answer)


import requests

from calculator_agent.tool_schemas import TOOLS


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"


def ask_llm(messages):

    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": TOOLS,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    return response.json()["message"]


if __name__ == "__main__":

    messages = [
        {
            "role": "user",
            "content": "Calculate the total not the subtotal with 15% vat cost for 15 laptops at $800 each."
        }
    ]

    result = ask_llm(messages)

    print("\nMODEL MESSAGE:")
    print(result)

    print("\nTOOL CALLS:")

    for tool_call in result.get("tool_calls", []):
        print(tool_call["function"]["name"])
        print(tool_call["function"]["arguments"])
