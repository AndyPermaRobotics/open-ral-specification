openRAL is an ontology-like knowledge representation that enables farmers, regulatory entities, scientists, but also software, AI, and machines to exchange information as structured data. This allows partners to develop interconnected software and machines easily. In contrast to real ontologies, the data structure is lightweight and purely oriented towards ease-of-use, speed, and low demand on computing power.

At its core, openRAL represents objects and processes in a consistent JSON base structure: RalObjects and RalMethods. This base structure ensures that fundamental properties of objects and methods/processes are represented in a uniform, reusable manner, with free-text descriptions that make the semantics of individual fields understandable for both humans and AI.

For example, it precisely defines how objects relate to each other (`linkedObjectsRef`) or in which state a method currently is (`methodState`).

The formal specification of these language constructs is defined and described in the `open_ral.schema.json` file.

A key concept is the `ralType`, which enables the definition of reusable "classes" or "templates" for the same things and processes across organizations. The `ralType` describes what something is and how it is structured, including which `specificProperties` exist for this particular type of object or method.



