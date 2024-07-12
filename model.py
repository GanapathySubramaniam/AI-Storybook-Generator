from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv('.env')

import re

def extract_novel_info(text):
    # Extract novel title
    title_match = re.search(r'<title>(.*?)</title>', text, re.DOTALL)
    novel_title = title_match.group(1).strip() if title_match else "Unknown Title"

    # Extract chapter information
    chapter_pattern = re.compile(r'<chapter(\d+)>\s*<chapter\1 title>(.*?)</chapter\1 title>\s*<chapter\1 content>(.*?)</chapter\1 content>\s*</chapter\1>', re.DOTALL)
    chapters = chapter_pattern.findall(text)

    # Organize chapter information
    chapter_info = []
    for chapter_num, title, content in chapters:
        chapter_info.append({
            'number': int(chapter_num),
            'title': title.strip(),
            'content': content.strip()
        })

    # Sort chapters by number
    chapter_info.sort(key=lambda x: x['number'])

    return novel_title, chapter_info


class Chat:
    def __init__(self):
        self.client = Anthropic()
        self.messages = []
        with open('prompts/story_teller.txt') as f:
            self.system_instructions = f.read()

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def stream_chat(self, prompt_content):
        self.add_message('user', prompt_content)
        with self.client.messages.stream(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2500,
            temperature=1.0,
            system=self.system_instructions,
            messages=self.messages
        ) as stream:
            full_response = ""
            for chunk in stream:
                if chunk.type == "content_block_delta":
                    text = chunk.delta.text
                    yield text
                    full_response += text
        self.add_message('assistant',full_response)

    def clear_history(self):
        self.messages.clear()

    def get_story(self):
        return extract_novel_info(self.messages[-1]['content'])


    def get_history(self):
        return self.messages

class image_gen_model:
    def __init__(self):
        self.openai_client=OpenAI()
        self.size="1024x1024"
        self.quality="standard"
        self.style='vivid' 
        self.edit_image_size='1024x1024'

    def generate_image(self,prompt):
        response = self.openai_client.images.generate(
                                                model="dall-e-3",
                                                prompt=prompt,
                                                size=self.size,
                                                quality=self.quality,
                                                style=self.style,
                                                n=1,
                                                response_format='url')
        image_url = response.data[0].url
        return image_url



def tts(prompt):
    file_name='tts.mp3'
    openai_client=OpenAI()
    male_response = openai_client.audio.speech.create(model="tts-1",voice='onyx',input=str(prompt[0]['text']))
    male_response.write_to_file(f'{file_name}')
    return file_name
