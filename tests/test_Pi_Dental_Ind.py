import json

import pytest
from playwright.sync_api import Playwright

from PageObjects.Login import Login

with open("Data/Credentials.json") as file:
    credentials = json.load(file)
    User_Credentials = credentials["User_Credentials"]

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_self_child(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
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
    CoveragesPage.addChild(child_Bp, child_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()
@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_child_without_self(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password = User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    child_Bp = User_Credentials["childBP"]
    child_Name = User_Credentials["childName"]
    mobile_No = User_Credentials["mobileNo"]
    email_Id = User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email, user_Password)
    CreateNewQuote = login_page.qms_login()
    CoveragesPage = CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.proposerNotAnInsured()
    CoveragesPage.addChild(child_Bp, child_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage = InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_spouse_child_without_self(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password = User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    child_Bp = User_Credentials["childBP"]
    child_Name = User_Credentials["childName"]
    spouse_Bp = User_Credentials["spouseBp"]
    spouse_Name = User_Credentials["spouseName"]
    mobile_No = User_Credentials["mobileNo"]
    email_Id = User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email, user_Password)
    CreateNewQuote = login_page.qms_login()
    CoveragesPage = CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.proposerNotAnInsured()
    CoveragesPage.addSpouse(spouse_Bp, spouse_Name)
    CoveragesPage.addChild(child_Bp, child_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage = InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_spouse_without_self(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password = User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    spouse_Bp = User_Credentials["spouseBp"]
    spouse_Name = User_Credentials["spouseName"]
    mobile_No = User_Credentials["mobileNo"]
    email_Id = User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email, user_Password)
    CreateNewQuote = login_page.qms_login()
    CoveragesPage = CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.proposerNotAnInsured()
    CoveragesPage.addSpouse(spouse_Bp, spouse_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage = InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()
@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_self_Spouse_child(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    spouse_Bp = User_Credentials["spouseBp"]
    spouse_Name = User_Credentials["spouseName"]
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
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.addSpouse(spouse_Bp, spouse_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_self_change_to_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.changeToGold(insured_number [0])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_self_child_change_to_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    child_Bp= User_Credentials["childBP"]
    child_Name= User_Credentials["childName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.changeToGold(insured_number[0])
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.changeToGold(insured_number[1])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_child_without_self_change_to_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password = User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    child_Bp = User_Credentials["childBP"]
    child_Name = User_Credentials["childName"]
    mobile_No = User_Credentials["mobileNo"]
    email_Id = User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email, user_Password)
    CreateNewQuote = login_page.qms_login()
    CoveragesPage = CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.proposerNotAnInsured()
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.changeToGold(insured_number[0])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage = InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_spouse_child_without_self_change_to_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password = User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    child_Bp = User_Credentials["childBP"]
    child_Name = User_Credentials["childName"]
    spouse_Bp = User_Credentials["spouseBp"]
    spouse_Name = User_Credentials["spouseName"]
    mobile_No = User_Credentials["mobileNo"]
    email_Id = User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email, user_Password)
    CreateNewQuote = login_page.qms_login()
    CoveragesPage = CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.proposerNotAnInsured()
    CoveragesPage.addSpouse(spouse_Bp, spouse_Name)
    CoveragesPage.changeToGold(insured_number[0])
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.changeToGold(insured_number[1])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage = InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_spouse_without_self_change_to_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password = User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    spouse_Bp = User_Credentials["spouseBp"]
    spouse_Name = User_Credentials["spouseName"]
    mobile_No = User_Credentials["mobileNo"]
    email_Id = User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email, user_Password)
    CreateNewQuote = login_page.qms_login()
    CoveragesPage = CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.proposerNotAnInsured()
    CoveragesPage.addSpouse(spouse_Bp, spouse_Name)
    CoveragesPage.changeToGold(insured_number[0])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage = InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()
@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_ind_self_Spouse_child_change_to_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    ph_Bp = User_Credentials["phBp"]
    ph_Name = User_Credentials["phName"]
    spouse_Bp = User_Credentials["spouseBp"]
    spouse_Name = User_Credentials["spouseName"]
    child_Bp= User_Credentials["childBP"]
    child_Name= User_Credentials["childName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addph(ph_Bp, ph_Name)
    CoveragesPage.changeToGold(insured_number[0])
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.changeToGold(insured_number[1])
    CoveragesPage.addSpouse(spouse_Bp, spouse_Name)
    CoveragesPage.changeToGold(insured_number[2])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()







