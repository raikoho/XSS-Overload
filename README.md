# XSS-Overload
Super fast and optimized XSS Overload for GET requests parameters using a dictionary for payloads.
This is a Python-based tool designed to automate the process of testing for Cross-Site Scripting (XSS) vulnerabilities on web applications. This tool allows security researchers and ethical hackers to efficiently execute various payloads against specified parameters in GET requests and also introduces automatic parameter determination.

## Features

- **Automated Payload Injection**: Automatically injects XSS payloads into specified parameters of a target URL.
- **Dynamic Parameter Detection**: Automatically detects parameters in the URL, allowing for a seamless testing experience.
- **Custom Payload File Support**: Users can specify their own payload files or utilize reserved payloads included with the tool - Provision of own dictionary with popular XXE.
- **User-Friendly Interface**: Terminal interface with colorful output to enhance the user experience.

## Installation

To get started with XSS Overload, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/raikoho/XSS-Overload.git
    cd XSS-Overload
    python3 xss-overload.py
    ```

2. **Install required packages**:
    Ensure you have Python 3.x installed, then run:
    ```bash
    pip install termcolor requests pyfiglet
    ```

## Usage

1. Run the tool:
    ```bash
    python xss-overload.py
    ```

2. Follow the on-screen instructions:
   - Enter the target URL.
   - The tool will automatically detect GET parameters.
   - Select the parameter to test.
   - Choose the payload file (either the default or your custom one).

3. Review the results for any successful payload executions.

## Wordlist

Use default included payloads.txt for over XXE payloads.
Or plug in your own.

## Thank you

Thank you for using this tool. Please write to me if you have your own ideas on how to make it even better.
