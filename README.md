# 🚀 AI Content Generator Pro

**Professional multi-platform content creation powered by Google Gemini AI**

&#x20; &#x20;

## 📋 Description

AI Content Generator Pro is a powerful tool for generating high-quality content using Google's Gemini AI. The app supports content generation for 7 major social platforms and various content types with intelligent validation and optimization.

### ✨ Key Features

- 🤖 **AI-Powered Generation**: Powered by Google Gemini 1.5 Flash
- 🌍 **Multilingual**: Supports 16 languages
- 📱 **7 Social Platforms**: Facebook, Instagram, TikTok, LinkedIn, YouTube Shorts, X/Twitter, Threads
- 🎭 **16 Brand Voices**: From professional to humorous
- ✅ **Smart Validation**: Automatic input sanitization and validation
- 📊 **Detailed Analytics**: Analyze generated content metadata
- 🎨 **Modern UI**: Stylish UI with gradients and animations
- 🔧 **Predefined Templates**: Quick start examples included

## 🛠️ Technologies

- **Backend**: Python 3.8+
- **AI Model**: Google Gemini 1.5 Flash
- **Frontend**: Gradio 4.0+
- **Environment**: Python-dotenv
- **Logging**: Python logging module

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or newer
- Google AI API key
- Git (for cloning repository)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/ai-content-generator-pro.git
cd ai-content-generator-pro
```

2. **Create a virtual environment:**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**

```bash
# Create .env file
cp .env.example .env

# Edit .env file and add your API key
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```

5. **Run the app:**

```bash
python app.py
```

The app will be available at: `http://localhost:7860`

## 🔧 Configuration

### Environment Variables (.env)

```env
# Required
GOOGLE_API_KEY=your_google_api_key_here

# Optional
DEBUG=False
LOG_LEVEL=INFO
MAX_CONTENT_LENGTH=10000
SERVER_HOST=0.0.0.0
SERVER_PORT=7860
```

### Getting a Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add it to your `.env` file

## 📁 Project Structure

```
ai-content-generator-pro/
├── app.py                 # Main application file
├── config.py             # Configuration
├── requirements.txt      # Python dependencies
├── prompt_template.txt   # Prompt template
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore rules
├── README.md           # Documentation
├── utils/              # Utilities
│   ├── __init__.py
│   ├── content_generator.py  # Content generator
│   └── validators.py         # Validators
└── templates/          # Templates (optional)
    └── prompt_template.txt
```

## 💡 Usage

### Main Steps:

1. **Select the language** of the content
2. **Enter the topic** (required)
3. **Describe the primary goal** (required)
4. **Define the target audience** (required)
5. **Select brand voice**
6. **Add a key message** (optional)
7. **Include additional information** (optional)
8. **Click "Generate Content"**

### Example:

**Topic:** "Benefits of healthy eating for busy professionals"

**Goal:** "Motivate working professionals to adopt healthier eating habits"

**Audience:** "Busy professionals aged 25–45"

**Result:** Ready-made content for all 7 platforms with optimized headlines, hashtags, and CTAs.

## 🌟 Supported Platforms

| Platform           | Features                          | Content Length       |
| ------------------ | --------------------------------- | -------------------- |
| **Facebook**       | Public focus, 2–3 hashtags        | 100–200 words        |
| **Instagram**      | Visual content, 5–10 hashtags     | 150–300 characters   |
| **TikTok**         | Energetic tone, trends            | 15–30 seconds script |
| **LinkedIn**       | Professional tone, business value | 1300–1500 characters |
| **YouTube Shorts** | SEO-optimized titles              | 30-sec script        |
| **X/Twitter**      | Direct tone, questions            | 240–280 characters   |
| **Threads**        | Personal tone, thread style       | Cascading posts      |

## 🔍 API Documentation

### ContentGenerator Class

```python
from utils.content_generator import ContentGenerator

generator = ContentGenerator()

# Generate content
result = generator.generate_with_metadata(
    language="Ukrainian",
    topic="AI in healthcare",
    primary_goal="Educate doctors on the benefits of AI",
    target_audience="Medical professionals",
    brand_voice="Professional",
    key_message="AI is revolutionizing diagnostics",
    additional_info="Include statistics and examples"
)
```

## 🚨 Troubleshooting

### Common Issues:

**1. API key not configured:**

```
❌ Configuration Error: Please check your API key configuration in .env file.
```

**Solution:** Check your `.env` file and make sure the API key is correct.

**2. Validation error:**

```
❌ Topic is required and cannot be empty
```

**Solution:** Fill in all required fields (marked \*).

**3. Connection error:**

```
❌ API Connection Failed: Please check your API key.
```

**Solution:** Check your internet connection and validate your API key.

## 🔐 Security

- API keys are stored in `.env` files (never committed to Git)
- Inputs are automatically sanitized
- All user data is validated
- Secure logging without sensitive data

## 🤝 Contributing

We welcome contributions! Here’s how you can help:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

### Roadmap:

-

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- **Google** for Gemini AI API
- **Gradio** for the amazing UI framework
- **Developer community** for open code and support

## 📞 Contact

- **GitHub Issues:** [Create issue](https://github.com/your-username/ai-content-generator-pro/issues)
- **Email:** [your-email@example.com](mailto\:your-email@example.com)
- **LinkedIn:** [Your Profile](https://linkedin.com/in/your-profile)

---

🌟 **Like the project? Star it!** 🌟

&#x20;

**Made with ❤️ in Ukraine 🇺🇦**

