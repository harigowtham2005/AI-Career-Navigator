import os


class Config:
    """
    Application Configuration
    """

    # Flask
    SECRET_KEY = "ai-career-navigator-2026"

    # Upload Configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024      # 10 MB

    ALLOWED_EXTENSIONS = {"pdf"}

    # Database
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "sky"
    DB_NAME = "ai_career_navigator"

    # Dashboard
    DEFAULT_MIN_SCORE = 0

    # Application
    APP_NAME = "AI Career Navigator"

    APP_VERSION = "2.0"