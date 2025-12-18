import os
import google.generativeai as genai
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class ActionGPTFallback(Action):

    def name(self):
        return "action_gpt_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        user_message = tracker.latest_message.get('text')

        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            prompt = f"You are a helpful customer support assistant. Keep responses brief and friendly. User asks: {user_message}"
            response = model.generate_content(prompt)
            bot_reply = response.text.strip()
            
        except Exception as e:
            print(f"Gemini API Error: {e}")
            bot_reply = "Sorry, I can only help with customer support questions about working hours, orders, and refunds."

        dispatcher.utter_message(text=bot_reply)
        return []