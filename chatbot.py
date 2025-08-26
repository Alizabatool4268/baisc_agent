from agents import Runner
import chainlit as cl
from main import english_agent

@cl.on_message
async def main(msg:cl.Message):
    await cl.Message(content="").send()
    # my prompt
    prompt = msg.content
    # agent get
    result = Runner.run_sync(english_agent,prompt)
    await cl.Message(content=f"AI response: {result.final_output}").send()
    