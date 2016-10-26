""" Filename = __init__.py
Copyright (c) 2014-2016 Ehsan Iran-Nejad
Python scripts for Autodesk Revit

This file is part of pyRevit repository at https://github.com/eirannejad/pyRevit

pyRevit is a free set of scripts for Autodesk Revit: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See this link for a copy of the GNU General Public License protecting this package.
https://github.com/eirannejad/pyRevit/blob/master/LICENSE


~~~
Description:
This is pyRevit's main loader script.
Its purpose is to create an instance of pyRevit.session and call its .load() method.
That would in return start parsing the folders for scripts, create a dll for the commands and
lastly create the pyRevit ui in Revit.

The main reason why this loader script has been kept outside the pyRevit library is to demonstrate how a third-party
script can tap into the pyRevit library to read configurations, user settings, access logging system and also
start and interact with a pyRevit.session
"""

import sys

import pyRevit.config as cfg                        # import basic configurations.
from pyRevit.logger import logger                   # import logger to log messages to pyRevit log.
from pyRevit.utils import Timer                     # import Timer from standard utils to log the load  time.

from pyRevit.usersettings import user_settings      # handles user settings

import pyRevit.session as session              # import session to start loading pyRvit.


# initialize timer
t = Timer()

# log python version, home directory, config file and loader script location.
logger.info('Running on: {0}'.format(sys.version))
logger.info('Home Directory is: {0}'.format(cfg.HOME_DIR))
logger.info('Config file is: {}'.format(user_settings.config_file))

# load pyRevit session.
session.load_from(cfg.HOME_DIR)

# log load time
logger.info('Load time: {}'.format(t.get_time_hhmmss()))
