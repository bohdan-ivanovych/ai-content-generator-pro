"""
Input validation utilities for the AI Content Generator
"""

import re
from typing import List, Dict, Any


def validate_content_input(topic: str, primary_goal: str, target_audience: str) -> List[str]:
    """
    Validate required input fields for content generation

    Args:
        topic: The main topic for content
        primary_goal: The primary goal of the content
        target_audience: The target audience description

    Returns:
        List of error messages (empty if valid)
    """
    errors = []

    # Required field validation
    if not topic or not topic.strip():
        errors.append("❌ Topic is required and cannot be empty")

    if not primary_goal or not primary_goal.strip():
        errors.append("❌ Primary goal is required and cannot be empty")

    if not target_audience or not target_audience.strip():
        errors.append("❌ Target audience must be specified")

    # Length validation
    if topic and len(topic.strip()) < 3:
        errors.append("❌ Topic should be at least 3 characters long")

    if topic and len(topic) > 200:
        errors.append("❌ Topic should be under 200 characters")

    if primary_goal and len(primary_goal) > 300:
        errors.append("❌ Primary goal should be under 300 characters")

    if target_audience and len(target_audience) > 200:
        errors.append("❌ Target audience should be under 200 characters")

    return errors


def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent issues

    Args:
        text: Input text to sanitize

    Returns:
        Sanitized text
    """
    if not text:
        return ""

    # Basic sanitization
    text = text.strip()
    text = text.replace('\x00', '')  # Remove null bytes
    text = text.replace('\r\n', '\n')  # Normalize line endings
    text = text.replace('\r', '\n')  # Normalize line endings

    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)

    return text


def validate_language(language: str, supported_languages: List[str]) -> bool:
    """
    Validate if the selected language is supported

    Args:
        language: Selected language
        supported_languages: List of supported languages

    Returns:
        True if valid, False otherwise
    """
    return language in supported_languages


def validate_brand_voice(brand_voice: str, supported_voices: List[str]) -> bool:
    """
    Validate if the selected brand voice is supported

    Args:
        brand_voice: Selected brand voice
        supported_voices: List of supported brand voices

    Returns:
        True if valid, False otherwise
    """
    return brand_voice in supported_voices


def validate_all_inputs(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate all input data and return results

    Args:
        data: Dictionary containing all input data

    Returns:
        Dictionary with validation results
    """
    results = {
        'is_valid': True,
        'errors': [],
        'sanitized_data': {}
    }

    # Sanitize inputs
    sanitized = {}
    for key, value in data.items():
        if isinstance(value, str):
            sanitized[key] = sanitize_input(value)
        else:
            sanitized[key] = value

    results['sanitized_data'] = sanitized

    # Validate required fields
    content_errors = validate_content_input(
        sanitized.get('topic', ''),
        sanitized.get('primary_goal', ''),
        sanitized.get('target_audience', '')
    )

    results['errors'].extend(content_errors)

    # Set overall validity
    results['is_valid'] = len(results['errors']) == 0

    return results