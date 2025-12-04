# open-ral-specification
This is the formal specification of openRAL, a lightweight and open language for regenerative agriculture. Provided in Markdown and JSON Schemas, it enables AI, software, and machines to exchange structured data and build interoperable, transparent workflows.

## Content
* entities.schema.json: JSON Schema for entities in openRAL
* open_ral.md: Overview about openRAL that puts the JSON Schema into context

## Usage

### Giving an AI context about openRAL

Use `python create_single_document.py` to create a single Markdown document that contains all relevant informations about openRAL.
This can be used to give an AI model the full context about openRAL in one file.

e.g. for `copilote-instructions.md` use this text:
```
## OpenRAL

When it comes to interaction with RalObject and RalMethods check [[../open_ral_bundle.md]] to get an understand of how openRAL works and about the schema of RalObjects and RalMethods as well as the interaction with the open-ral.io API.

For accessing the open-ral.io API use the API-KEY: OPEN_RAL_API_KEY
```

## Contributing

### Proposing New RALTypes

If you've developed a custom ralType that could benefit the broader openRAL community, you can propose it for inclusion in the official registry at https://open-ral.io.

**To submit a proposal**:
- Email info@open-ral.io with your ralType specification, documentation, and use cases
- See the "Official vs. Custom RALTypes" section in `open_ral.md` for detailed contribution guidelines
- Include examples of the ralType in use and rationale for standardization

Contributed ralTypes that are accepted will become part of the official standard, enabling cross-organizational interoperability for your use case.