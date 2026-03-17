# Cherab Stubs

Type stubs for the [Cherab](https://github.com/cherab/core) library, providing type annotations for static type checkers like `mypy`.

## Installation

```bash
pip install cherab-stubs
```

## Usage

Once installed, type checker like `mypy` will automatically use these stubs when type-checking code that uses the Cherab library.

## Development

### Setting up the development environment

1. Clone this repository
2. Install [pixi](https://pixi.sh/) if you haven't already
3. Set up the development environment:
   ```bash
   pixi install
   pixi run test
   ```

### Running type checks

```bash
pixi run type-check
```

### Running tests

```bash
pixi run test
```

### Code formatting and linting

```bash
pixi run lint
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.
