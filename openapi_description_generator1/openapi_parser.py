import yaml
from typing import Dict, List


class OpenAPIParser:
    def __init__(self):
        self.openapi_spec: Dict = {}

    def parse(self, file_path: str) -> None:
        """
        Parse the OpenAPI specification from the provided file path.
        """
        with open(file_path, 'r') as file:
            self.openapi_spec = yaml.safe_load(file)

    def extract_resources(self) -> Dict[str, Dict]:
        """
        Extract the resources from the OpenAPI specification.
        """
        resources: Dict[str, Dict] = {}

        for path, path_item in self.openapi_spec.get('paths', {}).items():
            for method, operation in path_item.items():
                if method in ['get', 'post', 'put', 'delete', 'options', 'head', 'patch', 'trace']:
                    resource_id = f"{path}_{method}"
                    resources[resource_id] = {
                        'path': path,
                        'method': method,
                        'summary': operation.get('summary', ''),
                        'description': operation.get('description', '')
                    }

        return resources
