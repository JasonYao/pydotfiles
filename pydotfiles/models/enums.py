from enum import Enum, auto
from pydotfiles.utils import BijectiveDictionary


"""
Model enums
"""


class FileActionType(Enum):
    """
    Represents what kind of file operation
    this FileAction is
    """
    COPY = auto()
    DELETE = auto()

    SYMLINK = auto()
    UNSYMLINK = auto()

    SCRIPT = auto()
    UNDO_SCRIPT = auto()

    @staticmethod
    def from_string(label):
        if label is None:
            raise KeyError("Enum: No file action was passed in")
        return FileActionType[label.upper()]

    @staticmethod
    def get_reverse(file_action_type):
        file_action_reverse_mapping = BijectiveDictionary({
            FileActionType.COPY: FileActionType.DELETE,
            FileActionType.SYMLINK: FileActionType.UNSYMLINK,
            FileActionType.SCRIPT: FileActionType.UNDO_SCRIPT
        })
        return file_action_reverse_mapping.get(file_action_type)


class OS(Enum):
    """
    Represents a given operating system
    """
    MACOS = auto()
    LINUX = auto()
    UBUNTU = auto()
    CENTOS = auto()

    @staticmethod
    def from_string(label):
        if label is None:
            raise KeyError("Enum: No operating system was passed in")

        if label == "darwin":
            return OS.MACOS

        return OS[label.upper()]

    @staticmethod
    def get_package_manager(os):
        return {
            OS.MACOS: PackageManager.BREW,
            OS.LINUX: PackageManager.APT,
            OS.UBUNTU: PackageManager.APT,
            OS.CENTOS: PackageManager.YUM
        }.get(os)


class PackageManager(Enum):
    """
    Represents a system package manager
    """
    BREW = auto()

    # Linux package managers
    YUM = auto()
    APT = auto()

    @staticmethod
    def from_label(label):
        if label is None:
            raise KeyError("Enum: No package manager was passed in")
        return PackageManager[label.upper()]


class OverrideAction(Enum):
    """
    Represents an override action that
    a user can input when deciding what
    to do about certain file actions
    """

    SKIP_FILE = auto()
    SKIP_ALL_FILES = auto()

    OVERWRITE_FILE = auto()
    OVERWRITE_ALL_FILES = auto()

    BACKUP_FILE = auto()
    BACKUP_ALL_FILES = auto()

    @staticmethod
    def from_label(label):
        if label is None:
            raise KeyError("Enum: No override action was passed in")
        return OverrideAction[label.upper()]

    @staticmethod
    def affects_multiple_files(override_action):
        return override_action in {
            OverrideAction.SKIP_ALL_FILES,
            OverrideAction.OVERWRITE_ALL_FILES,
            OverrideAction.BACKUP_ALL_FILES
        }


"""
Exception enums
"""


class PydotfilesErrorReason(Enum):
    """
    Represents a particular reason why
    the pydotfiles failed, enables extraction
    of a potentially useful help message
    as well
    """

    UNKNOWN_ERROR = auto()
    NO_REMOTE_REPO = auto()
    REMOTE_REPO_CLONE_ISSUE = auto()
    UNKNOWN_CLEANING_TARGET = auto()
    UNKNOWN_MODULE_NAME = auto()

    @staticmethod
    def get_help_message(reason):
        help_message_map = {
            PydotfilesErrorReason.UNKNOWN_ERROR: None
        }
        return help_message_map.get(reason)