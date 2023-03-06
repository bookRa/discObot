from os.path import join, dirname

import openai
import os

from dotenv import load_dotenv

# pull env vars from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
openai.api_key = os.getenv("SECRET_OPENAI_TOKEN")
print(openai.api_key)


GPT_PROMPT_PREFIX =(
    "I will provide you with the lyrics to a song. Your job is to create a series of midjourney prompts that will"
    "lead to a satisfying music video. Each midjourney prompt creates a new image. Midjourney (MJ) is a text-to-image"
    " model.\n"
    "So, you will interpret the lyrics and generate imagery to go along with the song.\n\n"
    "The following is the format of a midjourney prompt:\n\n"
    ""
    "Create a descriptive block of text for subject or concept [1] to be input as a complex prompt for an AI art "
    "generation program such as MidJourneyAI. Use the following logic to construct the prompt:\n"
    "Use epic, powerful and evocative terms that will generate images in a hyper realistic style, incorporating "
    "cinematography, staging and photography terminology and elements of the scene or environment. You can also"
    "incorporate terms such as these: "
    "`High resolution` , `hyper realism`, `photo realistic`, `true-to-life`,`well composed`\n\n"
    "---- START PROMPT TEMPLATE----\n\n"
    "`A professional photoshoot using a [2] to capture [1] from a [3]. [4] [5] [6] [7] [8]`\n\n"
    "---- END PROMPT TEMPLATE----\n\n"
    "where [2] is a high-end camera system used for filming feature productions or professional photography"
    "where [3] is a description of the camera placement and angle\n"
    "where [4] is a very descriptive sentence of what action the subject is performing\n"
    "where [5] is a composition style for the scene using complementary colors\n"
    "where [6] is a lighting style and placement\n"
    "where [7] is a mood or theme for the scene that complements the lighting choice\n"
    "where [8] is a series of flags to modify the image output. it should always include `--ar 7:4` and "
    " about 1/4 of prompts should also include `--version 3 --video`\n\n"
    " So, to reiterate, I am going to provide lyrics, then you craft a spellbinding music video by creating "
    "perfect midjourney prompts.\n\n"
    "LYRICS: \n\n"
)

def generate_text(prompt):
    # Generate text with the GPT-3 model
    print(f":::full prompt is:::\n\n {''.join(GPT_PROMPT_PREFIX) + prompt}")
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt="".join(GPT_PROMPT_PREFIX) + prompt,
        max_tokens=2049,
        stop=None,
        temperature=0.5,
    )

    # Return the generated text
    return response.choices[0].text


teapot = generate_text("I'm a little teapot, short and stout\nHere is my handle, here is my spout\nWhen I get all steamed up, hear me shout\nJust tip me over and pour me out!\n")
print(teapot)