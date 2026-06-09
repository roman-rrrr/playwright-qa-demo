def test_invalid_username(page):
    page.goto("https://practice.expandtesting.com/login")

    page.locator("#username").fill("wrong_username")

    page.locator("#password").fill("SuperSecretPassword!")

    page.get_by_role("button", name="Login").click()

    assert "/login" in page.url

    assert "Your username is invalid!" in (
        page.locator("#flash").text_content()
    )