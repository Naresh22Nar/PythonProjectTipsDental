from PageObjects.CreateNewQuote import CreateNewQuote


class Login:
    def __init__(self,page):
        self.page = page
    def navigate_to_login_page(self):
        self.page.goto(
            "https://auth.sit.indigit.io/realms/Tune/protocol/openid-connect/auth?response_type=code&client_id=1003&state=Y1VXdnA0Tjk5OXJkQkRlLnFjT0RzbGVZWEdWSlN5d1NYLXdaM1RuR3I3Q0NE&redirect_uri=https%3A%2F%2Ftune.sit.indigit.io%2F&scope=openid%20profile&code_challenge=DauHhvQCkg7VkQuC6FE1Ki7YNv7ESrdMmNBzoGpL_a8&code_challenge_method=S256&nonce=Y1VXdnA0Tjk5OXJkQkRlLnFjT0RzbGVZWEdWSlN5d1NYLXdaM1RuR3I3Q0NE")
    def user_login(self, User_Email,user_Password):
        self.page.get_by_label("username").fill(User_Email)
        self.page.get_by_label("password").fill(user_Password)
        self.page.get_by_role("button", name="login").click()
    def qms_login(self):
        self.page.locator("p").filter(has_text="Quotation Management System").click()
        Create_New_Quote = CreateNewQuote(self.page)
        return Create_New_Quote


