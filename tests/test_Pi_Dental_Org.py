import json

import pytest
from playwright.sync_api import Playwright

from PageObjects.Login import Login

with open("Data/Credentials.json") as file:
    credentials = json.load(file)
    User_Credentials = credentials["User_Credentials"]

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_Employees_child(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    child_Bp= User_Credentials["childBP"]
    child_Name= User_Credentials["childName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.addChild(child_Bp, child_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_child_Spouse(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    spouse_Bp= User_Credentials["spouseBp"]
    spouse_Name= User_Credentials["spouseName"]
    child_Bp= User_Credentials["childBP"]
    child_Name= User_Credentials["childName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.addSpouse(spouse_Bp,spouse_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_Employees_Spouse(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    spouse_Bp= User_Credentials["spouseBp"]
    spouse_Name= User_Credentials["spouseName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.addSpouse(spouse_Bp,spouse_Name)
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_Change_To_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.changeToGold(insured_number[0])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()




@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_Change_To_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.changeToGold(insured_number[0])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_Employees_child_Change_To_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
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
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
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
def test_dental_Org_Employee_Epmloyees_child_Spouse_Change_To_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    spouse_Bp= User_Credentials["spouseBp"]
    spouse_Name= User_Credentials["spouseName"]
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
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.changeToGold(insured_number[0])
    CoveragesPage.addChild(child_Bp, child_Name)
    CoveragesPage.changeToGold(insured_number[1])
    CoveragesPage.addSpouse(spouse_Bp,spouse_Name)
    CoveragesPage.changeToGold(insured_number[2])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_Employees_Spouse_Change_To_Gold(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    spouse_Bp= User_Credentials["spouseBp"]
    spouse_Name= User_Credentials["spouseName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    insured_number = [0, 1, 2, 3]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    CoveragesPage.changeToGold(insured_number[0])
    CoveragesPage.addSpouse(spouse_Bp,spouse_Name)
    CoveragesPage.changeToGold(insured_number[1])
    InsuredPersonsPage = CoveragesPage.clickOnProceedQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()

@pytest.mark.parametrize('User_Credentials', User_Credentials)
def test_dental_Org_Employee_SaveQuote(playwright: Playwright,User_Credentials, browser_Instance):
    User_Email = User_Credentials["userEmail"]
    user_Password= User_Credentials["userPassword"]
    org_Ph_Name= User_Credentials["orgPhName"]
    org_Ph_Bp=User_Credentials["orgPhBp"]
    employee_Bp = User_Credentials["phBp"]
    employee_Name = User_Credentials["phName"]
    mobile_No= User_Credentials["mobileNo"]
    email_Id= User_Credentials["emailId"]
    login_page = Login(browser_Instance)
    login_page.navigate_to_login_page()
    login_page.user_login(User_Email,user_Password )
    CreateNewQuote = login_page.qms_login()
    CoveragesPage= CreateNewQuote.create_dental_quote()
    CoveragesPage.addOrgPh(org_Ph_Bp, org_Ph_Name)
    CoveragesPage.addEmployee(employee_Bp, employee_Name)
    InsuredPersonsPage = CoveragesPage.clickOnSaveQuote()
    InsuredPersonsPage.enterInsuredInfoDetails(mobile_No, email_Id)
    ReviewPage= InsuredPersonsPage.clickOnGenearteQuote()
    ReviewPage.downloadQuote()
    ReviewPage.issuePolicy()
    ReviewPage.getPolicyNo()






