class SGRouter(object):
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.app_label == 'stackGuruApi':
            return 'sg_db_main'
        return None

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.app_label == 'stackGuruApi':
            return 'sg_db_main'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models that are both in the Example app.
        if obj1._meta.app_label == 'stackGuruApi' and obj2._meta.app_label == 'stackGuruApi':
            return True
        # No opinion if neither object is in the Example app (defer to default or other routers).
        elif 'stackGuruApi' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

        # Block relationship if one object is in the Example app and the other isn't.
            return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'stackGuruApi':
            # The Example app should be migrated only on the example_db database.
            return db == 'sg_db_main'
        elif db == 'sg_db_main':
            # Ensure that all other apps don't get migrated on the example_db database.
            return False
        elif app_label == 'admin' or app_label == 'auth' or app_label=='contenttypes' or app_label=='sessions':
            # Specific for local default migrations
            return db == 'default'

        # No opinion for all other scenarios
        return None

