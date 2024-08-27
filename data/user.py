class User:

    _user_pretty_name_to_user_password = {
        "standard user": ["standard_user", "secret_sauce"],
        "locked out user": ["locked_out_user", "secret_sauce"],
    }

    def __init__(self, user_pretty_name):
        try:
            self.name = self._user_pretty_name_to_user_password[
                user_pretty_name][0]
            self.password = self._user_pretty_name_to_user_password[
                user_pretty_name][1]
        except KeyError:
            raise KeyError(
                f'User {user_pretty_name} does not exist.'
            )
