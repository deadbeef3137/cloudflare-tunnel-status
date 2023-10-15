# Cloudflare Tunnel Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Cloudflare Tunnel Monitor|128](https://raw.githubusercontent.com/deadbeef3137/ha-cloudflare-tunnel-monitor/master/images/cloudflare-tunnel.png)


# About
This script is designed to interact with the Cloudflare API to retrieve the status of available tunnels. It fetches and displays details about each tunnel such as its name, ID, and status. The script fetches credential information from environment variables and utilizes the requests library to interact with the API.

# Requirements

### Python Version

Ensure that Python 3.12 is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Dependencies Installation
All dependencies required for the script to run are included in the `requirements.txt` file. You can install them using pip with the following command:

```bash
pip install -r requirements.txt
```

In the case the `requirements.txt` file is not provided, you must install the necessary packages manually. For the given script, you'll need:

`python-dotenv`: to handle the loading of environment variables from a `.env` file.

`requests`: to make HTTP requests.

You can install these packages by running:
```bash
pip install python-dotenv requests
```

## Setup

### Environment Variables
The script uses environment variables to safely store and use sensitive data, like the Cloudflare API key and email. Ensure to set up your environment variables in a `.env` file in the same directory as your script with the following format:

```dotenv
CLOUDFLARE_EMAIL=your_cloudflare_email
CLOUDFLARE_GLOBAL_API_KEY=your_cloudflare_global_api_key
CLOUDFLARE_ACCOUNT_ID=your_cloudflare_account_id
```
Replace the placeholder values with your actual Cloudflare credentials.

## Usage

After fulfilling the prerequisites and setting up the environment variables, you can run the script using Python:

```bash
python cloudflare_tunnel.py
```

## Output

Upon successful execution, the script will fetch and display the status of available tunnels from Cloudflare in the following format:

```plaintext
Tunnels:

[Tunnel Name] | ID: [Tunnel ID] | Status: [Tunnel Status]
```
If it encounters an issue, it will display an error message indicating the HTTP status code and response text.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements, bug fixes, or additional functionality. Always ensure to follow best practices for coding and adhere to the current structure of the script.

## License
This integration is released under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer

This project is not affiliated with or endorsed by Cloudflare.
