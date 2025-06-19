import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://faucet.haust.app/"
TESTNET_ADDRESS = "your_haust_testnet_address_here"  # Replace with your actual testnet wallet address

async def claim_haust_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless=True to run without UI
        page = await browser.new_page()

        await page.goto(FAUCET_URL)

        # Wait for the address input field to appear
        await page.wait_for_selector('input[type="text"], input[placeholder*="address"]')

        # Fill in the testnet address
        await page.fill('input[type="text"], input[placeholder*="address"]', TESTNET_ADDRESS)

        # Click the claim/request button
        # Adjust selector if needed after inspecting the page
        await page.click('button:has-text("Claim")')

        # Wait for success message or timeout after 10 seconds
        try:
            await page.wait_for_selector('text=success', timeout=10000)
            print("Faucet claim successful!")
        except Exception:
            print("No success confirmation detected. Please check manually.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_haust_faucet())
