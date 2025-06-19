import gradio as gr
import logging
import time
from config import Config, validate_config
from utils.content_generator import ContentGenerator
from utils.validators import validate_all_inputs

# Setup logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the content generator
try:
    validate_config()
    generator = ContentGenerator()
    logger.info("Application initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize application: {e}")
    generator = None


def generate_content_wrapper(language, topic, primary_goal, target_audience,
                             brand_voice, key_message, additional_info, progress=gr.Progress()):
    """Wrapper function for content generation with validation"""

    if generator is None:
        return "❌ **Configuration Error:** Please check your API key configuration in .env file."

    try:
        progress(0.1, desc="Validating input...")

        # Prepare input data
        input_data = {
            'language': language,
            'topic': topic,
            'primary_goal': primary_goal,
            'target_audience': target_audience,
            'brand_voice': brand_voice,
            'key_message': key_message,
            'additional_info': additional_info
        }

        # Validate inputs
        validation_result = validate_all_inputs(input_data)

        if not validation_result['is_valid']:
            error_message = "**Validation Errors:**\n" + "\n".join(validation_result['errors'])
            return error_message

        progress(0.3, desc="Preparing content generation...")

        # Use sanitized data
        sanitized_data = validation_result['sanitized_data']

        progress(0.5, desc="Generating content with AI...")

        # Generate content with metadata
        result = generator.generate_with_metadata(**sanitized_data)

        if not result['success']:
            return f"❌ **Generation Error:** {result['error']}"

        progress(0.9, desc="Formatting result...")

        # Format the output
        metadata = result['metadata']
        formatted_result = f"""✅ **Content Generated Successfully!**

---

{result['content']}

---

📊 **Generation Statistics:**
- **Language:** {metadata['language']}
- **Topic:** {metadata['topic']}
- **Brand Voice:** {metadata['brand_voice']}
- **Word Count:** {metadata['word_count']} words
- **Character Count:** {metadata['character_count']} characters
- **Generation Time:** {metadata['generation_time']} seconds
- **Generated:** {metadata['generated_at']}

---
*Powered by Google Gemini AI*
"""

        logger.info(f"Content generated successfully for topic: {topic}")
        return formatted_result

    except Exception as e:
        logger.error(f"Unexpected error in content generation: {e}")
        return f"❌ **Unexpected Error:** {str(e)}\n\nPlease try again or contact support if the issue persists."


def test_api_connection():
    """Test API connection"""
    if generator is None:
        return "❌ **API Not Configured:** Please check your .env file"

    try:
        if generator.test_connection():
            return "✅ **API Connection Successful!** Ready to generate content."
        else:
            return "❌ **API Connection Failed:** Please check your API key."
    except Exception as e:
        return f"❌ **Connection Test Error:** {str(e)}"


# Create the Gradio interface
with gr.Blocks(
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="cyan",
            neutral_hue="slate",
        ),
        css="""
    .gradio-container {
        max-width: 1200px !important;
        margin: auto;
    }
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .generate-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1em !important;
        padding: 12px 30px !important;
        border-radius: 25px !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    .generate-btn:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4) !important;
    }
    .tips-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        margin-top: 1rem;
    }
    .status-section {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    """,
        title="🚀 AI Content Generator Pro"
) as demo:
    # Header
    gr.HTML("""
    <div class="main-header">
        <h1>🚀 AI Content Generator Pro</h1>
        <p>Create high-quality content with artificial intelligence</p>
        <small>Powered by Google Gemini AI • Enhanced with Smart Validation</small>
    </div>
    """)

    # API Status Check
    with gr.Row():
        with gr.Column(scale=3):
            api_status = gr.Markdown(value="🔄 **Checking API connection...**")
        with gr.Column(scale=1):
            test_btn = gr.Button("🔍 Test API", variant="secondary", size="sm")

    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML("<h3>📝 Content Settings</h3>")

            language = gr.Dropdown(
                choices=Config.SUPPORTED_LANGUAGES,
                value="English",
                label="🌍 Content Language",
                info="Select the language for content generation"
            )

            topic = gr.Textbox(
                label="📋 Topic *",
                placeholder="e.g., artificial intelligence in healthcare",
                lines=2,
                info="Main topic of your content (required)"
            )

            primary_goal = gr.Textbox(
                label="🎯 Primary Goal *",
                placeholder="e.g., educate about AI benefits in medical diagnosis",
                lines=2,
                info="What do you want to achieve with this content? (required)"
            )

        with gr.Column(scale=1):
            gr.HTML("<h3>👥 Audience & Style</h3>")

            target_audience = gr.Textbox(
                label="👥 Target Audience *",
                placeholder="e.g., healthcare professionals, medical students",
                lines=2,
                info="Who is this content for? (required)"
            )

            brand_voice = gr.Dropdown(
                choices=Config.BRAND_VOICES,
                value="Professional",
                label="🗣️ Brand Voice",
                info="Choose your communication tone"
            )

            key_message = gr.Textbox(
                label="💡 Key Message",
                placeholder="e.g., AI is revolutionizing medical diagnostics",
                lines=3,
                info="Main idea to convey (optional)"
            )

    with gr.Row():
        additional_info = gr.Textbox(
            label="📎 Additional Information",
            placeholder="Links, contact info, business details, specific requirements, keywords to include...",
            lines=4,
            info="Any additional information to include in the content"
        )

    with gr.Row():
        with gr.Column(scale=1):
            clear_btn = gr.Button("🗑️ Clear All", variant="secondary", size="sm")
        with gr.Column(scale=2):
            generate_btn = gr.Button(
                "✨ Generate Content",
                variant="primary",
                elem_classes="generate-btn",
                size="lg"
            )
        with gr.Column(scale=1):
            word_count_btn = gr.Button("📊 Word Count", variant="secondary", size="sm")

    # Output section
    with gr.Row():
        output = gr.Markdown(
            label="📄 Generated Content",
            value="Your generated content will appear here...\n\n*Tip: Fill in the required fields (*) and click 'Generate Content' to start.*",
            elem_id="output-markdown"
        )

    # Features and tips section
    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML("""
            <div class="tips-section">
                <h4>💡 Pro Tips for Best Results</h4>
                <ul style="text-align: left; font-size: 0.9em; margin: 0.5rem 0; line-height: 1.4;">
                    <li><strong>Be Specific:</strong> Detailed topics get better results</li>
                    <li><strong>Define Audience:</strong> Clear audience = targeted content</li>
                    <li><strong>Set Clear Goals:</strong> What action should readers take?</li>
                    <li><strong>Add Context:</strong> Include relevant details in additional info</li>
                    <li><strong>Choose Voice:</strong> Match your brand personality</li>
                    <li><strong>Include Keywords:</strong> Add SEO keywords naturally</li>
                    <li><strong>Review Output:</strong> Edit and customize the generated content</li>
                </ul>
            </div>
            """)

        with gr.Column(scale=1):
            gr.HTML("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 1.5rem; border-radius: 12px; color: white;">
                <h4>🎯 Perfect For</h4>
                <div style="font-size: 0.9em; line-height: 1.5;">
                    <strong>Content Types:</strong><br>
                    📝 Blog posts & articles<br>
                    📱 Social media content<br>
                    📧 Email campaigns<br>
                    🛍️ Product descriptions<br>
                    📄 Website copy<br>
                    📊 Marketing materials<br>
                    📰 Press releases<br>
                    🎓 Educational content<br>
                    📋 Technical documentation
                </div>
            </div>
            """)


    # Event handlers
    def clear_all():
        return "", "", "", "", "", "", "Ready to generate new content..."


    def count_words(content):
        if "Generated Successfully" in content:
            words = len(content.split())
            chars = len(content)
            return f"📊 **Statistics:** {words} words, {chars} characters"
        return "📊 No content to analyze"


    # Connect events
    clear_btn.click(
        clear_all,
        outputs=[topic, primary_goal, target_audience, key_message, additional_info, output]
    )

    generate_btn.click(
        generate_content_wrapper,
        inputs=[language, topic, primary_goal, target_audience, brand_voice, key_message, additional_info],
        outputs=output
    )

    test_btn.click(
        test_api_connection,
        outputs=api_status
    )

    word_count_btn.click(
        count_words,
        inputs=[output],
        outputs=[]
    )

    # Quick start examples
    gr.Examples(
        examples=[
            ["English", "Benefits of healthy eating for busy professionals",
             "Motivate working professionals to adopt healthier eating habits",
             "Busy professionals aged 25-45", "Motivational",
             "Small changes in diet lead to big improvements in energy and productivity",
             "Include quick meal prep tips, time-saving strategies, and energy-boosting foods"],

            ["English", "Digital marketing trends for small businesses in 2024",
             "Educate small business owners about latest marketing strategies",
             "Small business owners and entrepreneurs", "Professional",
             "Stay competitive with cutting-edge digital marketing approaches",
             "Focus on AI tools, social commerce, video marketing, and automation"],

            ["English", "Remote work productivity and work-life balance",
             "Help remote workers maintain productivity while achieving better work-life balance",
             "Remote workers, freelancers, and digital nomads", "Expert",
             "Productivity isn't about working harder, it's about working smarter",
             "Include time management techniques, home office setup, communication tools"]
        ],
        inputs=[language, topic, primary_goal, target_audience, brand_voice, key_message, additional_info],
        label="🚀 Quick Start Examples - Click to Try!"
    )

    # Auto-test API on load
    demo.load(test_api_connection, outputs=api_status)

    # Footer
    gr.HTML("""
    <div style="text-align: center; margin-top: 2rem; padding: 1rem; 
                background: rgba(0,0,0,0.05); border-radius: 10px;">
        <p style="margin: 0; color: #666; font-size: 0.9em;">
            🤖 Powered by Google Gemini AI • 🎨 Built with Gradio • 
            ⚡ Enhanced with Smart Validation & Error Handling<br>
            <small>v2.0 • Professional Edition</small>
        </p>
    </div>
    """)

# Launch the app
if __name__ == "__main__":
    try:
        demo.launch(
            server_name=Config.SERVER_HOST,
            server_port=Config.SERVER_PORT,
            share=True,
            show_error=True,
            quiet=not Config.DEBUG
        )
    except Exception as e:
        logger.error(f"Failed to launch application: {e}")
        print(f"❌ Error launching app: {e}")
        print("💡 Please check your configuration and try again.")