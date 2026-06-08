def test_get_started(page):
    page.goto("https://playwright.dev")

    page.get_by_role(
        "link",
        name="Get started"
    ).click()

    assert page.url == "https://playwright.dev/docs/intro"
