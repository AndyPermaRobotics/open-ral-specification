# open-ral-specification
This is the formal specification of openRAL, a lightweight and open language for regenerative agriculture. Provided in Markdown and JSON Schemas, it enables AI, software, and machines to exchange structured data and build interoperable, transparent workflows.

## Content
* entities.schema.json: JSON Schema for entities in openRAL
* open_ral.md: Overview about openRAL that puts the JSON Schema into context

## Usage

### Giving an AI context about openRAL

Use `python create_single_document.py` to create a single Markdown document that contains all relevant informations about openRAL.
This can be used to give an AI model the full context about openRAL in one file.