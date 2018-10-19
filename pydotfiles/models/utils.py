# General imports
import logging
import shutil
import subprocess
import getpass
import sys

# Project imports
from pydotfiles.models import OverrideAction
from pydotfiles.utils import PrettyLogFormatter, PrettyPrint


logger = logging.getLogger(__name__)


"""
Project-specific logic
"""


def install_homebrew():
    if shutil.which("brew") is None:
        logger.info(f"Package Manager: Homebrew was not found, installing now (this may take a while)")
        command = "/usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\""

        process = subprocess.Popen(command.split(), stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        try:
            process.communicate('\r')
            logger.info(f"Package Manager: Successfully installed homebrew")
        except subprocess.TimeoutExpired:
            process.kill()
            logger.exception(f"Package Manager: Failed to install homebrew")
            raise
    else:
        logger.info(f"Package Manager: Homebrew is already installed")


def uninstall_homebrew():
    if shutil.which("brew") is None:
        logger.info(f"Package Manager: Homebrew is already uninstalled")
    else:
        logger.info(f"Package Manager: Uninstalling homebrew (this may take a while)")
        command = "ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)\""

        process = subprocess.Popen(command.split(), stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        logger.info(f"Package Manager: Successfully uninstalled homebrew")

        # TODO P2: implement
        # It's unknown what parameters we need to pass into the script, so comment this out for now
        # try:
        #     process.communicate('\r')
        # except TimeoutExpired:
        #     process.kill()
        #     PrettyPrint.fail(f"Package Manager: Failed to install homebrew")
        #     raise


"""
User-interfacing functions
"""


def ask_sudo_password():
    PrettyPrint.user(f"Sudo: Actions requiring sudo actions have been detected, please enter your password below (your password is NOT stored at any point in time)")
    sudo_password = getpass.getpass()
    return sudo_password


def get_user_override(action):
    """
    When an issue occurs where the destination of
    a FileAction already exists, we ask the user
    what to do
    """
    while True:
        decision = input(f"Action: File already exists, what would you like to do? [Destination={action.destination}]\n[s]kip, [S]kip all, [o]verwrite, [O]verwrite all, [b]ackup, [B]ackup all\n> ")

        if decision == 's':
            return OverrideAction.SKIP_FILE
        elif decision == 'S':
            return OverrideAction.SKIP_ALL_FILES
        elif decision == 'o':
            return OverrideAction.OVERWRITE_FILE
        elif decision == 'O':
            return OverrideAction.OVERWRITE_ALL_FILES
        elif decision == 'b':
            return OverrideAction.BACKUP_FILE
        elif decision == 'B':
            return OverrideAction.BACKUP_ALL_FILES


"""
General utils
"""


def set_logging(is_quiet, is_verbose):
    if is_quiet:
        logging_level = logging.WARNING
    elif is_verbose:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO

    # Enables normal logging to stdout and errors to stderr
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(PrettyLogFormatter())
    logging.root.addHandler(stderr_handler)

    # See https://github.com/Robpol86/sphinxcontrib-versioning/blob/master/sphinxcontrib/versioning/setup_logging.py
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging_level)
    stdout_handler.setFormatter(PrettyLogFormatter())
    stdout_handler.addFilter(type('', (logging.Filter,), {'filter': staticmethod(lambda r: r.levelno < logging.WARNING)}))
    logging.root.addHandler(stdout_handler)

    logging.root.setLevel(logging_level)