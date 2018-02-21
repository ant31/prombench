import yaml
from prombench.config import GCONFIG


print(yaml.safe_dump(GCONFIG.settings, indent=2))
