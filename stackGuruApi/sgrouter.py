class SGDatabaseRouter:
    """
    A router to control all database operations on models in the
    stackGuru application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read stack guru api models go to sg database.
        """
        if model._meta.app_label == 'stackGuruApi':
            return 'sg_db_main'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write Stack Guru Api go to Stack Guru Api database.
        """
        if model._meta.app_label == 'stackGuruApi':
            return 'sg_db_main'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the Stack Guru Api app is involved.
        """
        if obj1._meta.app_label == 'stackGuruApi' or \
           obj2._meta.app_label == 'stackGuruApi':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the discourse app only appears in the 'discourse'
        database.
        """
        if app_label == 'stackGuruApi':
            return db == 'sg_db_main'
        return None
