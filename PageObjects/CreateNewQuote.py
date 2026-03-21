from PageObjects.CoveragesPage import CoveragesPage


class CreateNewQuote:
    def __init__(self,page):
        self.page = page

    def create_dental_quote(self):
        self.page.get_by_role("button", name='New Quote').click()
        self.page.get_by_text("Accident & Health").click()
        self.page.get_by_text('Dental Shield').nth(0).click()
        self.page.get_by_role("button", name="Next").click()
        Coverages_Page = CoveragesPage(self.page)
        return Coverages_Page