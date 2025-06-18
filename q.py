import asyncio
from pyppeteer import launch

async def request_faucet_tokens(network_name, wallet_address):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://faucet.quicknode.com/')

    # Example: Select network from dropdown or UI element
    # This depends on the actual page structure, adjust selectors accordingly
    await page.waitForSelector('#network-select')
    await page.select('#network-select', network_name)  # network_name should match option value

    # Connect wallet step - may require manual intervention or advanced automation
    # For example, click "Connect Wallet" button
    await page.click('#connect-wallet-button')
    # Automate wallet connection here if possible (complex)

    # Input wallet address if needed
    await page.type('#wallet-address-input', wallet_address)

    # Click request faucet button
    await page.click('#request-faucet-button')

    # Wait for confirmation or success message
    await page.waitForSelector('.success-message', timeout=10000)

    print(f"Requested faucet tokens for {network_name} to {wallet_address}")

    await browser.close()

# Example usage for 8 networks
async def main():
    wallet_address = '0xYourWalletAddressHere'
    networks = [
        'ethereum-goerli',
        'polygon-mumbai',
        'arbitrum-nova',
        'avalanche-fuji',
        'fantom-testnet',
        'optimism-goerli',
        'bnb-testnet',
        'cronos-testnet'
    ]

    tasks = [request_faucet_tokens(network, wallet_address) for network in networks]
    await asyncio.gather(*tasks)

asyncio.run(main())
