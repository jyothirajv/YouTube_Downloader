#!"C:\Users\R4V3N\PycharmProjects\YouTube Downloader\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'quote==2.0.1','console_scripts','quote'
__requires__ = 'quote==2.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('quote==2.0.1', 'console_scripts', 'quote')()
    )
