import os
from openapi_parser import OpenAPIParser
from description_generator import DescriptionGenerator
from openapi_updater import OpenAPIUpdater


class Main:
    def __init__(self, file_path: str, openai_api_key: str):
        self.file_path = file_path
        self.openapi_parser = OpenAPIParser()
        self.description_generator = DescriptionGenerator(openai_api_key)
        self.openapi_updater = None

    def run(self):
        # Parse the OpenAPI specification sample.yaml
        self.openapi_parser.parse(self.file_path)

        # Extract the resources
        resources = self.openapi_parser.extract_resources()

        # Generate descriptions for the resources
        resources_with_descriptions = {}
        for resource_id, resource in resources.items():
            description = self.description_generator.generate_description(resource)
            if description:
                resource['description'] = description
                resources_with_descriptions[resource_id] = resource

        # Update the OpenAPI specification
        self.openapi_updater = OpenAPIUpdater(self.openapi_parser.openapi_spec)
        self.openapi_updater.update_specification(resources_with_descriptions)

        # Save the updated OpenAPI specification
        updated_file_path = os.path.join(os.path.dirname(self.file_path), f"updated_{os.path.basename(self.file_path)}")
        self.openapi_updater.save_updated_specification(updated_file_path)


if __name__ == "__main__":
    main = Main("Insert-Path-to-YAML-file", "Insert-OpenAI-API-key")
    main.run()
