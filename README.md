# 📱 Social Media Content Generator

An AI-powered web application that transforms YouTube video transcripts into engaging, platform-specific social media content using **Generative AI and an Agent-based workflow**.

The application extracts the transcript of a YouTube video and uses a **Content Writer Agent powered by Google Gemini** to generate customized content for platforms such as LinkedIn, Instagram, and Twitter/X.

---

## 🚀 Live Demo

**Streamlit App:**
`https://social-media-generator-project.streamlit.app/`

**GitHub Repository:**
`https://github.com/YOUR_USERNAME/Social_Media_project`

---

## 📌 Project Overview

Creating social media content manually from long-form video content can be time-consuming. This project automates the process by converting the information contained in a YouTube video into concise and engaging social media posts.

The application combines:

* YouTube transcript extraction
* Generative AI
* AI agent workflows
* Prompt-based content generation
* Platform-specific content formatting
* Interactive Streamlit UI

Users only need to provide a YouTube Video ID, describe the type of content they want, and select their target social media platforms.

---

## 🎯 Objectives

The main objectives of this project are:

* Automate social media content creation from YouTube videos.
* Reduce the time required to manually summarize long-form video content.
* Generate platform-specific posts using Generative AI.
* Provide users with an easy-to-use web interface.
* Demonstrate the practical use of AI agents and LLM APIs.
* Allow generated content to be downloaded for further use.

---

## ✨ Features

### 🎥 YouTube Transcript Extraction

The application extracts the transcript of a YouTube video using the **YouTube Transcript API**.

### 🤖 AI-Powered Content Generation

Google Gemini is used to analyze the transcript and generate natural-language social media content.

### 🧠 Agent-Based Workflow

The project uses the **OpenAI Agents SDK** to implement a single AI content-writing agent that receives the user's instructions and transcript and generates structured social media content.

### 💼 LinkedIn Content

Generate professional and informative LinkedIn posts suitable for sharing educational, technical, or professional video content.

### 📸 Instagram Content

Generate concise and engaging Instagram captions with relevant hashtags.

### 🐦 Twitter/X Content

Generate short, engaging content suitable for Twitter/X.

### ✍️ Custom Prompts

Users can provide their own instructions to control the style, purpose, tone, and information included in the generated content.

### 📥 Content Download

Generated posts can be downloaded as `.txt` files directly from the application.

### 🌐 Web-Based Interface

The entire application is accessible through an interactive Streamlit interface without requiring users to interact with the Python code directly.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    │ YouTube ID + Prompt │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ YouTube Transcript  │
                    │       API           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Content Writer     │
                    │       Agent         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Google Gemini    │
                    │        LLM          │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │ Platform-Specific Social Media  │
              │             Content             │
              └────────────────┬────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Display / Download │
                    │       Content       │
                    └─────────────────────┘
```

---

## 🔄 Application Workflow

### Step 1 — User Input

The user enters a YouTube Video ID into the Streamlit application.

Example:

```text
HTNz4L2XM58
```

### Step 2 — Content Request

The user enters a prompt describing the content they want.

Example:

```text
Generate a professional LinkedIn post and an engaging Instagram caption
based on this video transcript. Explain the main concepts and key
takeaways for beginners. Include relevant hashtags.
```

### Step 3 — Platform Selection

The user selects one or more target platforms:

* LinkedIn
* Instagram
* Twitter/X

### Step 4 — Transcript Extraction

The application retrieves the transcript associated with the YouTube Video ID.

### Step 5 — Agent Processing

The transcript and user's instructions are passed to the Content Writer Agent.

### Step 6 — AI Generation

The agent uses Google Gemini to generate platform-specific social media content.

### Step 7 — Result Display

The generated content is displayed inside the Streamlit application.

### Step 8 — Download

Users can download each generated post as a text file.

---

## 🤖 Agent Architecture

This project implements a **single-agent Agentic AI architecture**.

The main agent is the:

### Content Writer Agent

The Content Writer Agent is responsible for generating engaging and readable social media content based on:

* YouTube video transcript
* User instructions
* Selected social media platforms

The agent is configured with a structured output format containing the target platform and generated content.

### Agent Workflow

```text
User Request
     ↓
Transcript + User Prompt
     ↓
Content Writer Agent
     ↓
Gemini Language Model
     ↓
Structured Social Media Posts
     ↓
Streamlit Interface
```

This is a **single-agent system**, rather than a multi-agent architecture.

---

## 🛠️ Technologies Used

| Technology                | Purpose                                                |
| ------------------------- | ------------------------------------------------------ |
| Python                    | Core programming language                              |
| Streamlit                 | Web application and user interface                     |
| Google Gemini             | Generative AI model                                    |
| OpenAI Agents SDK         | Agent orchestration                                    |
| OpenAI Python SDK         | API client used with Gemini's compatible API interface |
| YouTube Transcript API    | YouTube transcript extraction                          |
| python-dotenv             | Environment variable management                        |
| Git & GitHub              | Version control and source-code hosting                |
| Streamlit Community Cloud | Application deployment                                 |

---

## 📂 Project Structure

```text
Social_Media_project/
│
├── app.py
├── socialmedia.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `app.py`

Contains the Streamlit application interface.

Responsibilities include:

* Collecting user input
* Accepting YouTube Video IDs
* Accepting custom prompts
* Selecting social media platforms
* Running the AI agent
* Displaying generated content
* Providing download buttons

### `socialmedia.py`

Contains the core AI and transcript functionality.

Responsibilities include:

* Loading environment variables
* Configuring the Gemini API client
* Extracting YouTube transcripts
* Defining the content-generation tool
* Defining the Content Writer Agent
* Configuring structured output

### `requirements.txt`

Contains the Python packages required to install and run the application.

### `.gitignore`

Prevents sensitive and unnecessary files from being uploaded to GitHub.

Examples include:

```text
.env
antigravity-env/
__pycache__/
*.pyc
```

---

## ⚙️ Installation

### Prerequisites

Make sure the following are installed:

* Python 3.x
* Git
* A Google Gemini API key

---

### 1. Clone the Repository

```bash
git clone https://github.com/navyasree1385/Social_Media_project.git
```

Move into the project directory:

```bash
cd Social_Media_project
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
```

Replace:

```text
your_gemini_api_key
```

with your actual Gemini API key.

### ⚠️ Security Notice

**Never commit your `.env` file or API key to GitHub.**

The project `.gitignore` is configured to prevent `.env` from being tracked.

For deployed applications, use the deployment platform's secure secrets management instead of placing API credentials directly in the repository.

---

## ▶️ Running the Application Locally

After installing the dependencies and configuring the environment variables, run:

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 🧑‍💻 How to Use

### 1. Enter a YouTube Video ID

Example:

```text
HTNz4L2XM58
```

The Video ID is the portion of a YouTube URL after:

```text
v=
```

For example:

```text
https://www.youtube.com/watch?v=HTNz4L2XM58
```

The Video ID is:

```text
HTNz4L2XM58
```

### 2. Enter Your Query

Example:

```text
Generate a professional LinkedIn post and an engaging Instagram caption
based on this video transcript. Explain the main concepts of AI agents,
how they work, and the key takeaways for beginners. Include relevant hashtags.
```

### 3. Select Platforms

Choose the platforms for which content should be generated.

```text
☑ LinkedIn
☑ Instagram
☐ Twitter
```

### 4. Generate Content

Click:

**Generate Content**

The application retrieves the transcript and sends the request to the AI agent.

### 5. Review the Results

Generated content is displayed separately for each selected platform.

### 6. Download

Use the download button associated with each platform to save the generated content as a `.txt` file.

---

## 🧪 Example

### Input

**YouTube Video ID**

```text
HTNz4L2XM58
```

**Prompt**

```text
Generate a professional LinkedIn post and an engaging Instagram caption
based on this video transcript. Explain the main concepts of AI agents,
how they work, and the key takeaways for beginners. Include relevant hashtags.
```

**Selected Platforms**

```text
LinkedIn
Instagram
```

### Output

The application generates separate content for each selected platform.

```text
LinkedIn Post
────────────────────────────────

Professional platform-specific content...


Instagram Post
────────────────────────────────

Engaging caption with relevant hashtags...
```

---

## 🔌 API Integration

The project integrates with two major external services.

### YouTube Transcript API

Used to retrieve the transcript of a YouTube video.

General workflow:

```text
YouTube Video ID
      ↓
YouTube Transcript API
      ↓
Video Transcript
```

### Google Gemini API

Used to generate the social media content.

General workflow:

```text
Transcript + User Prompt
          ↓
      Gemini API
          ↓
Generated Social Media Content
```

---

## 📊 Input and Output

### Input

The application accepts:

* YouTube Video ID
* User-generated prompt
* Target social media platforms

### Output

The application produces:

* Platform-specific social media content
* Generated captions/posts
* Downloadable `.txt` files

---

## 🧠 Generative AI Approach

The application uses a Large Language Model to transform unstructured transcript information into structured social media content.

The basic process is:

```text
Long-form Video Content
          ↓
      Transcript
          ↓
   Context + Prompt
          ↓
     Gemini LLM
          ↓
Platform-Specific Content
```

The user's prompt provides additional instructions regarding:

* Content type
* Platform
* Tone
* Target audience
* Key information
* Hashtags
* Formatting

---

## 🔒 Security and Privacy

The application does not store API keys directly in the source code.

Sensitive credentials are supplied through environment variables during local development and secure deployment secrets in the deployed application.

The repository intentionally excludes:

```text
.env
antigravity-env/
__pycache__/
```

GitHub also provides security features such as secret scanning and push protection that can help prevent credentials from being accidentally committed. 

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment workflow:

```text
Local Project
     ↓
Git Repository
     ↓
GitHub
     ↓
Streamlit Community Cloud
     ↓
Live Web Application
```

### Deployment Configuration

The deployed application uses:

```text
Repository: Social_Media_project
Branch: main
Main file: app.py
```

API credentials are configured through Streamlit's Secrets management rather than being committed to GitHub.

---

## 🧪 Testing

The application was tested using YouTube videos and different combinations of:

* Video IDs
* User prompts
* Social media platforms
* Generated content requests

Example test video:

```text
https://youtu.be/HTNz4L2XM58
```

The application successfully performs:

```text
YouTube Video
      ↓
Transcript Extraction
      ↓
AI Processing
      ↓
Content Generation
      ↓
Platform-Specific Output
      ↓
Download
```

---

## ⚠️ Error Handling

The application handles common runtime situations such as:

* Missing YouTube Video ID
* No social media platform selected
* Transcript retrieval failures
* AI generation errors
* Invalid or unexpected AI responses
* Temporary API service errors
* API quota limitations

The application displays errors through the Streamlit interface rather than terminating silently.

---

## 📈 Future Enhancements

The following features can be added in future versions:

### 🔗 Direct YouTube URL Support

Allow users to paste a complete YouTube URL instead of manually extracting the Video ID.

### 🎨 AI-Generated Visuals

Generate images or graphics along with social media posts.

### 📅 Social Media Scheduling

Allow users to schedule generated posts for future publishing.

### 🔄 Additional Platforms

Support platforms such as:

* Facebook
* Threads
* Reddit
* Medium

### 🌍 Multi-Language Generation

Generate social media content in multiple languages.

### 🎯 Audience Personalization

Allow users to specify:

* Target audience
* Industry
* Age group
* Professional level
* Content style

### 📊 Analytics

Provide analytics and performance insights for generated content.

### 🔐 Authentication

Add user accounts and personalized content-generation history.

### 💾 Content History

Allow users to save, view, edit, and reuse previously generated posts.

---

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python programming
* Generative AI
* Large Language Models
* AI Agents
* Prompt Engineering
* API integration
* Natural Language Processing
* YouTube transcript processing
* Streamlit application development
* Environment variable management
* Git and GitHub
* Cloud deployment

---

## 🎯 Project Significance

The project demonstrates how Generative AI and agent-based workflows can be applied to automate a practical content-creation task.

Instead of manually watching a long video, extracting important information, summarizing it, and adapting it for multiple platforms, the application automates these steps through a single interactive workflow.

```text
Manual Process:

Watch Video
    ↓
Take Notes
    ↓
Summarize
    ↓
Write LinkedIn Post
    ↓
Rewrite for Instagram
    ↓
Rewrite for Twitter


Automated Process:

YouTube Video
    ↓
AI Agent
    ↓
LinkedIn + Instagram + Twitter Content
```

---

## 👨‍💻 Author

**Karthii**

This project was developed as a practical implementation of Generative AI and Agentic AI concepts.

### Areas Demonstrated

* Artificial Intelligence
* Generative AI
* AI Agents
* Prompt Engineering
* API Integration
* Natural Language Processing
* Web Application Development
* Cloud Deployment

---

## 📄 License

This project is intended for educational and demonstration purposes.

If you plan to distribute or reuse the project publicly, add an appropriate open-source license to the repository.

---

## ⭐ Acknowledgements

This project uses the following technologies and services:

* Google Gemini
* OpenAI Agents SDK
* YouTube Transcript API
* Streamlit
* GitHub

---

## 📬 Support

If you encounter an issue while running the project:

1. Verify that Python and all dependencies are installed.
2. Verify that the Gemini API key is correctly configured.
3. Check that the YouTube Video ID is valid.
4. Check the application logs for API or deployment errors.
5. Open an issue in the GitHub repository with relevant error details.

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
