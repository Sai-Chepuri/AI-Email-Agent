# AI Email Agent

An AI-powered Python email assistant that reads unread Gmail messages, extracts content, and generates concise, structured summaries using LLMs (Gemini). The goal is to automate email digestion and build a foundation for production-grade AI agent engineering.

---

## Features (MVP)

- **Secure Connection**: Connects securely to Gmail API using OAuth.
- **Smart Fetching**: Fetches unread emails from the Primary inbox.
- **Data Extraction**: Extracts sender, subject, and body content.
- **AI-Powered**: Sends email content to LLM for summarization.
- **Terminal Output**: Generates a clean, readable daily summary in the terminal.
- **Modular Design**: Modular architecture for easy extension.

---

## How It Works

1. **Authenticate**: Authenticate with Gmail API (OAuth2).
2. **Fetch**: Fetch unread emails.
3. **Parse**: Parse email content (subject, sender, body).
4. **Preprocess**: Preprocess email text.
5. **Summarize**: Send structured prompt to Gemini API.
6. **Output**: Receive and display summarized digest.

---

## Tech Stack

- **Language**: Python 3.x
- **APIs**: Gmail API (Google Cloud), Gemini API (or OpenAI compatible LLM)
- **Auth**: Google OAuth 2.0
- **Environment**: VS Code

---

## Installation

Clone the repository and set up the virtual environment:

```bash
# Clone the repository
git clone https://github.com/Sai-Chepuri/AI-Email-Agent.git
cd AI-Email-Agent

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Mac/Linux:
source venv/bin/activate 
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Setup (Gmail API)

1. Enable the **Gmail API** in your Google Cloud Console.
2. Download your `credentials.json` file.
3. Place `credentials.json` directly in the project root directory.
4. Run the project to trigger the authentication flow on first execution.

---

## Run the Project

Execute the main script to start the application:

```bash
python main.py
```

The script will automatically:
- Authenticate Gmail
- Fetch unread emails
- Generate AI summaries
- Print the digest in your terminal

---

## Next Improvements (In Progress)

### Email Cleaning (Planned)
- HTML cleaning using BeautifulSoup.
- Remove tracking pixels & links.
- Strip out unsubscribe/footer sections.
- Clean repeated whitespace & invisible characters.

### Summary Improvements
- Better prompt engineering.
- Structured output (bullet points, categories).
- Sender-based grouping.

## Future Roadmap

- [ ] Scheduled daily runs (cron / cloud scheduler).
- [ ] Email digest sent back to user inbox.
- [ ] Web dashboard (React / Angular).
- [ ] Voice summaries (TTS integration).
- [ ] Multi-agent workflow (filtering, prioritization, categorization).
- [ ] Mobile-friendly notification summaries.

---

## Project Goal

This project is part of a broader journey to learn:
- AI agent engineering.
- LLM application design.
- Production-ready automation pipelines.
- Real-world DevOps + cloud deployment patterns.

---

## Contributing

Contributions are welcome. Feel free to open issues or submit PRs for:
- Better email parsing
- Prompt improvements
- UI/dashboard ideas
- Performance optimization

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
