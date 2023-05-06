import os
import openai
openai.api_key = "Your-GPT4-Key-Here"
model_engine = "gpt-4"

while True:
    input_text = []
    print("Type A Message And Use !fin Once Finished, or type 'exit' to exit")
    while True:
        user_input = input("")
        if user_input == "!fin":
            break
        if user_input == "exit":
            exit()
        input_text.append(user_input)

    input_text = "\n".join(input_text).replace("!fin", "")

    response = openai.ChatCompletion.create(
       model=model_engine,
       messages=[{"role": "user", "content": input_text }]
    )

    output_text = response['choices'][0]['message']['content']
    print("ChatGPT API reply:", output_text)