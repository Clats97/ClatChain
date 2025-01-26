import time
import sys
import msvcrt
import requests

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
        print(f"Error fetching '{coin_id}' price from Coingecko: {e}")
        return None


def get_coin_id(user_input):
    
    return COINGECKO_ID_MAP.get(user_input.lower().strip())


def fetch_and_display_price(coin):
  
    while True:
        coin_id = get_coin_id(coin)
        if coin_id is None:
            print(f"'{coin}' is not recognized or not mapped to a Coingecko ID.")
            print("Press ENTER to search another coin, or type 'exit' to quit.")
            if wait_for_user_input_or_timeout(10) == "exit":
                sys.exit(0)
            return

        price = get_coingecko_price(coin_id)
        if price is not None:
            print(f"[{time.strftime('%H:%M:%S')}] {coin.upper()} Price: ${price:,.4f}")
        else:
            print(f"Could not fetch price for '{coin.upper()}'. Check network or spelling.")

        print("Press enter to search for another coin, type 'exit' to close the program, or wait 5 minutes for the next update...")

        user_typed = wait_for_user_input_or_timeout(300)
        if user_typed is not None:
            if user_typed.lower() == "exit":
                print("Exiting program.")
                sys.exit(0)
            break


def wait_for_user_input_or_timeout(timeout=5.0):
  
    start_time = time.time()
    buffer = []

    while (time.time() - start_time) < timeout:
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == '\r':
                return ''.join(buffer).strip()
            elif char in ('\b', '\x08'):
                if buffer:
                    buffer.pop()
            else:
                buffer.append(char)
        time.sleep(0.1)

    return None

def main():
    print("Welcome to ClatChain Crypto Checker.")
    print("Updates the chosen coin price every 5 minutes.\n")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        user_coin = input("Enter a coin (e.g., BTC, ETH, DOGE, LTC, USDT) or 'exit' to quit: ").strip()
        if user_coin.lower() == "exit":
            print("Exiting program.")
            break

        if not user_coin:
            continue

        print(f"\nPrice will be updated every 5 minutes for {user_coin.upper()}...\n")
        fetch_and_display_price(user_coin)


if __name__ == "__main__":

    print("\033[1;31m ██████╗    ██╗          █████╗     ████████╗     ██████╗    ██╗  ██╗     █████╗     ██╗    ███╗   ██╗")
    print("██╔════╝    ██║         ██╔══██╗    ╚══██╔══╝    ██╔════╝    ██║  ██║    ██╔══██╗    ██║    ████╗  ██║")
    print("██║         ██║         ███████║       ██║       ██║         ███████║    ███████║    ██║    ██╔██╗ ██║")
    print("██║         ██║         ██╔══██║       ██║       ██║         ██╔══██║    ██╔══██║    ██║    ██║╚██╗██║")
    print("╚██████╗    ███████╗    ██║  ██║       ██║       ╚██████╗    ██║  ██║    ██║  ██║    ██║    ██║ ╚████║")
    print(" ╚═════╝    ╚══════╝    ╚═╝  ╚═╝       ╚═╝        ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝    ╚═╝  ╚═══╝\033[0m")

    print("\033[1;34mC L A T C H A I N       C R Y P T O       T O O L\033[0m   \033[1;31m(Version 1.00)\033[0m\n")
    author = "🛡️ By Josh Clatney - Ethical Pentesting Enthusiast 🛡️"
    print(author + "\n[Crypto Price Tool]\nCrypto Clarity In Seconds\n")

    main()