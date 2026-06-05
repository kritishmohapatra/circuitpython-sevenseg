# Changelog

All notable changes to this project will be documented in this file.

## 1.0.0 (2026)

### Added
- Initial release
- Support for digits 0-9
- Support for uppercase A-Z (except K, M, V, W, X)
- Support for lowercase a-z (except k, m, v, w, x, z)
- Support for symbols: `- _ . ! ? ' " [ ] = + ^ (space)`
- Common cathode and common anode support
- `show(char, dp=False)` — display any supported character
- `clear()` — turn off all segments
- `dot(on=True)` — toggle decimal point only
- `deinit()` — release all GPIO pins
- Examples: simpletest, all chars, input test
- Tested on Raspberry Pi Pico 2W