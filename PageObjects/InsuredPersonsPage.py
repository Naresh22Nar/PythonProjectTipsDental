from PageObjects.ReviewPage import ReviewPage


class InsuredPersonsPage:
    def __init__(self,page):
        self.page = page
    def enterInsuredInfoDetails(self, mobile_No, email_Id):
        self.page.get_by_role("textbox", name="123456789").wait_for()
        self.page.locator(".mat-checkbox-inner-container").nth(2).click()
        self.page.locator(".mat-checkbox-inner-container").nth(3).click()
        self.page.get_by_role("textbox", name="123456789").fill(mobile_No)
        self.page.get_by_role("textbox", name="Enter").fill(email_Id)
    def clickOnGenearteQuote(self):
        self.page.get_by_role("button", name='Generate Quote').click()
        Review_Page= ReviewPage(self.page)
        return Review_Page