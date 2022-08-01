import databases

# from ..settings import DATABASE_URL
# from . import queries
# from . import models
from settings import DATABASE_URL
from db import queries
from db import models


database = databases.Database(DATABASE_URL)