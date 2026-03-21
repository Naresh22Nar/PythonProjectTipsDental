from PageObjects.InsuredPersonsPage import InsuredPersonsPage


class CoveragesPage:
    def __init__(self,page):
        self.page = page
    def addph(self, ph_Bp, ph_Name):
        self.page.locator("//input[@id='dx-input-0']").fill(ph_Bp)
        self.page.locator("//input[@id='dx-input-1']").fill(ph_Name)
    def addOrgPh(self, org_Ph_Bp, org_Ph_Name):
        self.page.wait_for_timeout(2000)
        self.page.get_by_text('Organisation').click()
        self.page.wait_for_timeout(2000)
        self.page.locator("//input[@id='dx-input-1']").fill(org_Ph_Name)
        self.page.locator("//input[@id='dx-input-0']").fill(org_Ph_Bp)
        self.page.locator("//input[@id='dx-input-0']").press("Tab")




    def proposerNotAnInsured(self):
        self.page.locator(".mat-checkbox-layout").nth(0).click()
    def addEmployee(self, employee_Bp, employee_Name):
        self.page.get_by_text("Add Insured Person").click()
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            employee_Name)
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            employee_Bp)
        self.page.get_by_text("Save", exact=True).click()
    def changeToGold(self,insured_number):
        self.page.wait_for_timeout(2000)
        self.page.locator('span', has_text= 'more_vert' ).nth(insured_number).click()
        self.page.get_by_text('Edit', exact= True).click()
        self.page.get_by_text("PlatinumPlan *").click()
        self.page.locator('span.mat-option-text').nth(0).click()
        self.page.get_by_role("button", name="Update").click()
    def addChild(self, child_Bp, child_Name):
        self.page.get_by_text("Add Insured Person").click()
        self.page.get_by_text('close', exact= True).click()
        self.page.get_by_text("Add Insured Person").click()
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            child_Name)
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            child_Bp)
        self.page.get_by_role('combobox', name='Relationship with Proposer').click()
        self.page.get_by_text("Child").click()
        self.page.get_by_text("Save", exact=True).click()

    def addSpouse(self, spouse_Bp, spouse_Name):
        self.page.get_by_text("Add Insured Person").click()
        self.page.get_by_text('close', exact=True).click()
        self.page.get_by_text("Add Insured Person").click()
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            spouse_Bp)
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            spouse_Name)

        self.page.get_by_role('combobox', name='Relationship with Proposer').click()
        self.page.get_by_text("Spouse").click()
        self.page.get_by_text("Save", exact=True).click()
    def addChild_Gold(self, child_Bp, child_Name):
        self.page.get_by_text("Add Insured Person").click()
        self.page.get_by_text('close', exact= True).click()
        self.page.get_by_text("Add Insured Person").click()
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            child_Name)
        self.page.locator(
            "body > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > mat-dialog-container:nth-child(2) > app-additional-insured-popup:nth-child(1) > mat-dialog-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > dx-input:nth-child(1) > div:nth-child(1) > mat-form-field:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > input:nth-child(1)").fill(
            child_Bp)
        self.page.get_by_role('combobox', name='Relationship with Proposer').click()
        self.page.get_by_text("Child").click()
        self.page.get_by_text("PlatinumPlan *").click()
        self.page.locator('span.mat-option-text').nth(0).click()
        self.page.get_by_text("Save", exact=True).click()

    def clickOnProceedQuote(self):
        self.page.locator(".mat-checkbox-layout").nth(1).click()
        self.page.get_by_role("button", name='Proceed Quote').click()
        Insured_Persons_Page = InsuredPersonsPage(self.page)
        return Insured_Persons_Page
    def clickOnSaveQuote(self):
        self.page.get_by_text('Save Quote').click()
        self.page.locator(".mat-checkbox-layout").nth(1).click()
        self.page.get_by_role("button", name='Proceed Quote').click()
        Insured_Persons_Page = InsuredPersonsPage(self.page)
        return Insured_Persons_Page