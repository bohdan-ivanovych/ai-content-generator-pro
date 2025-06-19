import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for the AI Content Generator"""

    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # Application Settings
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", "10000"))

    # Server Configuration
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT = int(os.getenv("SERVER_PORT", "7860"))

    # Paths
    TEMPLATE_DIR = "templates"
    LOGS_DIR = "logs"
    EXPORTS_DIR = "exports"

    # Supported Languages
    SUPPORTED_LANGUAGES = [
        "English", "Ukrainian", "Russian", "Polish", "German",
        "French", "Spanish", "Italian", "Portuguese", "Chinese",
        "Japanese", "Korean", "Arabic", "Hindi", "Dutch", "Swedish"
    ]

    # Brand Voices
    BRAND_VOICES = [
        "Professional", "Friendly", "Authoritative", "Creative",
        "Formal", "Conversational", "Motivational", "Expert",
        "Casual", "Academic", "Persuasive", "Informative",
        "Inspiring", "Technical", "Storytelling", "Humorous"
    ]

    # Model Configuration
    MODEL_NAME = "gemini-1.5-flash"

    # Content Types
    CONTENT_TYPES = [
        "Blog Post", "Social Media", "Email Campaign",
        "Product Description", "Website Copy", "Press Release",
        "Technical Documentation", "Marketing Material"
    ]


# Validation function
def validate_config():
    """Validate that all required configuration is present"""
    if not Config.GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is required but not found in environment variables!")

    print("✅ Configuration validated successfully!")
    return True


if __name__ == "__main__":
    validate_config()