def test_find_element(page):
    page.goto("https://playwright.dev")

    get_started = page.locator("text=Get started")

    assert get_started.is_visible()
