import pytest
from playwright.sync_api import sync_playwright

# Fixture untuk Playwright
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_login_checkout(page):
    # Navigasi ke Halaman Login
    page.goto("https://www.saucedemo.com/")

    # Verifikasi bahwa teks pada elemen logo adalah "Swag Labs"
    assert page.locator('//div[@class="login_logo"]').text_content() == "Swag Labs"

    # Menginputkan kolom username dan password Login
    page.locator('//input[@id="user-name"]').fill('standard_user')
    page.locator('//input[@id="password"]').fill('secret_sauce')

    # Klik tombol login
    page.locator('[id="login-button"]').click()

    # Verifikasi bahwa teks pada halaman produk adalah "Products"
    assert page.locator('//span[@class="title"]').text_content() == "Products"

    # Klik tombol Add to cart
    page.locator('//button[@id="add-to-cart-sauce-labs-backpack"]').click()

    # Klik tombol Keranjang
    page.locator('//a[.="1"]').click()

    # Klik tombol Checkout
    page.locator('//button[@id="checkout"]').click()

    # Menginputkan Form Your Information
    page.locator('//input[@id="first-name"]').fill('Test123')
    page.locator('//input[@id="last-name"]').fill('secret_sauce')
    page.locator('//input[@id="postal-code"]').fill('16541')

    # Verifikasi Elemen Aktif Button Continue (Enabled)
    assert page.is_enabled('//input[@id="continue"]')

    # Klik tombol Continue
    page.locator('//input[@id="continue"]').click()

    # Verifikasi bahwa teks pada halaman Overview adalah "Checkout: Overview"
    assert page.locator('//span[@class="title"]').text_content() == "Checkout: Overview"

    # Verifikasi Elemen Aktif Button Finish (Enabled)
    assert page.is_enabled('//button[@id="finish"]')

    # Klik tombol Finish
    page.locator('//button[@id="finish"]').click()

    # Verifikasi bahwa telah berhasil Order
    assert page.locator('//h2[@class="complete-header"]').text_content() == "Thank you for your order!"