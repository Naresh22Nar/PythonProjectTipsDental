from playwright.sync_api import expect


class ReviewPage:
    def __init__(self,page):
        self.page = page
    def downloadQuote(self):
        self.page.get_by_role("button", name='Download Quote & PDS Documents').wait_for()
        self.page.get_by_role("button", name='Download Quote & PDS Documents').click()
        self.page.locator('.mat-checkbox-inner-container').nth(0).click()
        self.page.get_by_role("button", name='Send').click()
        self.page.wait_for_timeout(2000)
        self.page.locator("span").filter(has_text='close').click()
    def issuePolicy(self):
        self.page.get_by_role("button", name="Issue Policy").click()
        self.page.get_by_text("Accept & Proceed").click()
    def getPolicyNo(self):
        self.page.get_by_text("Issued").wait_for()
        expect(self.page.get_by_text("Issued")).to_have_text("Issued")
        self.page.locator("div[class='summary-result'] span[class='ng-star-inserted']").wait_for()

        policyNo = self.page.locator("div[class='summary-result'] span[class='ng-star-inserted']").text_content()
        print(policyNo)