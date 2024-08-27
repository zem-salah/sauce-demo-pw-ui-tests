from data.user import User


def test_standard_login_should_redirect_to_inventory(login_actions):
    login_actions.login_form.navigate()
    login_actions.login_as(User('standard user'))
    login_actions.login_form.page.wait_for_url('**/inventory.html')


def test_locked_in_user_should_not_be_able_to_login(login_actions):
    pass


def test_username_is_required(login_actions):
    pass


def test_password_is_required(login_actions):
    pass


def test_unrecognized_user_should_not_be_able_to_login(login_actions):
    pass
