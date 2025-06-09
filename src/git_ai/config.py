from pathlib import Path
from decouple import config


class GitAIConfig:
    """Configuration for the Git AI tool."""

    SRC_DIR: Path = Path(__file__).parent
    PROMPTS_DIR: Path = config(
        "GIT_AI_PROMPTS_DIR", default=Path(__file__).parent / "prompts"
    )
    DEFAULT_PROMPT_TEMPLATE: Path = PROMPTS_DIR / "generate_commit_message.txt.jinja2"
    GEMINI_API_KEY: str = config("GIT_AI_GEMINI_API_KEY")
    PROMPT_TEMPLATE: Path = Path(
        config("GIT_AI_PROMPT_TEMPLATE", default=str(DEFAULT_PROMPT_TEMPLATE))
    )
    NUM_PREVIOUS_COMMITS: int = config(
        "GIT_AI_NUM_PREVIOUS_COMMITS", default=3, cast=int
    )
    RUN_PRE_COMMIT = config("GIT_AI_RUN_PRE_COMMIT", default=True, cast=bool)
    AI_MODEL: str = config("GIT_AI_LLM_MODEL", default="gemini-2.5-flash-preview-04-17")
    COMMIT_EDITOR: str = config("GIT_AI_COMMIT_EDITOR", default="vi")
