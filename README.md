# 📚 **AI-Powered Story Generator**  
```

           _____    _____ _                      _____                           _                        _ _   _       _____                                 
     /\   |_   _|  / ____| |                    / ____|                         | |                      (_) | | |     |_   _|                                
    /  \    | |   | (___ | |_ ___  _ __ _   _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __  __      ___| |_| |__     | |  _ __ ___   __ _  __ _  ___  ___ 
   / /\ \   | |    \___ \| __/ _ \| '__| | | | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| \ \ /\ / / | __| '_ \    | | | '_ ` _ \ / _` |/ _` |/ _ \/ __|
  / ____ \ _| |_   ____) | || (_) | |  | |_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |     \ V  V /| | |_| | | |  _| |_| | | | | | (_| | (_| |  __/\__ \
 /_/    \_\_____| |_____/ \__\___/|_|   \__, |  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|      \_/\_/ |_|\__|_| |_| |_____|_| |_| |_|\__,_|\__, |\___||___/
                                         __/ |                                                                                                 __/ |          
                                        |___/                                                                                                 |___/           

```
An immersive story creation tool that generates captivating stories, vivid images, and an engaging audiobook using state-of-the-art AI models like Claude 3.5 and DALL-E 3. The application leverages Streamlit for a seamless web interface, providing an end-to-end storytelling experience.

---

## 🚀 **Project Overview**

The AI-Powered Story Generator allows users to input a story description and receive a fully fleshed-out novel, complete with chapter-wise images and an audiobook. This tool is perfect for authors, content creators, and storytelling enthusiasts looking to transform ideas into rich, multimedia narratives effortlessly.

---

## 📂 **Project Structure**

```
📁 AI-Story-Generator/
├── 📄 app.py                     # Streamlit front-end application
├── 📄 model.py                   # Core AI models for story, image, and audio generation
├── 📄 requirements.txt           # Project dependencies
└── 📁 prompts/
    └── 📄 story_teller.txt       # Instructions for AI story generation
```

---

## 🧠 **Key Features**

- ✨ **Automated Story Generation:** Uses Anthropic's Claude 3.5 to generate structured and detailed stories.
- 🎨 **Image Creation:** DALL-E 3 generates vibrant images based on chapter content.
- 🎧 **Audiobook Conversion:** Text-to-speech (TTS) feature produces an immersive audio experience.
- 💻 **Interactive Web Interface:** Streamlit provides a simple and intuitive UI for user interaction.
- 📖 **Chapter-Based Output:** Displays stories with images and audio in an organized format.

---

## ⚡ **Getting Started**

### **1. Install Dependencies**

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```text
streamlit
openai
anthropic
python-dotenv
```

### **2. Set Up API Keys**

- Obtain API keys for **OpenAI** and **Anthropic**.
- Create a `.env` file in the root directory with the following content:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### **3. Launch the Application**

```bash
streamlit run app.py
```

- Open the provided `localhost` link in your browser to access the web app.

---

## 🎯 **Usage Example**

### **Generate a Story**

1. Enter a description of the type of story you want.
2. Click **Generate Story!**.
3. Watch as the story, images, and audiobook are created.

---

## 📄 **Sample Output**

### **Example: Fantasy Adventure**

- **Story Title:** *The Dragon's Whisper*
- **Chapters:** 
    - *Chapter 1: The Awakening* 
    - *Chapter 2: Into the Wilds* 
    - *Chapter 3: The Final Stand* 

- **Features:**
    - Beautifully generated chapter illustrations.
    - A smooth and clear audiobook narration.

---

## 🔮 **Future Enhancements**

- ✅ Add genre-specific prompts to guide story creation.
- 📈 Implement voice customization for the TTS model.
- 🖥️ Expand the web interface with advanced customization options.
- 🌐 Allow users to download the complete novel in PDF/ePub formats.

