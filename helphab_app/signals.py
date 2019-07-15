from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from .models import Package, UserPackageChoice


@receiver(post_save, sender=User, dispatch_uid="assign_default_packages_to_user")
def assign_default_packages_to_user(**kwargs):
    """Initializes a package for a new user with the default choices."""
    # nothing to do for existing users
    if kwargs["created"] is False:
        return

    user = kwargs["instance"]
    user_package_choice, _ = UserPackageChoice.objects.get_or_create(user=user)
    user_package_choice.available_packages.add(
        # we have to add individual objects to the M2M.add, so we create a list
        # from the QuerySet and unpack the list
        *list(Package.objects.filter(default=True))
    )


charge_completed = Signal(providing_args=["price"])
