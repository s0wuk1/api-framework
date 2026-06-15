import os
import yaml

class CongfigUtil:

    def read_yaml(self):
        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        yaml_path = os.path.join(
            base_dir,
            "conf",
            "config.yaml"
        )
        with open(yaml_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
config_util = CongfigUtil()