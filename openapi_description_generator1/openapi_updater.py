import yaml
from typing import Dict


class OpenAPIUpdater:
    def __init__(self, openapi_spec: Dict):
        self.openapi_spec = openapi_spec

    def update_specification(self, resources_with_descriptions: Dict[str, Dict]) -> None:
        """
        Update the OpenAPI specification with the generated descriptions.
        """
        for resource_id, resource in resources_with_descriptions.items():
            path, method = resource_id.split('_')
            operation = self.openapi_spec['paths'][path][method]

            if 'description' in resource:
                operation['description'] = resource['description']

    def save_updated_specification(self, file_path: str) -> None:
        """
        Save the updated OpenAPI specification to the provided file path.
        """
        with open(file_path, 'w') as file:
            yaml.safe_dump(self.openapi_spec, file)
