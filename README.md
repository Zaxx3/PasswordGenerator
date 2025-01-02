# Password Generator

A Python-based GUI application for generating customizable passwords. This tool allows you to specify the length, include specific words (or parts of them), and generate multiple passwords at once. The generated passwords can also be saved to a file.

## Features

- **Customizable Length**: Specify the desired length of each password.
- **Include Words**: Add specific words, and parts of those words will be randomly used in the passwords.
- **Generate Multiple Passwords**: Define how many passwords to generate at once.
- **Save Passwords**: Save the generated passwords to a `.txt` file.
- **User-Friendly GUI**: Intuitive and easy-to-use graphical interface built with `tkinter`.

## Requirements

- Python 3.x
- `tkinter` (pre-installed with Python on most systems)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-generator
   cd password-generator
   ```
2. Run the script:
   ```bash
   python password_generator_gui.py
   ```

## Usage

1. Open the application.
2. Enter the desired password length.
3. Specify the number of passwords to generate.
4. Optionally, add words (comma-separated) to include parts of them in the passwords.
5. Click **Generate Password** to create passwords.
6. View the generated passwords in the text box.
7. Click **Save Passwords** to save the passwords to a `.txt` file.

## Example

- **Password Length**: `12`
- **Number of Passwords**: `5`
- **Words**: `example,secure`

Generated passwords might look like:
```
excur2!a3Ex@pl
SecuExmpl45!
sE#xmplu7@re
... (3 more passwords)
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
