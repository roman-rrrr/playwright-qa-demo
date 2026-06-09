def test_success_login(page):
    page.goto("https://practice.expandtesting.com/login")

    page.locator("#username").fill("practice")
    page.locator("#password").fill("SuperSecretPassword!")

    page.get_by_role("button", name="Login").click()

    assert "/secure" in page.url

    assert "You logged into a secure area!" in (
        page.locator("#flash").text_content()
    )

    assert page.get_by_role(
        "link",
        name="Logout"
    ).is_visible()