import random
import gradio as gr
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

def random_response(message, history):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="model_ID",
    )
    return chat_completion.choices[0].message.content

demo = gr.ChatInterface(random_response, type="messages", autofocus=False)

if __name__ == "__main__":
    demo.launch(share=True)



