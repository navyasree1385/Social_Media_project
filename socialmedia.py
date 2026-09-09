import asyncio
import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, WebSearchTool, function_tool, ItemHelpers, set_default_openai_client, set_default_openai_api
from openai import OpenAI, AsyncOpenAI
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import List


#step 2: gemini api key and configure
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL","https://generativelanguage.googleapis.com/v1beta/openai/")

#step 3
gemini_async_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL,
)
set_default_openai_client(gemini_async_client)
set_default_openai_api("chat_completions")

#Synchronous client for tools
gemini_sync_client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL,
)
#step 4 defining tools for agents
#tool: generate social media content from transcript
@function_tool
def generate_content(video_transcript: str, social_media_platform: str):
    print(f"Generating social media content for {social_media_platform}...")
    response = gemini_sync_client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=[
            {"role": "user", "content": f"Here is a new video transcript:\n"
                                        f"Generate social media post on {social_media_platform} based on the following transcript:\n\n{video_transcript}"},
        ],
        max_tokens=2500,
    )
    return response.choices[0].message.content
#step 5 defining the agent
@dataclass
class Post:
    Platform: str
    content:str

content_writer_agent = Agent(
    name="Content Writer Agent",
    instructions="""You are a talented content writer who writes engaging highly readable social media posts. You will be given a video transcript and social media platform, then create a compelling post. You will generate a social media post based on the video transcript and social media platform. You may search the web for up-to-date information
                    according to the platform and fill in some useful details if needed.""",
    model="gemini-3.5-flash",               
    tools=[generate_content],

    output_type=List[Post],
)
#step 6 define helper functions
#fetch transcript from a youtube video using the video id
def get_transcript(video_id: str, languages: list = None) -> str:
    """
    Fetch the transcript of a YouTube video given its video ID.
    """

    if languages is None:
        languages = ["en"]

    try:
        # Create YouTube Transcript API client
        ytt_api = YouTubeTranscriptApi()

        # Fetch transcript using the current API
        fetched_transcript = ytt_api.fetch(
            video_id,
            languages=languages
        )

        # Combine all transcript snippets
        transcript_text = " ".join(
            snippet.text for snippet in fetched_transcript
        )

        return transcript_text

    except Exception as e:
        error_msg = f"An unexpected error occurred while fetching transcript: {str(e)}"
        print(f"Error: {error_msg}")
        raise Exception(error_msg) from e
        
#step 7 run the agent
async def main():
    video_id="3bVjLdI3C1k"
    transcript = get_transcript(video_id)
    msg = f"Generate a LinkedIn post and an Instagram caption based on the transcript "

    #package input for the agent
    input_items = [{"content": msg, "role": "user"}]
    #run content writer agent
    with trace("Writing content"):
        result = await Runner.run(content_writer_agent, input=input_items)
        output = ItemHelpers.text_message_outputs(result.new_items)
        print("Generated Post:\n", output)

if __name__ == "__main__":
    asyncio.run(main())            
    
    