#!"e:\cours\edx cours\finalproject\eduresis\myenv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'icdiff==1.9.1','console_scripts','icdiff'
__requires__ = 'icdiff==1.9.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('icdiff==1.9.1', 'console_scripts', 'icdiff')()
    )
