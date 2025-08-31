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
    ```bash
    { "api_key": "YOUR_OPENAI_KEY" }


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
    ```bash
    
    pip install sqlite3 apscheduler pyTelegramBotAPI openai pypdf2 python-docx faster-whisper pydub


⸻

## 🚀 How to Run the Bot
	1.	Open a terminal in the project root.
	2.	Run the bot script:
      ```bash
            
      python main.py

  3.	Open Telegram, search for your bot, and start interacting using the commands below.

⸻

## 📝 Bot Commands & Features
|----------------|-------------------------------------------------|
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
|----------------|-------------------------------------------------|

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

## 📸 Workflow & Screenshots

Workflow Diagram:

Bot Interface Example:

Place screenshots of Telegram bot interactions in the images/ folder.

تحبي أعملها لك؟
