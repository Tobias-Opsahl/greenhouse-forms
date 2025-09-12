from pathlib import Path

# Fonts

FONTS_FOLDER_PATH = Path("src") / "ui" / "fonts"
DNB_FONT_LIGHT_FILENAME = "DNB-Light.woff2"
DNB_FONT_REGULAR_FILENAME = "DNB-Regular.woff2"
DNB_FONT_MEDIUM_FILENAME = "DNB-Medium.woff2"
DNB_FONT_BOLD_FILENAME = "DNB-Bold.woff2"

VALID_ENVIRONMENTS = [
    "dev",  # Development
    "sit",  # System integration test (SIT)
    "uat",  # User acceptance test (UAT)
    "prod",  # Production
]

ENVIRONMENTS_READABLE = ["Development", "SIT (test)", "UAT (QA)", "Production"]

ENVIRONMENTS_READABLE_TO_DATABASE_NAME = {
    env_readable: env for env, env_readable in zip(VALID_ENVIRONMENTS, ENVIRONMENTS_READABLE)
}
