openRAL is an ontology-like knowledge representation that enables farmers, regulatory entities, scientists, but also software, AI, and machines to exchange information as structured data. This allows partners to develop interconnected software and machines easily. In contrast to real ontologies, the data structure is lightweight and purely oriented towards ease-of-use, speed, and low demand on computing power.

At its core, openRAL represents objects and processes in a consistent JSON base structure: RalObjects and RalMethods. This base structure ensures that fundamental properties of objects and methods/processes are represented in a uniform, reusable manner, with free-text descriptions that make the semantics of individual fields understandable for both humans and AI.

For example, it precisely defines how objects relate to each other (`linkedObjectsRef`) or in which state a method currently is (`methodState`).

The formal specification of these language constructs is defined and described in the `open_ral.schema.json` file.

A key concept is the `ralType`, which enables the definition of reusable "classes" or "templates" for the same things and processes across organizations. The `ralType` describes what something is and how it is structured, including which `specificProperties` exist for this particular type of object or method.

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
  "currentOwners": [
    {
      "UID": "08ff32b5-f77b-47d6-9f27-30aed9f12f00"
    }
  ],
  "existenceStarts": "2025-11-26T15:29:13.088Z",
  "linkedObjectRef": [],
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
- `RALType`: Defines the type of the object (in this case "field"). It refers to the official RALTypes available at https://open-ral.io/
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

## currentOwners
```json
"currentOwners": [
    {
      "UID": "08ff32b5-f77b-47d6-9f27-30aed9f12f00"
    }
]
```
The currentOwners section lists all current owners of the object:
- An array of references to RalObjects (typically of type "person" or "organization") that own this object
- Each owner is referenced by their unique UID

## existenceStarts
```json
"existenceStarts": "2025-11-26T15:29:13.088Z"
```
The existenceStarts field contains an ISO 8601 timestamp (UTC) indicating when this object was created or when it started to exist in the system.

## linkedObjectRef
```json
"linkedObjectRef": []
```
The linkedObjectRef section contains references to other RalObjects that are logically related to this object:
- An array of UIDs referencing related objects (e.g., equipment assigned to this field, crops planted on it, or related parcels)
- This enables creating a network of interconnected objects

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


