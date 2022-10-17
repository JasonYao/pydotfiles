# Changelog | Pydotfiles

## [4.2.3](https://github.com/JasonYao/pydotfiles/compare/v4.2.2...v4.2.3) (2022-10-17)


### Bug Fixes

* **symlinks:** fixes symlinks to point to the correct absolute path ([2468975](https://github.com/JasonYao/pydotfiles/commit/2468975967874364466fce5427f0a9aec6f57f76)), closes [#86](https://github.com/JasonYao/pydotfiles/issues/86)

## [4.2.2](https://github.com/JasonYao/pydotfiles/compare/v4.2.1...v4.2.2) (2022-10-17)


### Bug Fixes

* **build:** fixes linux build runner when retrieving macos build options ([7c04f1a](https://github.com/JasonYao/pydotfiles/commit/7c04f1a206f4304d5a5197b691b8685074f5bacb))

## [4.2.1](https://github.com/JasonYao/pydotfiles/compare/v4.2.0...v4.2.1) (2022-10-17)


### Bug Fixes

* **build:** fixes the build command's release flag to work for directories without the output dir ([c14a58a](https://github.com/JasonYao/pydotfiles/commit/c14a58a2eedeae2a8770e8fbc735186783fb8f40))

# [4.2.0](https://github.com/JasonYao/pydotfiles/compare/v4.1.0...v4.2.0) (2022-10-17)


### Features

* **build:** adds in the -r or --release flag to the build command, which zips up build packages ([5367eaf](https://github.com/JasonYao/pydotfiles/commit/5367eaf635bd990d5dd42d1859939c67e1a75bd7)), closes [#85](https://github.com/JasonYao/pydotfiles/issues/85)

# [4.1.0](https://github.com/JasonYao/pydotfiles/compare/v4.0.4...v4.1.0) (2022-10-17)


### Features

* **build:** adds in the -b or --build-directory flag to the build command to control output ([65736da](https://github.com/JasonYao/pydotfiles/commit/65736da2e8619ad3292548e8f7bb1bce72c0218d)), closes [#84](https://github.com/JasonYao/pydotfiles/issues/84)

## [4.0.4](https://github.com/JasonYao/pydotfiles/compare/v4.0.3...v4.0.4) (2022-10-17)


### Bug Fixes

* **linux:** fixes build command for linux build runners when generating macos build packages ([d716993](https://github.com/JasonYao/pydotfiles/commit/d716993a9eed351df93947ca0ca6df421b9d1d9a))

## [4.0.3](https://github.com/JasonYao/pydotfiles/compare/v4.0.2...v4.0.3) (2022-10-16)


### Bug Fixes

* **build:** fixes json schema missing from distribution ([0f30e88](https://github.com/JasonYao/pydotfiles/commit/0f30e88117cf7960b9f69034233c50eaa186b7bd))

## [4.0.2](https://github.com/JasonYao/pydotfiles/compare/v4.0.1...v4.0.2) (2022-10-16)


### Bug Fixes

* **build:** adds in non-path json schema resolver to enable build command to work for pip install ([34f0721](https://github.com/JasonYao/pydotfiles/commit/34f0721674346c3bebd8bf49e5ce271cb20b1348))

## [4.0.1](https://github.com/JasonYao/pydotfiles/compare/v4.0.0...v4.0.1) (2022-10-15)


### Bug Fixes

* **build:** fixes build command by including schema files ([fca71f3](https://github.com/JasonYao/pydotfiles/commit/fca71f3e4380412ce273c8653a354748d2557965))

# [4.0.0](https://github.com/JasonYao/pydotfiles/compare/v3.1.0...v4.0.0) (2022-10-15)


### Features

* **build:** adds in dotfile profiles, and ability to generate stand-alone build packages ([9000a65](https://github.com/JasonYao/pydotfiles/commit/9000a6550d096aea69a4b66fc84b8a675012aa06))


### BREAKING CHANGES

* **build:** Introduces dramatically different execution model from the original pydotfiles live
process/live update to an offline build package generation approach

# [3.1.0](https://github.com/JasonYao/pydotfiles/compare/v3.0.0...v3.1.0) (2019-02-15)


### Features

* **developer environments:** Adds in the ability to install language runtimes and specified virtual ([15395b4](https://github.com/JasonYao/pydotfiles/commit/15395b4)), closes [#42](https://github.com/JasonYao/pydotfiles/issues/42) [#43](https://github.com/JasonYao/pydotfiles/issues/43) [#66](https://github.com/JasonYao/pydotfiles/issues/66) [#59](https://github.com/JasonYao/pydotfiles/issues/59)

# [3.0.0](https://github.com/JasonYao/pydotfiles/compare/v2.1.0...v3.0.0) (2019-02-09)


### Features

* **validation:** Formalizes the schema for default setting validation, and enables multiple-schema ([b1bde2d](https://github.com/JasonYao/pydotfiles/commit/b1bde2d)), closes [#57](https://github.com/JasonYao/pydotfiles/issues/57)


### BREAKING CHANGES

* **validation:** Requires a 'version' and 'schema' field for all core and referenced schemas. Valid
schema options currently include 'core' and 'default_settings'

# [2.1.0](https://github.com/JasonYao/pydotfiles/compare/v2.0.0...v2.1.0) (2019-02-06)


### Features

* **dock:** Adds in the ability to set the dock icons via config ([b55d99a](https://github.com/JasonYao/pydotfiles/commit/b55d99a)), closes [#52](https://github.com/JasonYao/pydotfiles/issues/52)

# [2.0.0](https://github.com/JasonYao/pydotfiles/compare/v1.2.0...v2.0.0) (2019-02-06)


### Bug Fixes

* **default-settings:** Fixes sudo command execution and grants the ability to ignore return code val ([f672b6f](https://github.com/JasonYao/pydotfiles/commit/f672b6f))


### BREAKING CHANGES

* **default-settings:** 'run_as_sudo' should instead be called 'sudo'. If you want to ignore return code
errors, please use ''check_output': false'

Fixes 54

# [1.2.0](https://github.com/JasonYao/pydotfiles/compare/v1.1.0...v1.2.0) (2019-02-06)


### Features

* **downloads:** Enables downloading a default set of basic dotfiles if one is not provided ([c0c8651](https://github.com/JasonYao/pydotfiles/commit/c0c8651)), closes [#17](https://github.com/JasonYao/pydotfiles/issues/17)

# [1.1.0](https://github.com/JasonYao/pydotfiles/compare/v1.0.0...v1.1.0) (2019-02-06)


### Features

* **defaults:** Adds in the ability to set default settings for a given OS ([ba7aebd](https://github.com/JasonYao/pydotfiles/commit/ba7aebd)), closes [#46](https://github.com/JasonYao/pydotfiles/issues/46)

# [1.0.0](https://github.com/JasonYao/pydotfiles/compare/v0.1.0...v1.0.0) (2019-02-06)


### Bug Fixes

* **ci/cd:** Fixes the broken test due to an out of date pytest dependency ([8bfea51](https://github.com/JasonYao/pydotfiles/commit/8bfea51)), closes [#50](https://github.com/JasonYao/pydotfiles/issues/50)


### Features

* **validator:** Adds in the ability to validate a given file or directory ([0acc0b9](https://github.com/JasonYao/pydotfiles/commit/0acc0b9)), closes [#9](https://github.com/JasonYao/pydotfiles/issues/9)


### BREAKING CHANGES

* **validator:** All settings.yaml/.json/.yml will now require a 'version' field, with the only
currently available version being 'alpha'

# [0.1.0](https://github.com/JasonYao/pydotfiles/compare/v0.0.5...v0.1.0) (2018-11-23)


### Features

* **ci/cd:** Adds in automatic artifact release for pypi and github (along with automatic semver) ([70bf842](https://github.com/JasonYao/pydotfiles/commit/70bf842)), closes [#3](https://github.com/JasonYao/pydotfiles/issues/3) [#5](https://github.com/JasonYao/pydotfiles/issues/5)
