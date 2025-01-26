# ClatChain Crypto Checker

A command-line Python tool that fetches current cryptocurrency prices from [CoinGecko](https://www.coingecko.com/en/api) and updates them at a user-defined interval (default: 5 minutes). This script is primarily designed for Windows environments, using `msvcrt` for non-blocking user input.

![clatchain](https://github.com/user-attachments/assets/b7db449d-2e70-4b32-b1ff-298a760b4009)

## Features
**Real-Time Price Fetching**: Retrieves the latest price (in USD) for various coins from CoinGecko’s Simple Price API.
**Coin Name Mappings**: Includes a built-in dictionary (`COINGECKO_ID_MAP`) for handling common coin names and tickers (e.g., `BTC`, `ETH`, `DOGE`, etc.).
**Auto-Update Loop**: Continuously updates the selected coin’s price every 5 minutes (or until user input).
**Interactive Input**: 
  - Press **Enter** to change to a different coin.
  - Type **exit** to terminate the program at any prompt.
**Error Handling**: Gracefully handles network errors or mismatched coin names.

## How It Works

1. **Initialization**:  
   - Displays an ASCII banner.  
   - Prompts the user to enter a cryptocurrency name or ticker.

2. **Coin Validation**:
   - The script checks the user’s input against the `COINGECKO_ID_MAP` dictionary.  
   - If a match is found (e.g., input `BTC` → `'bitcoin'` in the map), the corresponding CoinGecko ID is returned.
   - If no match is found, the user is prompted to enter a new coin name or exit.

3. **Fetching Prices**:
   - Using the identified CoinGecko ID, the script queries the [CoinGecko Simple Price API](https://www.coingecko.com/en/api/documentation) to retrieve the coin’s current USD price.
   - On success, it prints the fetched price to the console.  
   - On failure, it logs an error message indicating the issue (e.g., network error).

4. **Continuous Update Loop**:
   - After fetching the price once, the script waits up to 5 minutes (300 seconds) before fetching the price again.  
   - The user can interrupt this waiting period by pressing **Enter**, allowing them to search for another coin or by typing **exit** to terminate the program.

5. **User Input (Non-Blocking)**:
   - The script uses `msvcrt` (a Windows-specific Python library) to detect keystrokes without blocking program execution.  
   - If no input is detected within the specified timeout, the script proceeds to re-fetch the price.

## Installation

1. **Requirements**:
   - **Python 3.6+**  
   - **Windows OS** (due to `msvcrt` usage)  

2. **Python Libraries**:
   - `time` (standard library)
   - `sys` (standard library)
   - `msvcrt` (Windows-only standard library)
   - `requests` (third-party library for HTTP requests)

3. **Install Required Libraries**:

pip install requests

## Usage

1. **Clone or Download**:
   - Clone or download this repository or copy the script file into your local system.

2. **Run the Script**:

3. **Enter the Coin**:
   - Input the ticker or name of the cryptocurrency when prompted (e.g., `BTC`, `ETH`, `DOGE`, `ADA`).
   - Press **Enter** to confirm.

4. **Wait for Updates**:
   - The script displays the current price and updates it every 5 minutes, unless interrupted by user input.
   - **Press Enter**: Switch to a different coin.
   - **Type exit**: Terminates the program at any prompt.

## Configuration

- **Fetch Interval**:
  - By default set to **5 minutes**.  
  - You can adjust the `timeout` argument in `fetch_and_display_price(coin)` if you need to change it.

- **Coin Mapping**:
  - The dictionary `COINGECKO_ID_MAP` can be extended to include more coin name mappings or custom aliases.

## Limitations and Warnings

1. **Windows-Only**:  
   - The script uses `msvcrt`, which is exclusive to Windows.  
   - To use it on MacOS or Linux, you would need to replace `msvcrt` with a different mechanism for non-blocking user input.

2. **Network Reliability**:  
   - Relies on an active internet connection to fetch live data from the CoinGecko API.

3. **CoinGecko API Rate Limits**:  
   - The free tier of the CoinGecko API can limit requests per minute. If you exceed these limits, you may receive errors or get temporarily blocked. Check CoinGecko’s [API Documentation](https://www.coingecko.com/en/api/documentation) for more details.

4. **Not an Investment Tool**:  
   - The script is solely for **informational** purposes, and **does not** provide any financial or trading advice.

## Troubleshooting

**Error Fetching Price**:
  - Ensure you have a stable internet connection.
  - Verify the coin name or ticker is included in the `COINGECKO_ID_MAP` dictionary.  
  - Check if the CoinGecko API is online.

**Script Closes Immediately**:
  - Run the script from a command prompt (e.g., PowerShell or CMD) to view output before it closes.

**Keyboard Input Not Detected**:
  - Confirm you are using Windows.  
  - If you are using MacOS or Linux, you need a cross-platform approach for detecting keystrokes (e.g., `select` or `curses` module).

**Author**: Joshus M Clatney (clats97) – Ethical Pentesting Enthusiast 
**Version**: 1.00  

**Disclaimer**: This tool is provided “as is” for informational purposes only. Always verify prices with reliable sources before making financial decisions.

Copyright 2025 Johua M Clatney (Clats97)
