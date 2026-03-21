import json

import pytest
from playwright.sync_api import Playwright

from PageObjects.Login import Login

with open("Data/Credentials.json") as file:
    credentials = json.load(file)
    User_Credentials = credentials["User_Credentials"]

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_self_gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    insured_number = [0, 1, 2, 3]
    child_Bp= User_Credentials["childBP"]
    child_Name= User_Credentials["childName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.changeToGold(insured_number[0])
    CoveragesPage.addChild_Gold(child_Bp, child_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()
