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

Breaking down the example:

## identity
```json
"identity": {
    "alternateIDs": [],
    "alternateNames": [],
    "UID": "02333a62-7b35-4f98-9e1f-a9cbf56dcd48",
    "name": "",
    "siteTag": ""
}
```
The identity section contains all identifiers and names for the method:
- `UID`: A unique identifier (UUIDv4) that globally identifies this specific method instance
- `alternateIDs`: An array of alternative IDs issued by other systems. Each alternate ID contains:
  - `id`: The alternative identifier string
  - `issuedBy`: The system or authority that issued this alternate ID
- `alternateNames`: An array of alternative names used for this method
- `name`: The primary human-readable name of the method. This is not unique and can be changed
- `siteTag`: A location-specific tag or identifier used on-site

## template
```json
"template": {
    "RALType": "changeContainer",
    "version": "1",
    "methodStateTemplates": "generalMethodState"
}
```
The template section defines the type and structure of the method:
- `RALType`: Defines the type of the method (in this case "changeContainer"). It should be selected from the official RALTypes available at https://open-ral.io/ to ensure interoperability across systems and organizations. Use the semantic search API endpoint (`/semantic_search`) to discover appropriate official templates by describing your concept in natural language. For guidance on custom ralTypes when no official template matches your needs, see the "Official vs. Custom RALTypes" section above
- `methodStateTemplates`: Specifies which values the methodState field can have. In this case, it uses the "generalMethodState" template that defines common states for methods: undefined, planned, controlRequired, running, cancelled, finished. Multiple templates can be combined to mix their allowed states
- `version`: The version number of the RALType specification being used

## definition
```json
"definition": {
    "definitionText": "A Method to change the container of an object",
    "definitionURL": ""
}
```
The definition section provides semantic information about what this RALType of method represents:
- `definitionText`: A comprehensive free-text description of what this method type means and how it is used in its domain context
- `definitionURL`: A URL reference to external documentation or standards that further define this method type

## existenceStarts
```json
"existenceStarts": "2025-02-23T17:40:22"
```
The existenceStarts field contains an ISO 8601 timestamp (UTC) indicating when this method was created or when it started to exist in the system.

## executor
```json
"executor": {
    "identity": {
      "UID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
      ...
    },
    "template": {
      "RALType": "human",
      ...
    },
    ...
}
```
The executor section contains a complete RalObject representing the entity (person, machine, or organization) that executes or executed this method:
- This is a full RalObject, not just a reference, providing complete information about the executor
- In this example, the executor is a RalObject of type "human"
- The executor can be any RalObject type that is capable of performing the method (e.g., "human", "robot", "machine", "software_agent")

## inputObjects
```json
"inputObjects": [
    {
      "identity": {
        "UID": "2a9c7dec-0f4d-448f-befb-c305364f960a",
        ...
      },
      "template": {
        "RALType": "coffee",
        ...
      },
      "role": "item",
      ...
    },
    ...
]
```
The inputObjects section contains complete RalObjects that serve as input parameters for the method:
- An array of full RalObject instances, each with an additional `role` field
- These objects represent a specific state at the time of method creation (a snapshot), rather than a reference to the most current state
- The `role` field specifies the role of each input object in the method, similar to parameter names in programming functions (e.g., "item", "oldContainer", "newContainer")
- This creates an immutable record of what the input objects looked like when the method was executed

## inputObjectsRef
```json
"inputObjectsRef": []
```
The inputObjectsRef section contains references to RalObjects that serve as input parameters:
- An array of object references, each with a `role`, `UID`, and optional `domain` field
- Unlike `inputObjects`, these references always point to the most current state of the object
- This is useful when you need to reference objects without embedding their complete state
- Can be empty if all inputs are provided as complete objects in `inputObjects`

## outputObjects
```json
"outputObjects": [
    {
      "identity": {
        "UID": "2a9c7dec-0f4d-448f-befb-c305364f960a",
        ...
      },
      "currentGeolocation": {
        "container": {
          "UID": "00d25f49-801d-4a5f-8cf9-a20750f2eae3"
        },
        ...
      },
      "methodHistoryRef": [
        ...,
        {
          "UID": "02333a62-7b35-4f98-9e1f-a9cbf56dcd48",
          "RALType": "changeContainer"
        }
      ],
      "role": "item",
      ...
    }
]
```
The outputObjects section contains complete RalObjects that are the result of the method execution:
- An array of full RalObject instances, each with an additional `role` field
- These objects were either newly created or modified by the method
- The `role` field specifies the role of each output object in the method result
- Notice how the output object's state differs from the input object (e.g., updated container, added method to history)
- This creates a complete record of the method's effects on objects

## outputObjectsRef
```json
"outputObjectsRef": []
```
The outputObjectsRef section contains references to RalObjects that are the result of the method execution:
- An array of object references, each with a `role`, `UID`, and optional `domain` field
- These references point to objects that were either newly created or modified by the method
- Can be empty if all outputs are provided as complete objects in `outputObjects`

## methodState
```json
"methodState": "finished"
```
The methodState field indicates the current state of the method execution:
- The possible states are defined by the `methodStateTemplates` specified in the template section
- Common states for "generalMethodState" include:
  - `undefined`: Undefined method state
  - `planned`: The method is planned but not yet executed
  - `controlRequired`: An error occurred that should be checked
  - `running`: The method is currently being executed
  - `cancelled`: The method was cancelled
  - `finished`: The method was successfully completed

## duration
```json
"duration": null
```
The duration field contains the duration of the method execution:
- Can be an ISO 8601 duration string (e.g., "PT1H30M" for 1 hour 30 minutes)
- Can be `null` if the duration is not tracked or not yet determined
- Useful for tracking how long a process took to complete

## nestedMethods
```json
"nestedMethods": []
```
The nestedMethods section contains nested RalMethods that are executed as part of this method:
- An array of complete RalMethod instances
- Allows for hierarchical composition of methods, similar to function calls in programming
- Nested methods can have their own inputs, outputs, and nested methods
- Can be used with `objectConnectors` to define how inputs are passed to nested methods
- Empty in this example, but would contain full RalMethod objects when used

## specificProperties
```json
"specificProperties": []
```
The specificProperties section contains RALType-specific properties:
- An array of property objects, each with a `key`, `value`, `unit`, and optional `description`
- The properties are defined by the RALType specification
- These properties provide method-specific configuration or parameters
- For example, a "fertilizing" method might have properties like:
  - `fertilizer_type`: The type of fertilizer used
  - `amount`: The amount applied
  - `application_rate`: The rate of application
- Empty in this example as the "changeContainer" method doesn't require additional properties

## digitalSignatures
```json
"digitalSignatures": [
    {
      "signature": "FAqAFaeV1M7ke7CT8gkPwY2ReujW6b5W9Wd7aekqWarNnX2BUyDLsLSjT55fOfEZEScwS0+3auZUgKXFv2zrCg==",
      "signerUID": "8bIquGNww2cChmaWEgdlpX0tgzv1",
      "signedContent": [
        "$"
      ],
      "algorithm": "Ed25519"
    }
]
```
The digitalSignatures section contains cryptographic signatures that verify the authenticity and integrity of the method:
- An optional array of signature objects that can be used to prove who created or approved the method
- Each signature contains:
  - `signature`: A Base64-encoded digital signature string
  - `signerUID`: The UID of the signer (references a RalObject, typically of type "human" or "organization")
  - `signedContent`: An array of JSON Path expressions specifying which parts of the method were signed
    - `"$"` means the entire method (root) was signed
    - More specific paths like `"$.inputObjects[0]"` or `"$.methodState"` can sign specific parts
    - Multiple paths can be included to sign different parts separately
  - `algorithm`: (Optional) The cryptographic algorithm used for signing. Defaults to "Ed25519" if not specified. Supported algorithms include:
    - `Ed25519`: Elliptic curve signature scheme (default, recommended for new implementations)
    - `RSA-SHA256`: RSA with SHA-256 hashing
    - `ECDSA-P256-SHA256`: Elliptic Curve Digital Signature Algorithm with P-256 curve and SHA-256

**Multiple Signatures**: The array structure allows multiple parties to sign the same method, each potentially using different algorithms. This is useful for:
- Multi-party approval processes (e.g., farmer and inspector both sign a harvest method)
- Regulatory compliance (e.g., organic certification requires signatures from farmer and certifier)
- Audit trails (e.g., different stakeholders sign at different stages of a process)

**Public Key Lookup**: The `signerUID` references a RalObject that should contain the public key information needed to verify the signature. The public key is typically stored in the `specificProperties` of the referenced RalObject.

**Signature Verification Process**:
1. Retrieve the public key from the RalObject referenced by `signerUID`
2. Extract the content specified by the `signedContent` JSON Path expressions
3. Canonicalize the JSON content (remove whitespace, sort keys) to ensure consistent hashing
4. Verify the signature using the public key and the specified algorithm
5. If verification succeeds, the authenticity and integrity of the signed content is confirmed

**Usage Examples**:
- **Regulatory Compliance**: A farmer signs a harvest method to certify when and how crops were harvested
- **Traceability**: Multiple stakeholders sign methods at different stages of a supply chain
- **Audit Trail**: Methods are signed to create tamper-evident records of agricultural operations
- **Authorization**: Digital signatures prove that a method was approved by authorized personnel

**Note**: The `digitalSignatures` field is optional. Methods without signatures are still valid but lack cryptographic proof of authenticity. RalObjects can also include digital signatures using the same structure.


open_ral.schema.json:
```json

{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$comment": "Definitions that start with '_' (e.g. _Identity) are reusable components shared by both RalObjects and RalMethods. They do not represent valid standalone entities in the context of openRAL.",
    "title": "openRAL JSON Schema",
    "description": "This documents defines the schema for RalObjects and RalMethods of the openRAL.",
    "$defs": {
        "RalMethod": {
            "type": "object",
            "description": "A RalMethod represents a process that can be executed.",
            "properties": {
                "identity": {
                    "$ref": "#/definitions/_Identity"
                },
                "definition": {
                    "$ref": "#/definitions/_Definition"
                },
                "template": {
                    "allOf": [
                        {
                            "$ref": "#/definitions/_BaseTemplate"
                        },
                        {
                            "properties": {
                                "methodStateTemplates": {
                                    "type": "array",
                                    "description": "Defines the method state templates. These determine the allowed values for methodState. For example, 'generalMethodState' allows values: undefined, planned, controlRequired, running, cancelled, finished. Multiple templates can be combined, mixing their allowed states.",
                                    "items": {
                                        "type": "string"
                                    },
                                    "default": [
                                        "generalMethodState"
                                    ],
                                    "minItems": 1
                                }
                            },
                            "required": [
                                "methodStateTemplates"
                            ]
                        }
                    ]
                },
                "executor": {
                    "type": "object",
                    "TODO": "Wie ist das Schema des Executors definiert?",
                    "description": "Contains information about who executes the method"
                },
                "inputObjects": {
                    "type": "array",
                    "description": "A list of objects that serve as input parameters for the RalMethod. These objects represent a specific state at the time of method creation, rather than a reference to the most current state.",
                    "items": {
                        "type": "object",
                        "allOf": [
                            {
                                "$ref": "#/definitions/RalObject"
                            },
                            {
                                "properties": {
                                    "role": {
                                        "type": "string",
                                        "description": "Specifies the role of the input object in the RalMethod, similar to parameter names in programming language functions"
                                    }
                                },
                                "required": [
                                    "role"
                                ]
                            }
                        ]
                    }
                },
                "inputObjectsRef": {
                    "type": "array",
                    "description": "A list of references to RalObjects. These references always point to the most current state of the object, unlike inputObjects which represent a specific state for each object.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "role": {
                                "type": "string",
                                "description": "Specifies the role of the referenced object in the RalMethod"
                            },
                            "UID": {
                                "type": "string",
                                "format": "uuid",
                                "description": "The UUIDv4 of the referenced RalObject"
                            },
                            "domain": {
                                "type": [
                                    "string",
                                    "null"
                                ],
                                "description": "The domain where the RalObject can be found. If not provided, it's assumed to be in the current domain."
                            }
                        },
                        "required": [
                            "role",
                            "UID"
                        ]
                    },
                    "uniqueItems": true
                },
                "methodState": {
                    "type": "string",
                    "enum": [
                        "undefined",
                        "planned",
                        "controlRequired",
                        "running",
                        "cancelled",
                        "finished"
                    ],
                    "description": "The current state of the method execution",
                    "default": "undefined",
                    "enumDescriptions": {
                        "undefined": "Undefined method state",
                        "planned": "The method is planned but not yet executed",
                        "controlRequired": "An error occurred that should be checked",
                        "running": "The method is currently being executed",
                        "cancelled": "The method was cancelled",
                        "finished": "The method was successfully completed"
                    }
                },
                "nestedMethods": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/RalMethod"
                    },
                    "description": "A list of nested RalMethods that are executed as part of the parent RalMethod execution"
                },
                "outputObjects": {
                    "type": "array",
                    "description": "A list of complete RalObjects that are the result of the method execution. These objects were either newly created or modified by the method.",
                    "items": {
                        "type": "object",
                        "allOf": [
                            {
                                "$ref": "#/definitions/RalObject"
                            },
                            {
                                "properties": {
                                    "role": {
                                        "type": "string",
                                        "description": "Specifies the role of the output object in the RalMethod result"
                                    }
                                },
                                "required": [
                                    "role"
                                ]
                            }
                        ]
                    }
                },
                "outputObjectsRef": {
                    "type": "array",
                    "description": "A list of references to RalObjects that are the result of the method execution. These references point to objects that were either newly created or modified by the method.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "role": {
                                "type": "string",
                                "description": "Specifies the role of the referenced output object in the RalMethod result"
                            },
                            "UID": {
                                "type": "string",
                                "format": "uuid",
                                "description": "The UUIDv4 of the referenced RalObject"
                            },
                            "domain": {
                                "type": "string",
                                "description": "The domain where the RalObject can be found. If not provided, it's assumed to be in the same domain as the current object."
                            }
                        },
                        "required": [
                            "role",
                            "UID"
                        ]
                    }
                },
                "specificProperties": {
                    "$ref": "#/definitions/_SpecificProperties"
                },
                "objectConnectors": {
                    "type": "array",
                    "description": "Defines how InputObjects or InputObjectsRef are passed to NestedMethods, similar to function calls in programming languages.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "source": {
                                "type": "string",
                                "description": "JSON Path referencing an InputObject or InputObjectsRef in the parent RalMethod",
                                "pattern": "^\\$\\.(inputObjects|inputObjectsRef)\\[\\d+\\]$"
                            },
                            "target": {
                                "type": "string",
                                "description": "JSON Path referencing an InputObject or InputObjectsRef in a NestedMethod",
                                "pattern": "^\\$\\.nestedMethods\\[\\d+\\]\\.(inputObjects|inputObjectsRef)\\[\\d+\\]$"
                            },
                            "targetRole": {
                                "type": "string",
                                "description": "Defines the role the object will have in the NestedMethod"
                            }
                        },
                        "required": [
                            "source",
                            "target",
                            "targetRole"
                        ]
                    }
                },
                "digitalSignatures": {
                    "type": "array",
                    "description": "Optional array of cryptographic signatures that verify the authenticity and integrity of the method. Supports multiple signatures from different parties, each potentially using different algorithms.",
                    "items": {
                        "$ref": "#/definitions/_DigitalSignature"
                    }
                }
            },
            "required": [
                "identity",
                "definition",
                "template",
                "inputObjects",
                "inputObjectsRef",
                "methodState",
                "nestedMethods",
                "outputObjects",
                "outputObjectsRef",
                "specificProperties"
            ]
        },
        "RalObject": {
            "type": "object",
            "description": "A RalObject is the description of a real or digital object. It contains information about its state, owners, and methods and acts as a digital twin.",
            "properties": {
                "identity": {
                    "$ref": "#/definitions/_Identity"
                },
                "definition": {
                    "$ref": "#/definitions/_Definition"
                },
                "template": {
                    "allOf": [
                        {
                            "$ref": "#/definitions/_BaseTemplate"
                        },
                        {
                            "properties": {
                                "objectStateTemplates": {
                                    "type": "array",
                                    "description": "Defines the object state templates. These determine the allowed values for objectState. For example, 'generalObjectState' allows values: undefined, active, inactive. Multiple templates can be combined, mixing their allowed states.",
                                    "items": {
                                        "type": "string"
                                    },
                                    "default": [
                                        "generalObjectState"
                                    ],
                                    "minItems": 1
                                }
                            },
                            "required": [
                                "objectStateTemplates"
                            ]
                        }
                    ]
                },
                "objectState": {
                    "type": "string",
                    "description": "Current state of the object. Possible values depend on the objectStateTemplates defined in the template.",
                    "default": "undefined"
                },
                "specificProperties": {
                    "$ref": "#/definitions/_SpecificProperties"
                },
                "linkedObjectsRef": {
                    "type": "array",
                    "description": "A list of references to RalObjects that are related to this object. The role 'owner' is reserved for ownership relationships.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "role": {
                                "type": "string",
                                "description": "Describes the role of the referenced RalObject and the relationship of the referenced object to the current object. The role 'owner' is reserved for ownership relationships."
                            },
                            "UID": {
                                "type": "string",
                                "format": "uuid",
                                "description": "The UUIDv4 of the referenced RalObject"
                            },
                            "domain": {
                                "type": "string",
                                "description": "The domain where the RalObject can be found. If not provided, it's assumed to be in the same domain as the current object."
                            }
                        },
                        "required": [
                            "role",
                            "UID"
                        ]
                    }
                },
                "currentGeolocation": {
                    "type": "object",
                    "description": "Defines the current location of the object. Can be a physical location or a logical location by referencing a container object.",
                    "example": {
                        "container": {
                            "UID": "..."
                        },
                        "geoCoordinates": {
                            "latitude": 50.0,
                            "longitude": 10.0
                        },
                        "3WordCode": "",
                        "plusCode": "",
                        "postalAddress": {
                            "cityName": "",
                            "cityNumber": "",
                            "country": "",
                            "streetName": "",
                            "streetNumber": ""
                        }
                    },
                    "properties": {
                        "container": {
                            "type": "object",
                            "description": "The container object that contains the object",
                            "properties": {
                                "UID": {
                                    "type": "string",
                                    "format": "uuid",
                                    "description": "The UUIDv4 of the container object"
                                },
                                "domain": {
                                    "type": "string",
                                    "description": "The domain where the Container RalObject can be found. If not provided, it's assumed to be in the same domain as the current object."
                                }
                            },
                            "required": [
                                "UID"
                            ]
                        },
                        "geoCoordinates": {
                            "type": "object",
                            "description": "The geo coordinates of the object in latitude and longitude (WGS84)",
                            "example": {
                                "latitude": 52.0,
                                "longitude": 10.0
                            },
                            "properties": {
                                "latitude": {
                                    "type": "number"
                                },
                                "longitude": {
                                    "type": "number"
                                }
                            },
                            "required": [
                                "latitude",
                                "longitude"
                            ]
                        },
                        "3WordCode": {
                            "type": "string",
                            "description": "A 3-word code for geographic positions is a system that divides the entire world into a grid of 3m x 3m squares, with each square assigned a unique combination of three words.",
                            "example": "///filled.count.soap"
                        },
                        "plusCode": {
                            "type": "string",
                            "description": "Open Location Codes from Google. Similar to 3WordCode. Can have different lengths for different precision",
                            "example": "V75V+8Q"
                        },
                        "postalAddress": {
                            "type": "object",
                            "description": "The postal address of the object",
                            "properties": {
                                "cityName": {
                                    "type": "string"
                                },
                                "cityNumber": {
                                    "type": "string",
                                    "description": "The number of the city. Often a zip code"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "streetName": {
                                    "type": "string"
                                },
                                "streetNumber": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "methodHistoryRef": {
                    "type": "array",
                    "description": "References RalMethods that were executed on this object or will be executed in the future. The object could be an inputObject or an outputObject of the method.",
                    "default": [],
                    "items": {
                        "type": "object",
                        "properties": {
                            "UID": {
                                "type": "string",
                                "format": "uuid",
                                "description": "The UUIDv4 of the RalMethod"
                            },
                            "RALType": {
                                "type": "string",
                                "description": "The RalType of the RalMethod"
                            },
                            "methodState": {
                                "type": "string",
                                "description": "The current state of the RalMethod"
                            },
                            "executor": {
                                "type": "object",
                                "description": "The executor of the RalMethod. If only the RALType is given, any executor that inherits from this RALType can execute the ",
                                "properties": {
                                    "UID": {
                                        "type": "string",
                                        "format": "uuid",
                                        "description": "The UUIDv4 of the executor"
                                    },
                                    "RALType": {
                                        "type": "string",
                                        "description": "The RalType of the executor"
                                    }
                                },
                                "required": [
                                    "RALType"
                                ]
                            }
                        },
                        "required": [
                            "UID", "RALType"
                        ]
                    }
                },
                "existenceStarts": {
                    "type": "string",
                    "description": "Defines the time the real object that is represented by the RalObject started to exist",
                    "format": "date-time"
                },
                "digitalSignatures": {
                    "type": "array",
                    "description": "Optional array of cryptographic signatures that verify the authenticity and integrity of the object. Supports multiple signatures from different parties, each potentially using different algorithms.",
                    "items": {
                        "$ref": "#/definitions/_DigitalSignature"
                    }
                }
            }
        },
        "_Identity": {
            "type": "object",
            "description": "Defines the identity of an entity",
            "properties": {
                "UID": {
                    "type": "string",
                    "format": "uuid",
                    "description": "A UUIDv4 that globally uniquely identifies the entire object"
                },
                "alternateIDs": {
                    "type": [
                        "array",
                        "null"
                    ],
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "The alternative ID value"
                            },
                            "issuedBy": {
                                "type": "string",
                                "description": "The identification system the alternative ID belongs to"
                            }
                        }
                    },
                    "description": "Optional alternative IDs that can be used in other environments"
                },
                "alternateNames": {
                    "type": [
                        "array",
                        "null"
                    ],
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional alternative names that can be used in other environments"
                },
                "name": {
                    "type": [
                        "string",
                        "null"
                    ],
                    "description": "Optional name for easier human identification, not necessarily globally unique"
                },
                "siteTag": {
                    "type": [
                        "string",
                        "null"
                    ],
                    "description": "Also known as 'domain', indicates the environment where the object is stored"
                }
            },
            "required": [
                "UID"
            ]
        },
        "_Definition": {
            "type": "object",
            "description": "Provides a general textual description of the RalType for the entity (RalMethod or RalObject). The description can be either directly in the definitionText or referenced via a URL in definitionURL. The description provides a general description the template/RalType and NOT the specific entity ",
            "examples": [
                "A farm is an agricultural entity engaged in crop cultivation and/or animal husbandry for the production of food and other products."
            ],
            "properties": {
                "definitionText": {
                    "type": [
                        "string",
                        "null"
                    ],
                    "description": "General textual description of the RalType"
                },
                "definitionURL": {
                    "type": [
                        "string",
                        "null"
                    ],
                    "format": "uri",
                    "description": "URL referencing the general description of the RALTyp"
                }
            },
            "anyOf": [
                {
                    "required": [
                        "definitionText"
                    ]
                },
                {
                    "required": [
                        "definitionURL"
                    ]
                }
            ]
        },
        "_BaseTemplate": {
            "type": "object",
            "description": "Defines the structure of a specific entity instance, similar but more restrictive than a JSON schema. All entites must have a template.",
            "properties": {
                "RALType": {
                    "type": "string",
                    "description": "The unique name of the template for the entity. RALTypes should be selected from the official registry at https://open-ral.io to ensure cross-organizational interoperability. Use the semantic search API endpoint (/semantic_search) to discover appropriate official templates. Custom ralTypes are possible but must follow reverse-domain notation (e.g., com.organization.typeName) and come with interoperability trade-offs. See the 'Official vs. Custom RALTypes' section in the documentation for detailed guidance. The RALType is comparable to classes in object-oriented programming, where RalObjects are instances of these classes."
                },
                "version": {
                    "type": [
                        "string"
                    ],
                    "description": "Optional field indicating the version of the RalType and its underlying template"
                }
            },
            "required": [
                "RALType",
                "version"
            ]
        },
        "_SpecificProperties": {
            "type": "array",
            "description": "Special properties of the RalMethod, such as configuration values. Each key must be unique.",
            "items": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "Unique identifier for the specific property"
                    },
                    "value": {
                        "description": "Value of the specific property. The type is defined by the unit."
                    },
                    "unit": {
                        "type": "string",
                        "description": "Unit of the value, should be a predefined unit from the unitExamples, but can be a custom one if needed.",
                        "unitExamples": {
                            "String": "string without further restrictions",
                            "integer": "integer number",
                            "number": "number, can be integer or float",
                            "boolean": "boolean true or false",
                            "regex": "a regex pattern",
                            "iso8601": "date or duration in ISO 8601 format",
                            "cronTab": "e.g. '*/5 * * * *'",
                            "json": "a json object",
                            "JSONString": "a string containing a json object",
                            "C": "degree in celsius - unit of temperature",
                            "V": "volt - unit of electric potential difference",
                            "A": "ampere - unit of electric current",
                            "dBm": "decibel-milliwatt - unit of power e.g. for signal strength",
                            "m": "meter - unit of length",
                            "s": "second - unit of time",
                            "kg": "kilogram - unit of mass"
                        }
                    },
                    "description": {
                        "type": "string",
                        "description": "Optional description explaining the meaning or purpose of the specific property"
                    }
                },
                "required": [
                    "key",
                    "value",
                    "unit"
                ]
            },
            "uniqueProperties": [
                "key"
            ]
        },
        "_DigitalSignature": {
            "type": "object",
            "description": "Represents a cryptographic digital signature that verifies the authenticity and integrity of a RalObject or RalMethod. Multiple signatures from different parties are supported.",
            "properties": {
                "signature": {
                    "type": "string",
                    "description": "Base64-encoded digital signature string",
                    "pattern": "^[A-Za-z0-9+/=]+$"
                },
                "signerUID": {
                    "type": "string",
                    "format": "uuid",
                    "description": "The UID of the signer (references a RalObject, typically of type 'human' or 'organization'). The referenced object should contain the public key needed for signature verification."
                },
                "signedContent": {
                    "type": "array",
                    "description": "Array of JSON Path expressions specifying which parts of the object/method were signed. Use '$' to sign the entire root object. Examples: '$.inputObjects[0]', '$.methodState'",
                    "items": {
                        "type": "string",
                        "pattern": "^\\$"
                    },
                    "minItems": 1
                },
                "algorithm": {
                    "type": "string",
                    "description": "The cryptographic algorithm used for signing. Defaults to 'Ed25519' if not specified.",
                    "enum": [
                        "Ed25519",
                        "RSA-SHA256",
                        "ECDSA-P256-SHA256"
                    ],
                    "default": "Ed25519"
                }
            },
            "required": [
                "signature",
                "signerUID",
                "signedContent"
            ]
        }
    }
}
```


openapi_semantic.yml:
```yml
openapi: 3.0.3
info:
  title: openRAL Semantic Search API
  description: API for semantic search of RAL templates
  version: 1.0.0
  
servers:
  - url: https://europe-west3-ral1-80620.cloudfunctions.net
    description: Production server

security:
  - ApiKeyAuth: []

paths:
  /semantic_search:
    post:
      summary: Perform semantic search on RAL templates
      description: > 
        Use this endpoint to find the appropriate official RALType when you don't know which template fits your use case.
        
        Describe your concept in natural language, and the API will return matching RAL templates ranked by semantic similarity.
        For example, searching for "a specific area of land designated for the cultivation of crops" will find templates like "field", "plot", or "farmland".
        
        Note: If you already know the exact RALType name, you can use it directly without searching.
        
        Attention: Semantic similarity does not guarantee semantic equivalence, but rather finds templates that are contextually relevant based on the input description.
      parameters:
        - name: query
          in: query
          required: true
          description: Search text for finding templates that match the semantic meaning of the input
          schema:
            type: string
            example: "a specific area of land designated for the cultivation of crops"
        - name: templateTypes
          in: query
          required: false
          description: Filter by template types (currently not implemented)
          schema:
            type: array
            items:
              type: string
              enum: ["object", "method"]
              example: "object"
      responses:
        '200':
          description: Successful search results
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SearchResult'
                  example:
                    name: "field"
                    roles: ["thing"]
                    templateId: "flxES9jiumQvMUCze8tE"
                    templateType: "object"
                    relevance: 562
                    definitionText: "In an agricultural context, a 'field' refers to a specific area of land designated for the cultivation of crops or the grazing of livestock. Fields are typically delineated by natural boundaries like hedgerows, fences, or other markers, and they are managed by farmers to optimize the production of agricultural products. The size, shape, and use of a field can vary widely depending on the type of farming, the landscape, and the agricultural practices employed. Fields are fundamental units in farming operations, and they may be used for growing a single crop (monoculture) or multiple crops (polyculture), or for rotational grazing in the case of livestock farming. Soil preparation, irrigation, planting, and harvesting are all activities that take place within these fields."
        '400':
          description: Bad request - invalid parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized - missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden - invalid or inactive API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-KEY
      description: API key for authentication
      
  schemas:
    SearchResult:
      type: object
      required:
        - name
        - roles
        - templateId
        - templateType
        - relevance
        - definitionText
      properties:
        name:
          type: string
          description: Name of the official template registered at open-ral.io, used as the ralType for corresponding objects or methods. All returned templates are from the official openRAL registry.
          example: "TemperatureSensor"
        roles:
          type: array
          items:
            type: string
          description: List of roles associated with the template
          example: ["thing"]
        templateId:
          type: string
          description: Unique identifier of the template
          example: "b8ee8880-680d-4c1b-a1ac-1dc5d85dfb72"
        templateType:
          type: string
          description: Object or method
          example: "object"
          enum: ["object", "method"]
        relevance:
          type: number
          format: float
          description: Relevance score based on vector distance
          example: 0.85
        definitionText:
          type: string
          description: Text definition of the template
          example: "A sensor device that measures ambient temperature"
          
    Error:
      type: object
      required:
        - errorMessage
      properties:
        errorMessage:
          type: string
          description: Human-readable error message
          example: "The provided API key is invalid or missing"


```


openapi.yml:
```yml
openapi: 3.0.3
info:
  title: openRAL Cloud Functions API
  description: |
    
    This API provides access to RAL templates, allowing authenticated clients to:
    - Retrieve specific templates by name
    - Submit requests for new templates
    - Monitor API health status
    
    **Authentication**: Most endpoints require an API key. The API key can be provided as x-api-key header.
  version: 1.0.0
  contact:
    name: Permarobotics Team
    email: team@permarobotics.com

servers:
  - url: https://europe-west3-ral1-80620.cloudfunctions.net
    description: Production API server

tags:
  - name: Health
    description: Service health check endpoints
  - name: Templates
    description: RAL template retrieval endpoints
  - name: Requests
    description: Template request management endpoints

security:
  - ApiKeyAuth: []

paths:
  /checkHealth:
    get:
      tags:
        - Health
      summary: Health check endpoint
      description: |
        Verifies that the API service is running and accessible. Returns HTTP 200 if the service is operational.
        This endpoint accepts all HTTP methods and requires no authentication.
      operationId: checkHealth
      security: []
      responses:
        '200':
          description: Service is healthy and operational
    post:
      tags:
        - Health
      summary: Health check endpoint (POST)
      description: Verifies service availability via POST method
      operationId: checkHealthPost
      security: []
      responses:
        '200':
          description: Service is healthy and operational
    put:
      tags:
        - Health
      summary: Health check endpoint (PUT)
      description: Verifies service availability via PUT method
      operationId: checkHealthPut
      security: []
      responses:
        '200':
          description: Service is healthy and operational
    delete:
      tags:
        - Health
      summary: Health check endpoint (DELETE)
      description: Verifies service availability via DELETE method
      operationId: checkHealthDelete
      security: []
      responses:
        '200':
          description: Service is healthy and operational

  /getTemplate:
    get:
      tags:
        - Templates
      summary: Retrieve a RAL template by name
      description: |
        Retrieves a RAL template in the requested format (JSON or XML).
        
        Returns the latest version of the template. If no format is specified, JSON is returned by default.
        
        **Authentication**: Requires a valid API key provided via the `x-api-key` header.
        
        **Future Work**: Version selection via `version` parameter is planned for future implementation.
      operationId: getTemplate
      parameters:
        - name: templateName
          in: query
          required: true
          description: The name of the template to retrieve
          schema:
            type: string
          example: "human"
        - name: returnFormat
          in: query
          required: false
          description: The format in which to return the template. Defaults to JSON if not specified.
          schema:
            type: string
            enum: [JSON, XML]
            default: JSON
          example: "JSON"
      responses:
        '200':
          description: Template retrieved successfully
          content:
            application/json:
              schema:
                type: object
                description: The template data in JSON format
              examples:
                humanTemplate:
                  summary: Human Template Example
                  value:
                    identity:
                      UID: "human_001"
                      name: "Human Template"
                      siteTag: "example-site"
                    template:
                      RALType: "human"
                      version: "1"
            application/xml:
              schema:
                type: string
                description: The template data in XML format
              example: |
                <?xml version="1.0" encoding="UTF-8"?>
                <template>
                  <identity>
                    <UID>human_001</UID>
                    <name>Human Template</name>
                    <siteTag>example-site</siteTag>
                  </identity>
                  <template>
                    <RALType>human</RALType>
                    <version>1</version>
                  </template>
                </template>
        '400':
          description: Bad request - missing or invalid parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                missingApiKey:
                  summary: Missing API Key
                  value:
                    type: "MissingAuthentication"
                    details: "API key is required. Provide it via the 'x-api-key' header."
                missingTemplateName:
                  summary: Missing Template Name
                  value:
                    type: "MissingParameter"
                    details: "Template name is required. Provide it via the 'templateName' query parameter."
                invalidFormat:
                  summary: Invalid Return Format
                  value:
                    type: "InvalidParameter"
                    details: "Invalid return format \"TXT\". Supported formats are: JSON, XML."
        '403':
          description: Forbidden - invalid or inactive API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                invalidApiKey:
                  summary: Invalid API Key
                  value:
                    type: "Forbidden"
                    details: "Invalid API key. The provided API key is not authorized."
                inactiveApiKey:
                  summary: Inactive API Key
                  value:
                    type: "Forbidden"
                    details: "API key is inactive. Contact the administrator to reactivate your access."
        '404':
          description: Not found - template does not exist or format not available
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                templateNotFound:
                  summary: Template Not Found
                  value:
                    type: "NotFound"
                    details: "Template \"unknownTemplate\" does not exist in the database."
                formatNotAvailable:
                  summary: Format Not Available
                  value:
                    type: "NotFound"
                    details: "Template \"human\" does not have data in XML format."
        '405':
          description: Method not allowed - only GET requests are supported
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                type: "MethodNotAllowed"
                details: "Only GET requests are supported. Use GET with query parameters."
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                type: "InternalServerError"
                details: "An unexpected error occurred while processing your request. Please try again later."

  /createTemplateRequest:
    post:
      tags:
        - Requests
      summary: Submit a request for a new RAL template
      description: |
        Submit a request for a new RAL template that doesn't currently exist in the system.
        
        The request will be reviewed by the Permarobotics team and you will receive a confirmation with a unique request ID.
        
        **Required Information**:
        - Detailed description of the template functionality
        - Template type or category
        - Your user ID for tracking and follow-up
      operationId: createTemplateRequest
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - templateDescription
                - templateType
                - requestUserId
              properties:
                templateDescription:
                  type: string
                  description: Detailed description of the requested template functionality and use case
                  example: "Need a template for autonomous weeding robots that can identify and remove weeds using computer vision while preserving crops. Should support different crop types and weeding strategies."
                templateType:
                  type: string
                  description: Category or type of the template being requested
                  example: "WeedingAutomation"
                requestUserId:
                  type: string
                  description: User ID of the person making the request
                  example: "user_12345_abc"
            examples:
              weedingRobot:
                summary: Request for Weeding Robot Template
                value:
                  templateDescription: "Need a template for autonomous weeding robots that can identify and remove weeds using computer vision while preserving crops. Should support different crop types and weeding strategies."
                  templateType: "WeedingAutomation"
                  requestUserId: "user_12345_abc"
              pestMonitoring:
                summary: Request for Pest Monitoring Template
                value:
                  templateDescription: "Template for automated pest detection and monitoring system using image recognition and pheromone traps. Should generate alerts when pest levels exceed thresholds."
                  templateType: "PestMonitoring"
                  requestUserId: "user_67890_xyz"
              soilAnalysis:
                summary: Request for Soil Analysis Template
                value:
                  templateDescription: "Multi-sensor soil analysis template that combines NPK sensors, pH measurement, and organic matter detection. Need integration with lab analysis results."
                  templateType: "SoilAnalysis"
                  requestUserId: "user_24680_def"
      responses:
        '200':
          description: Template request submitted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  requestId:
                    type: string
                    description: Unique ID of the created template request
                    example: "req_2024_12_01_abc123xyz"
              examples:
                successfulRequest:
                  summary: Successful Request Creation
                  value:
                    requestId: "req_2024_12_01_abc123xyz"
        '400':
          description: Bad request - missing required field or invalid user
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: "Bad Request"
                  message:
                    type: string
                    example: "Expected field templateDescription in request body missing"
              examples:
                missingField:
                  summary: Missing Required Field
                  value:
                    error: "Bad Request"
                    message: "Expected field templateDescription in request body missing. Body was: {\"templateType\":\"WeedingAutomation\",\"requestUserId\":\"user_123\"}"
                userNotFound:
                  summary: User Does Not Exist
                  value:
                    error: "Bad Request"
                    message: "User 'user_invalid_123' not found"
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key provided in the x-api-key header
  schemas:
    
    ErrorResponse:
      type: object
      description: Standard error response with structured information
      required:
        - type
        - details
      properties:
        type:
          type: string
          description: Error type or category (e.g., NotFound, Forbidden, InvalidParameter)
          example: "NotFound"
        details:
          type: string
          description: Detailed description of the error with actionable information
          example: "Template 'AgriculturalRobotScheduler' does not exist in the database."

```