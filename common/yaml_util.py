import os
import yaml
class YamlUtil:
    @staticmethod
    def read_yaml(file_path):

        base_dir = os.path.dirname(
            os.path.dirname(__file__)
        )

        full_path = os.path.join(
            base_dir,
            file_path
        )

        with open(
                full_path,
                encoding="utf-8"
        ) as f:
            return yaml.safe_load(f)


yaml_util = YamlUtil()