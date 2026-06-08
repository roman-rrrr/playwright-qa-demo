def test_get_started_button(page):
    page.goto("https://playwright.dev")

    button = page.get_by_role(
        "link",
        name="Get started"
    )

    assert button.is_visible()
