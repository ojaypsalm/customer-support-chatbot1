# Customer Support Chatbot 🤖

An AI-powered customer support chatbot built with Rasa and Streamlit, featuring intelligent FAQ handling and AI fallback for out-of-scope queries.

## Features

- ✅ FAQ handling for common queries (working hours, orders, refunds)
- ✅ AI-powered fallback using Google Gemini API
- ✅ Beautiful Streamlit web interface
- ✅ Custom actions for dynamic responses
- ✅ Rule-based conversation management

## Project Structure
```
y/
├── data/
│   ├── nlu.yml          # Training data for intent classification
│   └── stories.yml      # Conversation flows
├── actions.py           # Custom actions (AI fallback)
├── domain.yml           # Bot responses and intents
├── config.yml           # NLU pipeline configuration
├── rules.yml            # Rule-based policies
├── endpoints.yml        # Server endpoints configuration
├── app.py               # Streamlit UI
└── .env                 # Environment variables (NOT in repo)
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/customer-support-chatbot.git
cd customer-support-chatbot
```

### 2. Create virtual environment
```bash
python -m venv chatbotvenv
chatbotvenv\Scripts\activate  # Windows
# source chatbotvenv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from: https://aistudio.google.com/app/apikey

### 5. Train the model
```bash
rasa train
```

### 6. Run the chatbot

Open **3 terminals** in the project folder:

**Terminal 1 - Actions Server:**
```bash
rasa run actions
```

**Terminal 2 - Rasa Server:**
```bash
rasa run --enable-api --cors "*"
```

**Terminal 3 - Streamlit UI:**
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

## Testing without Streamlit

For command-line testing:

**Terminal 1:**
```bash
rasa run actions
```

**Terminal 2:**
```bash
rasa shell
```

## Technologies Used

- **Rasa Open Source** - Conversational AI framework
- **Streamlit** - Web UI framework
- **Google Gemini API** - AI fallback for out-of-scope queries
- **Python 3.10+** - Programming language

## Features I Can Help With

- 🕐 Working hours inquiries
- 📦 Order status tracking
- 💰 Refund requests
- ❓ General questions (AI-powered)

## Contributing

Feel free to fork this project and submit pull requests!

## License

MIT License

## Author

Built by OJO Samuel  Adekanmi - OAU Engineering Graduate, AI Enthusiast
