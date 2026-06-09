def test_file_upload(page):
	page.goto("https://practice.expandtesting.com/upload")
	
	file_input = page.locator("#fileInput")

	file_input.set_input_files("/Users/roman/Desktop/playwright-qa-demo/tests/test.txt")

	page.get_by_role("button", name = "Upload").click()	
	
	page.wait_for_selector("text=File Uploaded!")
	
	assert "File Uploaded!" in page.content()
