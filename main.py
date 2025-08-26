import os
from agents import Runner, OpenAIChatCompletionsModel, set_tracing_disabled,Agent
from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")
my_base_url =os.getenv("BASE_URL")
# print(my_key,base_url)

client = AsyncOpenAI(
    api_key= my_key,
    base_url= my_base_url
)    
MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

english_agent= Agent(
    name="english tutor",
    model= MODEL,
    instructions="You are a helpful agent which will help users related to there english. dont answer questions if they are not related to english."
)

set_tracing_disabled(True)
result = Runner.run_sync(
    starting_agent= english_agent,
    input = ""
)

print(result.final_output)