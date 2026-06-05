def test_open_google(page):
    page.goto("https://google.com")

    assert "Google" in page.title()
