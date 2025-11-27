openRAL is an ontology-like knowledge representation that enables farmers, regulatory entities, scientists, but also software, AI, and machines to exchange information as structured data. This allows partners to develop interconnected software and machines easily. In contrast to real ontologies, the data structure is lightweight and purely oriented towards ease-of-use, speed, and low demand on computing power.

At its core, openRAL represents objects and processes in a consistent JSON base structure: RalObjects and RalMethods. This base structure ensures that fundamental properties of objects and methods/processes are represented in a uniform, reusable manner, with free-text descriptions that make the semantics of individual fields understandable for both humans and AI.

For example, it precisely defines how objects relate to each other (`linkedObjectsRef`) or in which state a method currently is (`methodState`).

The formal specification of these language constructs is defined and described in the `open_ral.schema.json` file.

A key concept is the `ralType`, which enables the definition of reusable "classes" or "templates" for the same things and processes across organizations. The `ralType` describes what something is and how it is structured, including which `specificProperties` exist for this particular type of object or method. Using official ralTypes from the open-ral.io registry ensures cross-organizational interoperability and standardized data exchange.

## RalObject Example

Here is an example of a `RalObject` of the `ralType` "field", which represents an agricultural field:
```
{
  "identity": {
    "UID": "f0cb0b64-7682-40a0-bbdc-72c68fdd45dd",
    "alternateIDs": [],
    "alternateNames": [],
    "name": "",
    "siteTag": ""
  },
  "template": {
    "RALType": "field",
    "objectStateTemplates": "generalObjectState",
    "version": "1"
  }
  "definition": {
    "definitionText": "In an agricultural context, a 'field' refers to a specific area of land designated for the cultivation of crops or the grazing of livestock. Fields are typically delineated by natural boundaries like hedgerows, fences, or other markers, and they are managed by farmers to optimize the production of agricultural products. The size, shape, and use of a field can vary widely depending on the type of farming, the landscape, and the agricultural practices employed. Fields are fundamental units in farming operations, and they may be used for growing a single crop (monoculture) or multiple crops (polyculture), or for rotational grazing in the case of livestock farming. Soil preparation, irrigation, planting, and harvesting are all activities that take place within these fields.",
    "definitionURL": " "
  },
  "currentGeolocation": {
    "3WordCode": "unknown",
    "container": {
      "UID": "unknown"
    },
    "geoCoordinates": {
        "latitude": 52.11791236538335,
        "longitude": 9.86210248591761
    },
    "plusCode": "unknown",
    "postalAddress": {
      "cityName": "unknown",
      "cityNumber": "unknown",
      "country": "unknown",
      "streetName": "unknown",
      "streetNumber": "unknown"
    }
  },
  "existenceStarts": "2025-11-26T15:29:13.088Z",
  "linkedObjectsRef": [
    {
      "role": "owner",
      "UID": "08ff32b5-f77b-47d6-9f27-30aed9f12f00"
    }
  ],
  "methodHistoryRef": [],
  "objectState": "undefined",
  "specificProperties": [
    {
      "name": "area",
      "unit": "ha",
      "value": "8.91"
    },
    {
      "name": "boundaries",
      "unit": "vector_list",
      "value": "{\"coordinates\":[[9.86210248591761, 52.11791236538335],[9.86210248591761, 52.11791236538335],[9.86210248591761, 52.11791236538335]]}"
    },
    {
      "name": "soil type",
      "unit": "soil_type",
      "value": ""
    },
    {
      "name": "soil value",
      "unit": "soil_value_germany",
      "value": ""
    }
  ]
}
```

Breaking down the example:

## identity
```json
"identity": {
    "UID": "f0cb0b64-7682-40a0-bbdc-72c68fdd45dd",
    "alternateIDs": [
        {
            "id": "23",
            "issuedBy": "other.system.com"
        }
    ],
    "alternateNames": [],
    "name": "Feld 23",
    "siteTag": ""
},
```
The identity section contains all identifiers and names for the object:
- `UID`: A unique identifier (UUIDv4) that globally identifies this specific object. 
- `alternateIDs`: An array of alternative ids issued by other systems. Each alternate ID contains:
  - `id`: The alternative identifier string
  - `issuedBy`: The system or authority that issued this alternate ID
- `alternateNames`: An array of alternative names used for this object
- `name`: The primary human-readable name of the object. This is not unique and can be changed.
- `siteTag`: A location-specific tag or identifier used on-site

## template
```json
"template": {
    "RALType": "field",
    "objectStateTemplates": "generalObjectState",
    "version": "1"
}
```
The template section defines the type and structure of the object:
- `RALType`: Defines the type of the object (in this case "field"). It should be selected from the official RALTypes available at https://open-ral.io/ to ensure interoperability across systems and organizations. Use the semantic search API endpoint (`/semantic_search`) to discover appropriate official templates by describing your concept in natural language. For guidance on custom ralTypes when no official template matches your needs, see the "Official vs. Custom RALTypes" section below.
- `objectStateTemplates`: Specifies which values the objectState field can have. In this case, it uses the "generalObjectState" template that defines common states for general objects. TODO: link to state template definitions
- `version`: The version number of the RALType specification being used

## definition
```json
"definition": {
    "definitionText": "In an agricultural context, a 'field' refers to a specific area of land designated for the cultivation of crops or the grazing of livestock. Fields are typically delineated by natural boundaries like hedgerows, fences, or other markers, and they are managed by farmers to optimize the production of agricultural products. The size, shape, and use of a field can vary widely depending on the type of farming, the landscape, and the agricultural practices employed. Fields are fundamental units in farming operations, and they may be used for growing a single crop (monoculture) or multiple crops (polyculture), or for rotational grazing in the case of livestock farming. Soil preparation, irrigation, planting, and harvesting are all activities that take place within these fields.",
    "definitionURL": " "
}
```
The definition section provides semantic information about what this RALType of object represents:
- `definitionText`: A comprehensive free-text description of what this object type means and how it is used in its domain context
- `definitionURL`: A URL reference to external documentation or standards that further define this object type

## currentGeolocation
```json
"currentGeolocation": {
    "3WordCode": "unknown",
    "container": {
      "UID": "a3ba0729-80ef-4a8e-b1f6-8a88e56dd44d"
    },
    "geoCoordinates": {
        "latitude": 52.11791236538335,
        "longitude": 9.86210248591761
    },
    "plusCode": "unknown",
    "postalAddress": {
      "cityName": "unknown",
      "cityNumber": "unknown",
      "country": "unknown",
      "streetName": "unknown",
      "streetNumber": "unknown"
    }
  }
```
The currentGeolocation section describes the physical location of the object:
- `geoCoordinates`: Geographic coordinates in WGS84 format (latitude and longitude)
- `container`: References another RalObject that contains this object (e.g., a farm that contains this field)
- `postalAddress`: The postal address with street, city, and country information
- `3WordCode`: A what3words address for precise location identification
- `plusCode`: A Google Plus Code for location identification

## existenceStarts
```json
"existenceStarts": "2025-11-26T15:29:13.088Z"
```
The existenceStarts field contains an ISO 8601 timestamp (UTC) indicating when this object was created or when it started to exist in the system.

## linkedObjectsRef
```json
"linkedObjectsRef": [
    {
      "role": "owner",
      "UID": "08ff32b5-f77b-47d6-9f27-30aed9f12f00"
    }
]
```
The linkedObjectsRef section contains references to other RalObjects that are logically related to this object:
- An array of object references, each with a `role`, `UID`, and optional `domain` field
- Each reference describes the relationship through its `role` field (e.g., "owner", "operator", "assigned_equipment", "related_crop")
- The role `"owner"` is reserved for ownership relationships and should be used to reference RalObjects (typically of type "person" or "organization") that own this object
- This enables creating a network of interconnected objects with clearly defined relationships

## methodHistoryRef
```json
"methodHistoryRef": []
```
The methodHistoryRef section contains references to all RalMethods (processes/actions) that have been performed on this object:
- This creates a complete history of all operations and processes applied to this object (e.g., planting, harvesting, fertilizing)

## objectState
```json
"objectState": "undefined"
```
The objectState field indicates the current state of the object:
- The possible states are defined by the `objectStateTemplates` specified in the template section
- Common states might include: "active", "inactive", "archived", "undefined", etc.
- The specific states depend on the RALType and its state template

## specificProperties
```json
"specificProperties": [
    {
      "name": "area",
      "unit": "ha",
      "value": "8.91"
    },
    {
      "name": "boundaries",
      "unit": "vector_list",
      "value": "{\"coordinates\":[[9.86210248591761, 52.11791236538335],[9.86210248591761, 52.11791236538335],[9.86210248591761, 52.11791236538335]]}"
    },
    {
      "name": "soil type",
      "unit": "soil_type",
      "value": ""
    },
    {
      "name": "soil value",
      "unit": "soil_value_germany",
      "value": ""
    }
]
```
The specificProperties section contains RALType-specific properties:
- An array of property objects, each with a name, unit, and value
- The properties are defined by the RALType specification, you can add your own, but they will not be compatible with other systems that use the same RALType.
- For a "field" object, this includes:
  - `area`: The size of the field in hectares
  - `boundaries`: A vector list defining the field's boundaries as a polygon
  - `soil type`: Classification of the soil type
  - `soil value`: A soil quality rating (using the German soil value system in this example)
- These properties allow each RALType to have domain-specific attributes while maintaining a consistent overall structure

## Official vs. Custom RALTypes

### Official RALTypes

Official ralTypes are registered and maintained in the open-ral.io registry. Using official ralTypes provides several critical benefits:

- **Interoperability**: Data can be seamlessly exchanged between different organizations, systems, and software tools without custom integration work
- **Standardization**: Common understanding of what a ralType represents and which properties it contains
- **Semantic Clarity**: Well-documented definitions that AI systems and humans can rely on
- **Version Management**: Controlled evolution of templates with proper versioning
- **Community Support**: Shared maintenance and improvement by the openRAL community

**Finding Official RALTypes**: Use the semantic search API to discover appropriate official templates:

```bash
POST https://europe-west3-ral1-80620.cloudfunctions.net/semantic_search?query=your+concept+description
Headers:
  X-API-KEY: your-api-key
```

The API returns matching templates with relevance scores, allowing you to find the best fit for your use case even if you don't know the exact ralType name.

### Custom RALTypes

While official ralTypes should be used whenever possible, there are legitimate cases where custom ralTypes are necessary:

- The concept you need to represent doesn't exist in the official registry yet
- Your organization has highly specialized domain-specific objects or methods
- You're prototyping new concepts before proposing them for standardization

**Important Trade-offs**: Custom ralTypes come with significant limitations:

- ❌ **No Interoperability**: Other organizations cannot automatically interpret your custom ralType without additional documentation and integration work
- ❌ **Limited AI Understanding**: AI systems trained on openRAL won't understand your custom properties and semantics
- ❌ **Maintenance Burden**: You're responsible for documenting, versioning, and maintaining the custom ralType
- ⚠️ **Name Conflicts**: Risk of conflicts if the official registry later introduces a ralType with the same name

### Custom RALType Naming Convention

To avoid conflicts and enable future integration, custom ralTypes MUST follow reverse-domain notation:

```
com.organization.domain.typeName
```

**Examples**:
- `com.acmefarms.equipment.autonomousTractor`
- `org.researchlab.sensors.hyperspectralCamera`
- `de.bioland.certification.organicField`

**Naming Rules**:
1. Start with your organization's reverse domain (e.g., `com.yourcompany`)
2. Optionally add subdomain/category (e.g., `.equipment`, `.methods`)
3. End with a descriptive camelCase type name
4. Use only alphanumeric characters, dots, and camelCase (no spaces, underscores, or special characters)
5. Keep names concise but descriptive

### Documentation Requirements for Custom RALTypes

If you create custom ralTypes, you MUST maintain comprehensive documentation:

1. **Definition**: Detailed `definitionText` explaining what the ralType represents
2. **Specific Properties**: Complete specification of all `specificProperties` including:
   - Property name and description
   - Data type and unit
   - Valid value ranges or constraints
   - Required vs. optional properties
3. **Version History**: Track changes to your custom ralType structure
4. **Use Cases**: Examples of when and how the ralType should be used
5. **Related Types**: Document relationships to official or other custom ralTypes

### Contributing Custom RALTypes to the Official Registry

If you've created a custom ralType that could benefit the broader openRAL community, consider proposing it for inclusion in the official registry:

**Contribution Process**:
1. **Validate Need**: Ensure no existing official ralType covers your use case (use semantic search)
2. **Document Thoroughly**: Prepare complete documentation as outlined above
3. **Gather Support**: If possible, show adoption by multiple organizations or use cases
4. **Submit Proposal**: Contact the openRAL maintainers via info@open-ral.io with:
   - Your custom ralType specification
   - Use case descriptions
   - Example instances
   - Rationale for standardization
5. **Community Review**: The proposal will be reviewed by the openRAL community for clarity, necessity, and potential conflicts
6. **Standardization**: If accepted, your custom ralType will be integrated into the official registry with proper attribution

**Migration Path**: When a custom ralType becomes official:
- The official ralType may receive a simplified name (e.g., `com.acmefarms.equipment.autonomousTractor` → `autonomousTractor`)
- You should migrate your instances to use the official ralType
- The custom ralType should be marked as deprecated in your documentation
- A transition period allows gradual migration across your systems

**Best Practice**: Even when using custom ralTypes, design them as if they might become official standards - use clear naming, comprehensive documentation, and follow the same structural patterns as official ralTypes.


