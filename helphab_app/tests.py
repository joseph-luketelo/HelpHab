from django.test import TestCase
from .signals import assign_default_packages_to_user


class TestAssignDefaultPackagesToUser(TestCase):

    def test_should_send_signal_when_user_is_created(self):
        self.signal_was_called = False

        def handler(sender, **kwargs):
            self.signal_was_called = True

        assign_default_packages_to_user.connect(handler)

        self.assertTrue(self.signal_was_called)

        assign_default_packages_to_user.disconnect(handler)

