import os

SCREENSHOTS_PATH = os.path.join(".", "reports", "playwright")

class PlaywrightReports:

    def __init__(self, page):
        self.page = page

    def take_full_page_screenshot(self, request):
        test_name = request.node.nodeid.split("::test_")[-1].split(".py")[0]
        self.page.screenshot(path=os.path.join(SCREENSHOTS_PATH, f"{test_name}.png"))