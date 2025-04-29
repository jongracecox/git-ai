"""Pre-commit helper functions."""

import sys

from colored import Fore, Style
from sh import ErrorReturnCode_1, pre_commit


def run_pre_commit():
    """Run pre-commit hooks."""
    print(f"{Fore.blue}Running pre-commit hooks...{Style.reset}")
    try:
        pre_commit("run", _fg=True)
    except ErrorReturnCode_1:
        print(f"{Fore.red}Pre-commit hooks failed. Exiting.{Style.reset}")
        sys.exit(1)
    print(f"{Fore.blue}Pre-commit hooks passed.{Style.reset}")
