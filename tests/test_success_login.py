def test_success_login(page):
    page.goto("https://practice.expandtesting.com/login")

    page.locator("#username").fill("practice")

    page.locator("#password").fill("SuperSecretPassword!")

    page.get_by_role("button", name="Login").click()

    assert "/secure" in page.url