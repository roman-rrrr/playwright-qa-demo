def test_get_started(page):
    page.goto("https://playwright.dev")

    page.get_by_role(
        "link",
        name="Get started"
    ).click()

    print(page.text_content("h1"))