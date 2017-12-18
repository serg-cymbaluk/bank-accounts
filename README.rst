Bank Accounts
=============

Project description
-------------------

This test application allows "staff" users to manage other user accounts.

Any Google user can sign in to the system and ask an administrator to provide him "staff" permissions.
After the permission is provided in admin panel user can access his functions.

Accounts created by staff are not fully functional.
They have random generated username, no password and no permissions.

How to Setup
------------

1. Install *Docker* and *Docker Compose*.

2. Run command *docker-compose up* inside project folder.

3. Create superuser:

  .. code-block:: bash

    docker-compose exec web django-admin createsuperuser

4. Open address http://localhost:8000
