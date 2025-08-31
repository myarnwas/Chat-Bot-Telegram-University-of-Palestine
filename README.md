# 🎓 University of Palestine Academic Assistant Bot

> 🤖 A Telegram-based academic assistant bot built with **Python 3.11** and **pyTelegramBotAPI**.  
It provides quick access to academic information such as **exam schedules, FAQs, grants, notifications, and interactive chat features** for students.

---

## ⚠️ Before You Start

1. **Fork the repository** to your own GitHub account.
2. Make sure you have **FFmpeg installed** and added to your system PATH for audio/video processing: [FFmpeg Download](https://ffmpeg.org/download.html)
3. Create a file named `telegram_token.json` in the project root with your bot token:
    ```json
   { "token": "YOUR_TELEGRAM_BOT_TOKEN" }
4.	To enable AI chat features, add your OpenAI API key in folder/file-name_functions.py:
    ```json
    { "api_key": "YOUR_OPENAI_KEY" }
•	If you skip this step, the bot will still function normally but without AI-enhanced chat.


⸻

## 🖥️ Dependencies / Libraries

Required Python libraries:

import sqlite3
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import telebot
from telebot import types
import os
import openai
from pypdf import PdfReader
from docx import Document as DocxDocument
from faster_whisper import WhisperModel
from pydub import AudioSegment


Install with pip:
    
    pip install sqlite3 apscheduler pyTelegramBotAPI openai pypdf2 python-docx faster-whisper pydub


⸻

## 🚀 How to Run the Bot
1.	Open a terminal in the project root.
2.	Run the bot script:

  	    python main.py

  4.	Open Telegram, search for your bot, and start interacting using the commands below.

⸻

## 📝 Bot Commands & Features

| Command        | Description                                     |
|----------------|-------------------------------------------------|
| /start         | Start the bot and view welcome message          |
| /orario        | 📅 Show class & exam schedules                  |
| /adisu         | ❓ FAQs & grants                                |
| /sedute        | 🎓 Graduation schedules & plans                 |
| /chat          | 💬 Interactive chat (text, file, audio, video). |
| /notifications | 🔔 Smart academic notifications                 |
| /howto         | ℹ️ How to use the bot                           |
| /close         | ✖️ Close the bot session                        |


⸻

## 🔔 Notifications Feature

The bot provides smart academic notifications to help students stay updated on:
	•	Exam schedules
	•	Tuition or fee deadlines
	•	Class or graduation schedule updates

Students can customize which notifications to receive via the /notifications command.

⸻

## 📑 Methodology

1. **Requirement Analysis** – Identified student needs (schedules, FAQs, grants, notifications).  
2. **System Design** – Modular folders for features (`chat/`, `orario/`, `adisu/`, `sedute/`, `Notifications/`).  
3. **Implementation** – Python 3.11, `pyTelegramBotAPI`, optional AI via OpenAI API.  
4. **Testing & Deployment** – Local testing on Windows 11, improved error handling.  
5. **Future Improvements** – AI-powered responses, database integration, cloud deployment.
   
⸻

## 📂 Project Structure

    ├── chat/
    │   ├── __init__function.py
    │   ├── chat_function.py
    │   └── chat_markup.py
    ├── orario/
    │   ├── orario_functions.py
    │   └── orario_markup.py
    ├── adisu/
    │   ├── adisu_functions.py
    │   └── adisu_markup.py
    ├── sedute/
    │   ├── sedute_functions.py
    │   └── sedute_markup.py
    ├── Notifications/
    │   ├── __init__function.py
    │   ├── notifications_function.py
    │   └── notifications_markup.py
    ├── main.py
    ├── telegram_token.json (do NOT upload to GitHub)
    ├── openai_key (do NOT upload to GitHub)
    └── README.md

⸻

## 📘 How to Use the University Chat Bot

> Welcome to the University of Palestine’s Telegram Chat Bot! This bot is designed to assist students with academic information, schedules, FAQs, and more. Here’s how to get started:

### 🚀 Getting Started

1.	Install Telegram on your device.
2.	Start the Bot by searching for it in <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram" width="20" height="20"> Telegram or [clicking here](https://t.me/n8n_mayar_prompt_bot)
3.	Send /start to initiate the conversation.

### 🧭 Available Commands

Use the following commands to access various features:

	•	/start – Welcome message and main menu.
	•	/orario – View class and exam schedules.
	•	/sedute – Access graduation plans and schedules.
	•	/adisu – Get FAQs and grant information.
	•	/chat – Chat with the bot using text, files, audio, or video.
	•	/notifications – Enable smart notifications for events or deadlines.
	•	/howto – Link to this guide on using the bot.
	•	/close – End the bot session.

### 💬 Chat Features
	1.	Tap /chat to open the chat menu.
	2.	Choose the type of input:
	   •	Text – Send a text message to the bot.
	   •	File – Upload a file for analysis.
	   •	Audio – Record and send a voice message.
	   •	Video – Send a video message.
	3.	The bot will process your input and respond accordingly.

### ⚠️ Notes
	
 •	Only text, files, audio, and video inputs are supported. Stickers, locations, or contacts are not processed.
 •	For detailed instructions, visit the GitHub repository: [GitHub Link](https://github.com/myarnwas/Chat-Bot-Telegram-University-of-Palestine/tree/main)

⸻

## 📸 Workflow & Screenshots

Workflow Diagram:

Bot Interface Example:

Place screenshots of Telegram bot interactions in the images/ folder. 
