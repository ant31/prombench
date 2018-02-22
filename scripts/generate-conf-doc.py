import yaml
from promsnaps.config import GCONFIG


print(yaml.safe_dump(GCONFIG.settings, indent=2))
