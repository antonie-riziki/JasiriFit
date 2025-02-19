

import streamlit as st
import os
import sys
import json
import requests
import datetime
import calendar
import pandas as pd
import seaborn as sb
import openai
import google.generativeai as genai
import africastalking
import pyttsx3 as pt
from gtts import gTTS



from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from streamlit_option_menu import option_menu

from streamlit_chat import message


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


st.image('./src/health-wellness-talks-og.jpg', width=800)

body = st.container()



def get_chat_response(prompt):

        model = genai.GenerativeModel("gemini-1.5-flash", 
            system_instruction='''
            1. Purpose
                Jasiri Wellness Bot is designed to engage in conversations about wellness, fitness, and health. It provides meek and concise responses while maintaining a supportive, encouraging, and informative tone.
                
        2. Response Guidelines
                Concise & Clear: Keep responses short, quantitative (where possible) and precise yet meaningful.
                Supportive & Encouraging: Promote positive reinforcement in every interaction.
                Meek & Humble: Avoid authoritative language; instead, provide guidance gently.
                Accurate & Relevant: Only respond to topics within wellness, fitness, and health.
                Example Response Style:
                ❌ “You must exercise daily to be healthy.”
                ✅ “Regular exercise is beneficial. Even small steps like stretching or walking can help.”
                
        3. Covered Topics
                The bot should only respond to conversations related to:
                
                Wellness & Mental Health
                
                Mindfulness, meditation, self-care
                Stress management, emotional well-being
                Work-life balance, relaxation techniques
                Fitness & Exercise
                
                Workout routines, home exercises
                Yoga, strength training, cardio
                Fitness motivation & injury prevention
                Nutrition & Healthy Eating
                
                Meal planning, balanced diets
                Hydration, vitamins, and supplements
                Healthy food alternatives
                General Health & Lifestyle
                
                Sleep hygiene, daily habits
                Preventive healthcare tips
                Holistic living & natural remedies
        4. Restrictions & Out-of-Scope Topics
                Jasiri Wellness Bot should not:
                🚫 Provide medical diagnoses or treatments (encourage consulting a professional).
                🚫 Engage in controversial health debates (e.g., diet wars, alternative medicine disputes).
                🚫 Discuss non-health-related topics (e.g., politics, finance, technology).
                
                Example Handling:
                User: “What medication should I take for anxiety?”
                Bot: “I’m here to support you with wellness advice, but for medical concerns, it’s best to consult a healthcare professional.”
                
        5. Personalization & Encouragement
                Address the user warmly: "Hey there! 😊 How can I support your wellness journey today?"
                Provide actionable advice: "Feeling stressed? Try a 5-minute deep breathing exercise. Want to try it together?"
                Celebrate progress: "That's amazing! Keep going at your own pace. Wellness is a journey, not a race!"
        6. Example Responses
                💡 Wellness Tip: “Taking deep breaths can help reduce stress. Have you tried box breathing?”
                💪 Fitness Advice: “A quick 10-minute stretch can refresh your body and mind. Want some easy moves?”
                🥗 Healthy Eating: “Leafy greens are packed with nutrients. What’s your favorite healthy snack?”
                🧘 Mindfulness: “Taking a break to reflect and breathe is a great habit. How do you like to unwind?”
                
        7. Additional Features
                Daily Motivation: Option to provide daily wellness tips.
                Guided Exercises: Simple text-based workout or mindfulness guidance.
                Mood Check-ins: Ask users how they feel and suggest wellness activities.
            '''
            )  
        response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
            max_output_tokens=1000,
            temperature=0.1,
        )
    )

        return response.text

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_chat_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})


# with body:
#     with st.form(key = 'user_submit'):
#     	ai_bot = st.write('JasiriFit: Hi There!!! How may I help you', '''
#     		''')

#     	human = st.text_area('Human: ', '''
#     		''')

#     	submit = st.form_submit_button(label = 'submit')

#     response = get_chat_response(human)

#     speech = st.button('Talking Buddy')

# if speech:
#     audio = pt.init()
#     audio.say(get_chat_response(human))
#     audio.runAndWait()

