"""Provides a generic base object for other db model objects to inherit
from as well as a mixin objects that might apply to the model object.
"""

import sqlalchemy.orm


Object = sqlalchemy.orm.declarative_base()
