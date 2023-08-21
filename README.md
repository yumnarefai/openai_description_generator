# OpenAPI Description Generator
This tool was created by MetaGPT (Multi-agents system) and is designed to add descriptions for each resource defined in an OpenAPI specification. 

## Docs & Resources
The docs directory contains the following:
1. Product Requirement Design (PRD) created by AI Agent Alice (Product Manager)
2. System Design document created by AI Agent Bob (Architect)
3. API Specification and Tasks Document created by AI Agent Eve (Project Manager)
4. AI Agent Alex (Engineer) has implemented the code for description_generator.py, main.py, openapi_parser.py, openapi_updater.py

The resources directory contains illustrations of the competitive analysis, data API design and sequential flow.

## How to run
1. Ensure you have installed the libraries listed in requirements.txt (optional)
2. Go into the OpenAPI_description_generator1 directory
3. Insert the path to sample.yaml file and the openAI key in line 39 of main.py
4. Run main.py
5. You will obtain a updated-[file_name].yaml containing the resource descriptions.

The updated yaml file with the resource descriptions will be saved in the same directory as that which stores the file with missing resource descriptions.
