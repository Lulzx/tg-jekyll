import os
import logging
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from git import Repo

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
REPO_PATH = '/path/to/local/repo'
GITHUB_TOKEN = 'YOUR_GITHUB_PERSONAL_ACCESS_TOKEN'
GITHUB_REPO = 'https://github.com/yourusername/your-repo.git'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

openai.api_key = OPENAI_API_KEY

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        stop=None
    )
    return response.choices[0].text.strip()

def generate_title(post_content):
    title_prompt = f"Generate a title for a blog post about the following content:\n{post_content}"
    return generate_text(title_prompt)

def generate_category(post_content):
    category_prompt = f"Generate a category for a blog post about the following content:\n{post_content}"
    return generate_text(category_prompt)

def create_and_push_blog_post(filename, content):
    file_path = os.path.join(REPO_PATH, 'blog', '_posts', filename)
    
    front_matter = (
        "---\n"
        f"layout: post\n"
        f"title: \"{generate_title(content)}\"\n"
        f"date: {{% raw %}}{{{{ now | date: '%Y-%m-%d %H:%M' }}}}{% endraw %}\n"
        "comments: true\n"
        f"categories: {generate_category(content)}\n"
        "---\n"
    )
    full_content = f"{front_matter}\n{content}"

    with open(file_path, 'w') as file:
        file.write(full_content)

    repo = Repo(REPO_PATH)
    repo.git.add(file_path)
    repo.git.commit('-m', f'Added blog post {filename}')
    repo.git.push('origin', 'master')

@dp.message_handler(content_types=types.ContentTypes.TEXT, chat_type='channel')
async def handle_channel_post(message: types.Message):
    if message.chat.username == 'your_channel_username':
        post_content = message.text

        filename = f'blog_post_{message.message_id}.md'
        create_and_push_blog_post(filename, post_content)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
