# -*- coding: utf-8 -*-
__version__ = "1.1.2"


import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from .log_record import *
from .withinternallog import *
