openRAL is an ontology-like knowledge representation that enables farmers, regulatory entities, scientists, but also software, AI, and machines to exchange information as structured data. This allows partners to develop interconnected software and machines easily. In contrast to real ontologies, the data structure is lightweight and purely oriented towards ease-of-use, speed, and low demand on computing power.

At its core, openRAL represents objects and processes in a consistent JSON base structure: RalObjects and RalMethods. This base structure ensures that fundamental properties of objects and methods/processes are represented in a uniform, reusable manner, with free-text descriptions that make the semantics of individual fields understandable for both humans and AI.

For example, it precisely defines how objects relate to each other (`linkedObjectsRef`) or in which state a method currently is (`methodState`).

The formal specification of these language constructs is defined and described in the `open_ral.schema.json` file.

A key concept is the `ralType`, which enables the definition of reusable "classes" or "templates" for the same things and processes across organizations. The `ralType` describes what something is and how it is structured, including which `specificProperties` exist for this particular type of object or method. Using official ralTypes from the open-ral.io registry ensures cross-organizational interoperability and standardized data exchange.

**⚠️ IMPORTANT**: Before creating a RalObject or RalMethod, you should use an official RALType from open-ral.io. If you don't know which RALType fits your use case, use the semantic search API to find the appropriate template. See the "Finding the Right RALType" section below.

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

### Finding the Right RALType

**When to use the semantic search API:**
- You need to represent a concept but don't know if a suitable RALType exists
- You're unsure which of multiple possible RALTypes best fits your use case
- You want to discover what official templates are available for your domain

**Workflow for finding RALTypes:**

1. **Describe your concept**: Think about what you want to represent in natural language
2. **Query the API**: Send your description to the semantic search endpoint
3. **Review results**: The API returns matching templates ranked by relevance score
4. **Evaluate matches**: Check the definition texts and relevance scores (>400 typically indicates a good match)
5. **Select the best fit**: Use the `name` field from your chosen result as the `RALType` in your RalObject or RalMethod

**API Endpoint:**
```
POST https://europe-west3-ral1-80620.cloudfunctions.net/semantic_search?query=<your-description>
Header: X-API-KEY: <your-api-key>
```

**Response format:** Array of templates with `name`, `templateType`, `relevance`, and `definitionText` fields

**If you already know the RALType name**: You can skip the semantic search and directly use the known RALType in your template.

**If no suitable match exists** (relevance <300 or no results): Consider creating a custom RALType following the guidelines in the "Custom RALTypes" section below.

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


## RalMethod Example

Here is an example of a `RalMethod` of the `ralType` "changeContainer", which represents a method to change the container of an object:

```
{
  "specificProperties": [],
  "inputObjectsRef": [],
  "outputObjectsRef": [],
  "nestedMethods": [],
  "definition": {
    "definitionText": "A Method to change the container of an object",
    "definitionURL": ""
  },
  "existenceStarts": "2025-02-23T17:40:22",
  "executor": {
    "currentOwners": [],
    "locationHistoryRef": [],
    "ownerHistoryRef": [],
    "linkedObjectRef": [],
    "identity": {
      "alternateIDs": [],
      "alternateNames": [],
      "UID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
      "name": "",
      "siteTag": ""
    },
    "definition": {
      "definitionText": "A human being.",
      "definitionURL": ""
    },
    "objectState": "undefined",
    "template": {
      "RALType": "human",
      "version": "1",
      "objectStateTemplates": "generalObjectState"
    },
    "specificProperties": [
      {
        "key": "emailAddress",
        "value": "",
        "unit": "emailAddress"
      },
      {
        "key": "streetName",
        "value": "",
        "unit": "String"
      },
      {
        "key": "streetNumber",
        "value": "",
        "unit": "String"
      },
      {
        "key": "cityName",
        "value": "",
        "unit": "String"
      },
      {
        "key": "cityNumber",
        "value": "",
        "unit": "String"
      },
      {
        "key": "email",
        "value": "igeler7@gmail.com",
        "unit": "String"
      }
    ],
    "currentGeolocation": {
      "container": {
        "UID": "unknown"
      },
      "postalAddress": {
        "country": "unknown",
        "cityName": "unknown",
        "cityNumber": "unknown",
        "streetName": "unknown",
        "streetNumber": "unknown"
      },
      "3WordCode": "unknown",
      "geoCoordinates": {
        "longitude": 0,
        "latitude": 0
      },
      "plusCode": "unknown"
    },
    "methodHistoryRef": [
      {
        "UID": "fc7fc19b-4040-40d2-a81b-c956a1b41ace",
        "RALType": "generateDigitalSibling"
      },
      {
        "UID": "c818422b-c08f-4f5c-a3ea-2389af4539fe",
        "RALType": "changeOwner"
      },
      {
        "UID": "f707684b-7ae1-4c15-bc4c-da7e6f682798",
        "RALType": "changeOwner"
      },
      {
        "UID": "095b3513-0697-4d65-8c04-a81b668fa760",
        "RALType": "changeOwner"
      },
      {
        "UID": "73b19f6c-5915-43c4-83b5-79b3f5e9cff7",
        "RALType": "changeOwner"
      },
      {
        "UID": "3a09fd0a-f8b8-487f-b409-155b70c2143b",
        "RALType": "changeOwner"
      },
      {
        "UID": "5a1f0dcc-3c63-47c7-b6e2-80cac5d60b94",
        "RALType": "changeOwner"
      }
    ],
    "email": "igeler7@gmail.com"
  },
  "duration": null,
  "identity": {
    "alternateIDs": [],
    "alternateNames": [],
    "UID": "02333a62-7b35-4f98-9e1f-a9cbf56dcd48",
    "name": "",
    "siteTag": ""
  },
  "methodState": "finished",
  "template": {
    "RALType": "changeContainer",
    "version": "1",
    "methodStateTemplates": "generalMethodState"
  },
  "inputObjects": [
    {
      "locationHistoryRef": [],
      "ownerHistoryRef": [],
      "linkedObjectRef": [],
      "identity": {
        "alternateIDs": [],
        "alternateNames": [],
        "UID": "2a9c7dec-0f4d-448f-befb-c305364f960a",
        "name": "",
        "siteTag": ""
      },
      "currentOwners": [
        {
          "UID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
          "role": "owner"
        }
      ],
      "definition": {
        "definitionText": "Coffee, in relation to harvested coffee beans, refers to the seeds of the Coffea plant, typically extracted from its fruit (called cherries). These beans are harvested, processed, dried, and roasted to produce the beverage known as coffee. They are the primary raw material for making brewed coffee, with their flavor influenced by factors like origin, processing methods, and roasting techniques.",
        "definitionURL": ""
      },
      "objectState": "undefined",
      "template": {
        "RALType": "coffee",
        "version": "1",
        "objectStateTemplates": "generalObjectState"
      },
      "specificProperties": [
        {
          "key": "species",
          "value": "coffea arabica",
          "unit": "String"
        },
        {
          "key": "country",
          "value": "Honduras",
          "unit": "String"
        },
        {
          "key": "amount",
          "value": 0.48,
          "unit": "quintales"
        },
        {
          "key": "processingState",
          "value": "pergamino seco",
          "unit": "String"
        },
        {
          "value": [],
          "key": "qualityState",
          "unit": "stringlist"
        }
      ],
      "currentGeolocation": {
        "container": {
          "UID": "unknown"
        },
        "postalAddress": {
          "country": "unknown",
          "cityName": "unknown",
          "cityNumber": "unknown",
          "streetName": "unknown",
          "streetNumber": "unknown"
        },
        "3WordCode": "unknown",
        "geoCoordinates": {
          "longitude": 0,
          "latitude": 0
        },
        "plusCode": "unknown"
      },
      "methodHistoryRef": [
        {
          "UID": "29f846a8-d09e-46f8-a568-f2c63d46cbc4",
          "RALType": "generateDigitalSibling"
        },
        {
          "UID": "5a1f0dcc-3c63-47c7-b6e2-80cac5d60b94",
          "RALType": "changeOwner"
        }
      ],
      "role": "item"
    },
    {
      "currentOwners": [],
      "locationHistoryRef": [],
      "ownerHistoryRef": [],
      "linkedObjectRef": [],
      "identity": {
        "alternateNames": [],
        "UID": "c045fb26-18a5-41fa-8b3e-887bc1f8baf1",
        "name": "",
        "siteTag": "",
        "alternateIDs": [
          {
            "UID": "3f578aa05ab1a00e71ded5d547d2e0cc41b2c339d89989232f6a30ddde0353bd",
            "issuedBy": "Asset Registry"
          }
        ]
      },
      "definition": {
        "definitionText": "In an agricultural context, a 'field' refers to a specific area of land designated for the cultivation of crops or the grazing of livestock. Fields are typically delineated by natural boundaries like hedgerows, fences, or other markers, and they are managed by farmers to optimize the production of agricultural products. The size, shape, and use of a field can vary widely depending on the type of farming, the landscape, and the agricultural practices employed. Fields are fundamental units in farming operations, and they may be used for growing a single crop (monoculture) or multiple crops (polyculture), or for rotational grazing in the case of livestock farming. Soil preparation, irrigation, planting, and harvesting are all activities that take place within these fields.",
        "definitionURL": " "
      },
      "objectState": "undefined",
      "template": {
        "RALType": "field",
        "version": "1",
        "objectStateTemplates": "generalObjectState"
      },
      "specificProperties": [
        {
          "name": "area",
          "value": "",
          "unit": "ha"
        },
        {
          "name": "boundaries",
          "value": "",
          "unit": "vector_list"
        },
        {
          "name": "soil type",
          "value": "",
          "unit": "soil_type"
        },
        {
          "name": "soil value",
          "value": "",
          "unit": "soil_value_germany"
        }
      ],
      "currentGeolocation": {
        "container": {
          "UID": "unknown"
        },
        "postalAddress": {
          "country": "unknown",
          "cityName": "unknown",
          "cityNumber": "unknown",
          "streetName": "unknown",
          "streetNumber": "unknown"
        },
        "3WordCode": "unknown",
        "geoCoordinates": {
          "longitude": 0,
          "latitude": 0
        },
        "plusCode": "unknown"
      },
      "methodHistoryRef": [
        {
          "UID": "af83589c-624b-4931-b101-933a1610c91e",
          "RALType": "generateDigitalSibling"
        }
      ],
      "role": "oldContainer"
    },
    {
      "locationHistoryRef": [],
      "ownerHistoryRef": [],
      "linkedObjectRef": [],
      "identity": {
        "alternateNames": [],
        "UID": "00d25f49-801d-4a5f-8cf9-a20750f2eae3",
        "name": "RioFrio23022025C2",
        "siteTag": "",
        "alternateIDs": [
          {
            "UID": "RioFrio23022025C2",
            "issuedBy": "owner"
          }
        ]
      },
      "currentOwners": [
        {
          "UID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
          "role": "owner"
        }
      ],
      "definition": {
        "definitionText": "The term 'container' has different meanings depending on the context, but generally, a 'container' refers to an object or vessel used to hold, store, or transport items, substances, or materials. Here are a few specific definitions based on different contexts: A container is any object that can hold and secure contents, often with a lid, seal, or closure. This includes boxes, bottles, jars, cans, and crates used for storage or transport.",
        "definitionURL": "https://www.thefreedictionary.com/container"
      },
      "objectState": "undefined",
      "template": {
        "RALType": "container",
        "version": "1",
        "objectStateTemplates": "generalObjectState"
      },
      "specificProperties": [
        {
          "key": "serial number",
          "value": "",
          "unit": "String"
        },
        {
          "key": "max capacity",
          "value": 500,
          "unit": "quintales"
        }
      ],
      "currentGeolocation": {
        "container": {
          "UID": "unknown"
        },
        "postalAddress": {
          "country": "unknown",
          "cityName": "unknown",
          "cityNumber": "unknown",
          "streetName": "unknown",
          "streetNumber": "unknown"
        },
        "3WordCode": "unknown",
        "geoCoordinates": {
          "latitude": 14.866823,
          "longitude": -88.413033
        },
        "plusCode": "unknown"
      },
      "methodHistoryRef": [
        {
          "UID": "6405ec11-c037-47bc-8697-cca5e4b72050",
          "RALType": "generateDigitalSibling"
        }
      ],
      "role": "newContainer"
    }
  ],
  "outputObjects": [
    {
      "locationHistoryRef": [],
      "ownerHistoryRef": [],
      "linkedObjectRef": [],
      "identity": {
        "alternateIDs": [],
        "alternateNames": [],
        "UID": "2a9c7dec-0f4d-448f-befb-c305364f960a",
        "name": "",
        "siteTag": ""
      },
      "currentOwners": [
        {
          "UID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
          "role": "owner"
        }
      ],
      "definition": {
        "definitionText": "Coffee, in relation to harvested coffee beans, refers to the seeds of the Coffea plant, typically extracted from its fruit (called cherries). These beans are harvested, processed, dried, and roasted to produce the beverage known as coffee. They are the primary raw material for making brewed coffee, with their flavor influenced by factors like origin, processing methods, and roasting techniques.",
        "definitionURL": ""
      },
      "objectState": "undefined",
      "template": {
        "RALType": "coffee",
        "version": "1",
        "objectStateTemplates": "generalObjectState"
      },
      "specificProperties": [
        {
          "key": "species",
          "value": "coffea arabica",
          "unit": "String"
        },
        {
          "key": "country",
          "value": "Honduras",
          "unit": "String"
        },
        {
          "key": "amount",
          "value": 0.48,
          "unit": "quintales"
        },
        {
          "key": "processingState",
          "value": "pergamino seco",
          "unit": "String"
        },
        {
          "value": [],
          "key": "qualityState",
          "unit": "stringlist"
        }
      ],
      "currentGeolocation": {
        "container": {
          "UID": "00d25f49-801d-4a5f-8cf9-a20750f2eae3"
        },
        "postalAddress": {
          "country": "unknown",
          "cityName": "unknown",
          "cityNumber": "unknown",
          "streetName": "unknown",
          "streetNumber": "unknown"
        },
        "3WordCode": "unknown",
        "geoCoordinates": {
          "longitude": 0,
          "latitude": 0
        },
        "plusCode": "unknown"
      },
      "methodHistoryRef": [
        {
          "UID": "29f846a8-d09e-46f8-a568-f2c63d46cbc4",
          "RALType": "generateDigitalSibling"
        },
        {
          "UID": "5a1f0dcc-3c63-47c7-b6e2-80cac5d60b94",
          "RALType": "changeOwner"
        },
        {
          "UID": "02333a62-7b35-4f98-9e1f-a9cbf56dcd48",
          "RALType": "changeContainer"
        }
      ],
      "role": "item"
    }
  ],
  "digitalSignatures": [
    {
      "signature": "FAqAFaeV1M7ke7CT8gkPwY2ReujW6b5W9Wd7aekqWarNnX2BUyDLsLSjT55fOfEZEScwS0+3auZUgKXFv2zrCg==",
      "signerUID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
      "signedContent": [
        "$"
      ]
    }
  ]
}
```