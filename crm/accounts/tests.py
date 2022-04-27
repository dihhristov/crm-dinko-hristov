from django.test import TestCase

from crm.accounts.models import Profile, CrmUser


class ProfileTest(TestCase):
    profile_valid_data = {
        'first_name': 'Dinko',
        'last_name': 'Hristov',
        'email': 'dinko@hristov.it',
        'position': 'Account Manager',
        'user': CrmUser(),

    }

    def test_profile_create__when_first_name_contains_only_letters_expect_success(self):
        profile = Profile('Dinko', 'Hristov', 'dinko@hristov.it', 'Account Manager', CrmUser() )

        profile.save()

    def test__profile_create__when_first_name_contains_a_digit_expect_fail(self):
        pass

    def test_profile_create__when_first_name_contains_space_expect_success(self):
        pass
