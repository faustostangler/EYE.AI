---
name: Notation - C4 model
keywords: (placeholder)
metadata:
  url: None
  source: SOURCE_TYPE_TEXT
  date: 2026-05-16T15:32:01.632Z
  notebook: 1.3. Knowledge Management & Documentation
---
Notation - C4 model
Source: https://c4model.com/diagrams/notation
--------------------------------------------------------------------------------
Notation | C4 model Skip to main content C4 model Home Introduction History Abstractions
Software system
Container
Component
Code Microservices Queues and topics FAQ Diagrams
System context diagram
Container diagram
Component diagram
Code diagram System landscape diagram Dynamic diagram Deployment diagram Notation Review checklist FAQ Tooling FAQ Interactive example Book Video Training & workshops Patreon & Discord This website and example diagrams are licensed under a Creative Commons Attribution 4.0 International License. Diagrams Notation Notation The C4 model is notation independent, and doesn't prescribe any particular notation. That said, you still need to ensure that your diagram notation makes sense, and that the diagrams are comprehensible. A good way to think about this is to ask yourself whether each diagram can stand alone, and be (mostly) understood without a narrative. You can use this short software architecture diagram review checklist to help. Here are some general recommendations related to notation. Diagrams Every diagram should have a title describing the diagram type and scope (e.g. “System Context diagram for My Software System”). Every diagram should have a key/legend explaining the notation being used (e.g. shapes, colours, border styles, line types, arrow heads, etc). Acronyms and abbreviations (business/domain or technology) should be understandable by all audiences, or explained in the diagram key/legend. Elements The type of every element should be explicitly specified (e.g. Person, Software System, Container or Component). Every element should have a short description, to provide an “at a glance” view of key responsibilities. Every container and component should have a technology explicitly specified. Relationships Every line should represent a unidirectional relationship. Every line should be labelled, the label being consistent with the direction and intent of the relationship (e.g. dependency or data flow). Try to be as specific as possible with the label, ideally avoiding single words like, “Uses”. Relationships between containers (typically these represent inter-process communication) should have a technology/protocol explicitly labelled. Colours Although you may see many example diagrams and tools that make use of blue and grey boxes, this isn't something that is dictated by the C4 model, and you are free to use whatever colours you like! Just make sure that any colour coding is consistent (within and across diagrams) and be careful of things like black and white printers, color blindness, etc.
Diagram key/legend Any notation used should be as self-describing as possible, but all diagrams should have a key/legend to make the notation explicit. This applies to diagrams created with notations such as UML, ArchiMate and SysML too, as not everybody will know the notation being used. C4 and UML Although the example diagrams are created using a “boxes and lines” notation, the core diagrams can be illustrated using UML with the appropriate use of packages, components and stereotypes. The resulting UML diagrams do tend to lack the same degree of descriptive text though, because adding such text isn't possible (or easy) with some UML tools. Here are three examples of a system context, container and component diagram for comparison. C4 and ArchiMate See C4 Model, Architecture Viewpoint and Archi 4.7 for details of how to create C4 model diagrams with ArchiMate. Alternative visualisations Finally, don't feel that you need to always use a traditional “boxes and arrows” diagram. Although this is usually the default approach, there are other, often interactive, visualisations that can be used to show the same C4 model abstractions in very different ways.
