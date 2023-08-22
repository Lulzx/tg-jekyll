# Telegram Bot for Automated Blog Posts

This Telegram bot automates the process of creating blog posts from updates in a Telegram channel. It generates markdown files for blog posts and pushes them to a GitHub repository.

## Features

✉️ Listens to updates in a Telegram channel.

📝 Generates blog post titles using OpenAI GPT-3.

🗂️ Organizes posts in the `/blog/_posts` directory structure.

📦 Pushes generated posts to a GitHub repository.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Lulzx/tg-jekyll.git
   cd tg-jekyll
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot by creating a bot on Telegram and obtaining the API token.

4. Configure your GitHub repository and obtain a personal access token.

5. Obtain an API key for OpenAI's GPT-3 API.

6. Update the `main.py` file with your API tokens and paths.

## Usage

1. Invite your bot to the target Telegram channel with appropriate permissions.

2. Run the bot using:
   ```bash
   python3 telegram_bot.py
   ```

3. The bot will automatically listen to updates in the channel and generate blog posts.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.

🚀 Happy blogging with your automated Telegram bot!
