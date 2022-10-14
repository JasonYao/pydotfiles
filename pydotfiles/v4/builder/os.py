# General imports
from platform import mac_ver
from logging import getLogger

# Project imports
from pydotfiles.v4.common.alpha import DefaultSettings
from pydotfiles.v4.common.alpha.default_settings import MacVersion
from pydotfiles.v4.common.alpha.os import PackageManager, OperatingSystem

logger = getLogger(__name__)

##
# OS packages installation
##


def template_os_packages(data: OperatingSystem) -> str:
    if len(data.packages) == 0:
        return ""

    package_manager_package_installer = {
        PackageManager.yum: __template_yum_packages,
        PackageManager.brew: __template_homebrew_packages,
        PackageManager.apt: __template_apt_packages,
    }
    return package_manager_package_installer.get(data.package_manager)(data)


def __template_yum_packages(data: OperatingSystem) -> str:
    logger.error("TODO: Implement template yum packages")
    return ""


def __template_homebrew_packages(data: OperatingSystem) -> str:
    homebrew_packages = f"homebrew_packages = ({' '.join(data.packages)})\n"

    setup = f"""
    # TODO: move this into config
    # Any packages that requires flags upon
    # install should be both above and here
    declare -A flagged_packages
    flagged_packages[grep]=--with-default-names
    flagged_packages[gnu-sed]=--with-default-names
    flagged_packages[gnu-tar]=--with-default-names

    tmp_homebrew_cache_file=$(mktemp /tmp/pydotfiles-homebrew-cache)
    """

    install_function = r"""
    function check_homebrew_package() {
        package_name=$1

        if [[ $(grep "${package_name}" "${tmp_homebrew_cache_file}") == "" ]]; then
            info "Homebrew: Package ${package_name} has not been installed yet, installing now"
            if brew install "${package_name}" ${flagged_packages[${package_name}]} &> /dev/null ; then
                success "Homebrew: Package ${package_name} is now installed"
            else
                fail "Homebrew: Package ${package_name} failed to install"
            fi
        else
            success "Homebrew: Package ${package_name} is already installed"
        fi
    }

    function cache_brew_packages() {
        # -t sorts by time modified
        # -1 makes the packages each go on a single line
        brew list -t1 > "$tmp_homebrew_cache_file"
    }

    cache_brew_packages

    # Updates and upgrades brew packages
    info "Homebrew: Updating brews now"
    if brew update; then
        success  "Homebrew: Brews have been updated"
    else
        fail "Homebrew: Brews failed to be updated"
    fi

    info "Homebrew: Upgrading brews now"
    if brew upgrade; then
        success "Homebrew: Brews have been upgraded"
    else
        fail "Homebrew: Brews failed to upgrade"
    fi

    # Checks and installs any missing packages
    info "Homebrew: Checking installed packages"
    for package in "${homebrew_packages[@]}"; do
        check_homebrew_package "${package}"
    done
    """
    return homebrew_packages + setup + install_function


def __template_apt_packages(data: OperatingSystem) -> str:
    apt_packages = f"apt_packages = ({' '.join(data.packages)})\n"

    package_installation_function = r"""
    function check_and_install_package () {
        info "APT: Checking for $1"
        if dpkg -s "$1" > /dev/null 2>&1 ; then
            success "APT: $1 is already installed"
        else
            info "APT: $1 not found, installing now"
            if sudo apt-get install "$1" -y &> /dev/null ; then
                success "APT: $1 successfully installed"
            else
                fail "APT: $1 failed to install"
            fi
        fi
    }
    
    function update_and_upgrade () {
        # Updates & upgrades
        info "APT: Updating packages"
        if sudo apt-get update -y > /dev/null ; then
            success "APT: Packages were updated"
        else
            fail "APT: Packages were unable to be updated"
        fi
    
        info "APT: Upgrading packages"
        if sudo apt-get dist-upgrade -y > /dev/null ; then
            success "APT: Packages were upgraded"
        else
            fail "APT: Packages were unable to be upgraded"
        fi
    }
    
    function auto_remove () {
        # Auto removes any unnecessary packages
        info "APT: Auto removing any unnecessary packages"
        if sudo apt-get autoremove -y > /dev/null ; then
            success "APT: All unnecessary packages removed"
        else
            fail "APT: Unable to remove unnecessary packages"
        fi
    }
    
    # Does first-time initial setup if the user has root/sudo privileges
    if [[ $(groups | grep 'root\|admin\|sudo') != "" ]]; then
        # Does server setup
        update_and_upgrade
        
        for package in "${apt_packages[@]}"; do
            check_and_install_package "${package}"
        done
        auto_remove
    else
        warn "APT: $username does not have the correct permissions to install dependencies"
    fi
    """
    return apt_packages + package_installation_function


##
# OS applications installation
##


def template_os_applications(data: OperatingSystem) -> str:
    if len(data.applications) == 0:
        return ""

    package_manager_package_installer = {
        PackageManager.yum: __template_yum_applications,
        PackageManager.brew: __template_homebrew_applications,
        PackageManager.apt: __template_apt_applications,
    }
    return package_manager_package_installer.get(data.package_manager)(data)


def __template_yum_applications(data: OperatingSystem) -> str:
    logger.error("TODO: Implement template yum applications")
    return ""


def __template_homebrew_applications(data: OperatingSystem) -> str:
    cask_applications = f"cask_packages = ({' '.join(data.applications)})\n"

    install_function = r"""
    function check_homebrew_cask_package() {
        cask_name=$1

        if [[ $(grep "${cask_name}" "${tmp_homebrew_cache_file}") == "" ]]; then
            info "Homebrew-Cask: Application ${cask_name} has not been installed yet, installing now"
            if brew cask install "${cask_name}" &> /dev/null ; then
                success "Homebrew Casks: Application ${cask_name} is now installed"
            else
                fail "Homebrew Casks: Application ${cask_name} failed to install"
            fi
        else
            success "Homebrew Casks: Application ${cask_name} is already installed"
        fi
    }

    # Checks and installs any missing packages
    info "Homebrew Casks: Checking application statuses"
    for package in "${cask_packages[@]}"; do
        check_homebrew_cask_package "${package}"
    done
    """
    return cask_applications + install_function


def __template_apt_applications(data: OperatingSystem) -> str:
    logger.error("TODO: Implement template apt applications")
    return ""

##
# OS default dock
##


def template_os_default_dock(data: OperatingSystem) -> str:
    """
    We only support this on macos for now, not sure if there's a way to programmatically setup the desktop
    for a linux GUI (there probably is, but I'm too lazy to figure it out)
    """
    if len(data.default_dock) == 0:
        return ""

    header = """

    ##
    # Removes all non-essential dock apps and replaces them with our designated ones
    ##

    """

    valid_apps = f"""
    # Apps that you want included in the default dock
    valid_apps=("launchpad" "Notes" "iTunes" "appstore" "systempreferences" "firefox")
    """

    repopulate_function = """
    function repopulate_all_dock_apps() {
    """

    for default_dock_item in data.default_dock:
        repopulate_function += f"""check_and_manage_dock_apps "{default_dock_item}"
        """

    repopulate_function += """
        killall Dock
    }
    """

    return header + valid_apps + repopulate_function + r"""
    # Does this once instead of doing all over each time
    invert_string="grep -v"

    for app in "${valid_apps[@]}"; do
        invert_string+=" -e \"${app}\""
    done

    function check_and_remove_bad_dock_apps() {
        if [[ $(defaults read com.apple.Dock persistent-apps | grep "bundle-identifier" | eval "$invert_string") != "" ]]; then
            info "Dock: Contains non-default applications, killing off now"
            defaults delete com.apple.Dock persistent-apps
            killall Dock
            success "Dock: All non-default applications are now sanitised"
        else
            success "Dock: All non-default applications are already sanitised"
        fi
        info "Dock: Checking for all default app existences"
        repopulate_all_dock_apps
        success "Dock: All default apps are in place"
    }

    check_and_remove_bad_dock_apps
    """


def template_os_default_setting_files(data: OperatingSystem) -> str:
    if len(data.default_settings_files) == 0:
        return ""

    default_settings = ""
    for default_setting in data.default_settings_data:
        default_settings += template_os_default_setting(default_setting)
    return default_settings


def template_os_default_setting(data: DefaultSettings) -> str:
    if not data.should_run(get_current_mac_version()):
        return f"""
        # Command {data.name} is disabled since it was detected to not be in a valid version range or is manually disabled
        # Description: {data.description}
        """

    info_message = f"""

    ##
    # Setting default settings
    ##

    info "{data.name}"

    """

    command_check = f"""
    {f'if [[ {data.check_command} == {data.expected_check_state} ]]; then' if data.check_output else ''}
    {f'    success "{data.name}: Successfully completed previously"' if data.check_output else ''}
    {f'else' if data.check_output else ''}

    {f'    if {"sudo " if data.sudo else ""}{data.command} ; then'}
    {f'        success "{data.name}: Successfully executed command"'}    
    {f'        {data.post_command}'}
    {f'    else'}
    {f'        warn "{data.name}: Failed to complete"'}
    {f'    fi'}

    {f'fi' if data.check_output else ''}
    """
    return info_message + command_check


def get_current_mac_version():
    current_version = mac_ver()[0]
    return MacVersion.from_version(current_version)
