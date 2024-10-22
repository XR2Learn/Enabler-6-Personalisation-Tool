# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.3] - 2024 - 07 - 25
### Changed 
- Refactoring

### Added 
- Support for BM (bio-measurements) modality with data from Magic XRoom.

## [0.2.2] - 2024-03-12
### Changed 
-  License Update to Apache 2.0.

### Known Issues
- No support for BM (bio-measurements) modality with data from Magic XRoom.

## [0.2.1] - 2024-02-15

### Added

- More documentation
- License

## [0.2.0] - 2024-01-19

### Added

- More documentation
- DemoUI v2: with Emotions not simulated anymore, but coming from the multimodal fusion layer component (Inference)
- DemoUI v3: with Unity App not simulated anymore, but coming from a Unity App.
- Three different DemoUI, depending on which component is simulated.

## [0.1.1] - 2023-12-06

### Added

- More user-friendly messages with the next activity level.
- Documentation

### Fixed

- ~~Bug: An error occurring when there is no emotion to consider.~~

## [0.1.0] - 2023-10-31

### Added

- Basic version of Enablers 6: Personalisation tool.
    - Implementing a Pub/Sub messaging pattern.
    - Using REDIS as a message broker.
    - Personalisation function implements a majority voting for defining the emotion of activity.
    - Simulate input/output script.
- A DemoUI to showcase Enabler 6 functionality.
    - Flask app using websockets (sockets.io)
- Changelog

### Known Issues

- Bug: An error occurring when there is no emotion to consider.

<!-- 
Example of Categories to use in each release

### Added
- Just an example of how to use changelog.

### Changed
- Just an example of how to use changelog.

### Fixed
- Just an example of how to use changelog.

### Removed
- Just an example of how to use changelog.

### Deprecated
- Just an example of how to use changelog. -->


[unreleased]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/compare/v0.2.3...master

[0.1.0]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/releases/tag/v0.1.0

[0.1.1]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/releases/tag/v0.1.1

[0.2.0]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/releases/tag/v0.2.0

[0.2.1]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/releases/tag/v0.2.1

[0.2.2]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/releases/tag/v0.2.2

[0.2.3]: https://github.com/XR2Learn/Enabler-6-Personalisation-Tool/releases/tag/v0.2.3