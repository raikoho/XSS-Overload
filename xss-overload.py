import requests
from termcolor import colored
from pyfiglet import figlet_format
import sys

# ASCII art and intro
def intro():
    print(colored(figlet_format("XSS OVERLORD", font="slant"), "light_yellow"))
    print(colored("Welcome to the XSS OVERLORD for automated GET requests", "light_green"))
    print(colored("Created by Bohdan Misonh, version 1.0", "light_green"))

# Function to detect parameters in URL
def detect_parameters(url):
    if "?" in url:
        params_str = url.split("?")[1]
        params = params_str.split("&")
        return [param.split("=")[0] for param in params]
    return []

# Function to send payloads
def send_payload(url, param, payload):
    try:
        new_url = url.replace(f"{param}=", f"{param}={payload}")
        response = requests.get(new_url)

        # Debugging output for the test payload only
        print(colored(f"Testing payload: {payload}", "light_green"))
        print(colored(f"Response code: {response.status_code}", "light_magenta"))
        print(colored(f"Response length: {len(response.text)} characters", "light_blue"))
        # print(colored(f"Response snippet: {response.text[:200]}", "magenta"))  # Show first 200 chars

        # if payload in response.text:
            # print(colored(f"[SUCCESS] Payload executed on {url}", "light_green"))
        # else:
            # print(colored(f"[FAILED] Payload did not execute", "red"))

    except Exception as e:
        print(colored(f"[ERROR] An error occurred while sending the payload: {str(e)}", "red"))

# Load payloads from file
def load_payloads(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(colored(f"[ERROR] Unable to load payloads from file: {str(e)}", "red"))
        sys.exit()

# Main function
def main():
    intro()

    try:
        # Input URL
        url = input(colored("Enter the URL: ", "cyan"))

        # Auto-detect parameters
        params = detect_parameters(url)
        if not params:
            print(colored("No parameters found in the URL!", "red"))
            return

        print(colored("Parameters found:", "yellow"))
        for idx, param in enumerate(params, start=1):
            print(f"{idx}. {param}")

        param_index = int(input(colored("Choose a parameter to test (number): ", "cyan"))) - 1
        param = params[param_index]

        # Select payload file
        print(colored("Select payload source:", "yellow"))
        print("1. Use default payload file")
        print("2. Enter custom path")
        payload_choice = input(colored("Enter your choice (1/2): ", "cyan"))

        if payload_choice == "1":
            filepath = "payloads.txt"  # Replace with your actual default path
        else:
            filepath = input(colored("Enter the path to your payload file: ", "cyan"))

        # Load payloads and brute force
        payloads = load_payloads(filepath)
        for payload in payloads:
            send_payload(url, param, payload)

    except KeyboardInterrupt:
        print(colored("\nProgram interrupted by user. Exiting...", "yellow"))
        sys.exit()
    except Exception as e:
        print(colored(f"[ERROR] An unexpected error occurred: {str(e)}", "red"))
        sys.exit()

if __name__ == "__main__":
    main()

