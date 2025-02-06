import time
import sys
import requests
import tkinter as tk
from tkinter import ttk, messagebox
import threading

COINGECKO_ID_MAP = {
    "btc": "bitcoin",
    "bitcoin": "bitcoin",
    "eth": "ethereum",
    "ethereum": "ethereum",
    "xrp": "xrp",
    "tether": "tether",
    "usdt": "tether",
    "solana": "solana",
    "sol": "solana",
    "bnb": "binancecoin",
    "dogecoin": "dogecoin",
    "doge": "dogecoin",
    "usdc": "usd-coin",
    "cardano": "cardano",
    "ada": "cardano",
    "lido staked ether": "lido-staked-ether",
    "steth": "lido-staked-ether",
    "tron": "tron",
    "trx": "tron",
    "chainlink": "chainlink",
    "link": "chainlink",
    "avalanche": "avalanche-2",
    "avax": "avalanche-2",
    "wrapped steth": "wrapped-steth",
    "wsteth": "wrapped-steth",
    "wrapped bitcoin": "wrapped-bitcoin",
    "wbtc": "wrapped-bitcoin",
    "sui": "sui",
    "stellar": "stellar",
    "xlm": "stellar",
    "hedera": "hedera-hashgraph",
    "hbar": "hedera-hashgraph",
    "toncoin": "toncoin",
    "ton": "toncoin",
    "shiba inu": "shiba-inu",
    "shib": "shiba-inu",
    "weth": "weth",
    "polkadot": "polkadot",
    "dot": "polkadot",
    "leo token": "leo-token",
    "leo": "leo-token",
    "litecoin": "litecoin",
    "ltc": "litecoin",
    "bitget token": "bitget-token",
    "bgb": "bitget-token",
    "bitcoin cash": "bitcoin-cash",
    "bch": "bitcoin-cash",
    "hyperliquid": "hyperliquid",
    "uniswap": "uniswap",
    "uni": "uniswap",
    "official trump": "official-trump-2024",
    "usds": "stableusd",
    "pepe": "pepe",
    "ethereum classic": "ethereum-classic",
    "etc": "ethereum-classic",
    "render": "render-token",
    "rndr": "render-token",
}

def get_coingecko_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}
    try:
        resp = requests.get(url, params=params)
        data = resp.json()
        return data.get(coin_id, {}).get("usd")
    except Exception as e:
        return f"Error fetching '{coin_id}' price: {e}"

def get_coin_id(user_input):
    return COINGECKO_ID_MAP.get(user_input.lower().strip())

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ClatChain Crypto Checker")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.create_widgets()
        self.updating = False

    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10)

        header_label = ttk.Label(header_frame, text="ClatChain Crypto Tool", font=("Helvetica", 17, "bold"))
        header_label.pack()

        version_label = ttk.Label(header_frame, text="(Version 1.0.1)", font=("Helvetica", 10))
        version_label.pack()

        author_label = ttk.Label(header_frame, text="By Josh Clatney - Ethical Pentesting Enthusiast", font=("Helvetica", 9))
        author_label.pack(pady=(5, 15))

        # Input Frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        coin_label = ttk.Label(input_frame, text="Enter Coin Symbol:")
        coin_label.pack(side=tk.LEFT, padx=(0, 10))

        self.coin_entry = ttk.Entry(input_frame, width=30)
        self.coin_entry.pack(side=tk.LEFT)

        fetch_button = ttk.Button(input_frame, text="Fetch Price", command=self.start_fetching)
        fetch_button.pack(side=tk.LEFT, padx=(10, 0))

        # Status Frame
        status_frame = ttk.Frame(self.root)
        status_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.status_text = tk.Text(status_frame, wrap=tk.WORD, state=tk.DISABLED, height=10)
        self.status_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Control Frame
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        self.exit_button = ttk.Button(control_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack()

    def log_message(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, str(message) + "\n")  # Convert message to string
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)

    def start_fetching(self):
        if self.updating:
            messagebox.showinfo("Info", "Already fetching prices. Please wait.")
            return

        coin = self.coin_entry.get().strip()
        if not coin:
            messagebox.showwarning("Input Error", "Please enter a coin symbol.")
            return

        if coin.lower() == "exit":
            self.root.quit()
            return

        self.updating = True
        self.log_message(f"Fetching price for {coin.upper()}...\n")
        threading.Thread(target=self.fetch_and_display_price, args=(coin,), daemon=True).start()

    def fetch_and_display_price(self, coin):
        while self.updating:
            coin_id = get_coin_id(coin)
            if coin_id is None:
                self.log_message(f"'{coin}' is not recognized or not mapped to a CoinGecko ID.")
                self.updating = False
                return

            price = get_coingecko_price(coin_id)
            timestamp = time.strftime('%H:%M:%S')
            if isinstance(price, (int, float)):  # Updated to handle both int and float
                self.log_message(f"[{timestamp}] {coin.upper()} Price: ${price:,.4f}")
            else:
                self.log_message(price)

            self.log_message("Waiting for the next update in 1 minute...\n")
            # Wait for 5 minutes or until the user stops the updating
            for _ in range(60):
                if not self.updating:
                    break
                time.sleep(1)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.updating = False
            self.root.destroy()

def main():
    root = tk.Tk()
    app = CryptoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()