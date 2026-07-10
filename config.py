"""
config.py — Application Configuration
======================================
Defines configuration classes for different environments (Development,
Production, Testing). The active config is selected via the APP_ENV
environment variable (defaults to 'development').

All sensitive values are read from environment variables (or a .env file
loaded by python-dotenv in run.py) so no secrets are ever hardcoded.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file into the environment at import time.
# This makes config.py self-contained when imported directly.
load_dotenv()


def _build_db_uri() -> str:
    """Construct the MySQL connection URI from individual env vars.

    Using PyMySQL as the pure-Python MySQL driver (no C extensions needed),
    which makes the app easier to containerise.
    """
    driver = "pymysql"
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "password")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    name = os.getenv("DB_NAME", "devops_taskmanager")
    return f"mysql+{driver}://{user}:{password}@{host}:{port}/{name}"


class BaseConfig:
    """Shared settings inherited by all environment configs."""

    # ── Security ──────────────────────────────────────────────────────────
    # SECRET_KEY is used by Flask to sign session cookies and CSRF tokens.
    # MUST be set to a long random value in production.
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me-in-production")

    # ── Database ──────────────────────────────────────────────────────────
    SQLALCHEMY_DATABASE_URI: str = _build_db_uri()
    # Disable SQLAlchemy modification tracking (saves memory; we use Flask-Migrate)
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    # Connection pool settings — important for long-running containers
    SQLALCHEMY_ENGINE_OPTIONS: dict = {
        "pool_recycle": 280,   # Recycle connections before MySQL's wait_timeout (default 8h)
        "pool_pre_ping": True,  # Verify connection liveness before each use
        "pool_size": 10,
        "max_overflow": 20,
    }

    # ── Session / Auth ────────────────────────────────────────────────────
    # Protect session cookies from JavaScript access
    SESSION_COOKIE_HTTPONLY: bool = True
    # Prevent CSRF via cross-site requests
    SESSION_COOKIE_SAMESITE: str = "Lax"

    # ── WTForms CSRF ─────────────────────────────────────────────────────
    WTF_CSRF_ENABLED: bool = True

    # ── Logging ───────────────────────────────────────────────────────────
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_TO_STDOUT: bool = os.getenv("LOG_TO_STDOUT", "false").lower() == "true"


class DevelopmentConfig(BaseConfig):
    """Local development — verbose errors and debug mode on."""
    DEBUG: bool = True
    TESTING: bool = False
    # Show SQL queries in console during development
    SQLALCHEMY_ECHO: bool = True
    LOG_LEVEL: str = "DEBUG"


class ProductionConfig(BaseConfig):
    """Production — strict security, no debug leakage."""
    DEBUG: bool = False
    TESTING: bool = False
    # Enforce HTTPS-only cookies when behind a TLS terminator (nginx/ALB)
    SESSION_COOKIE_SECURE: bool = True
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "WARNING")


class TestingConfig(BaseConfig):
    """Automated tests — use SQLite in-memory DB to avoid needing MySQL."""
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"
    WTF_CSRF_ENABLED: bool = False   # Disable CSRF for easier test client usage
    LOG_LEVEL: str = "ERROR"


# ── Config registry ───────────────────────────────────────────────────────────
# Maps the APP_ENV string to its config class. Used by the app factory.
config_map: dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
