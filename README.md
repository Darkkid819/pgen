# Secure Password Generator

A simple Python script to generate secure passwords with customizable options.

## Usage

To generate a password, run the script with the following options:

```bash
python pgen.py [options]
```

### Options

- `--length`: Length of the password (default: 12).
- `--no-uppercase`: Exclude uppercase letters.
- `--no-lowercase`: Exclude lowercase letters.
- `--no-numbers`: Exclude numbers.
- `--no-special`: Exclude special characters.

### Examples

- Generate a 12-character password (default options):

  ```bash
  python pgen.py
  ```

- Generate a 16-character password without special characters:

  ```bash
  python pgen.py --length 16 --no-special
  ```

- Generate an 8-character password with only numbers:

  ```bash
  python pgen.py --no-uppercase --no-lowercase --no-special --length 8
  ```
