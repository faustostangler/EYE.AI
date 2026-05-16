---
name: domain-storytelling | Skills Marketp... - LobeHub
keywords: (placeholder)
metadata:
  url: https://lobehub.com/skills/melodic-software-claude-code-plugins-domain-storytelling
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:12:00.489Z
  notebook: 1.1. Product Engineering
---
domain-storytelling | Skills Marketp... · LobeHub
Products Community Resources Pricing
76.8K Get started Ctrl K
LobeHub
/
Skills
/
melodic-software-claude-code-plugins-domain-storytelling
UN
domain-storytelling
1.0.1
melodic-software
Feb 23, 2026
4
4
28
Overview
Installation Method
SKILL.md
Resources 3
Related Skills
Version History
Summary
This Skill guides AI-assisted Domain Storytelling sessions to capture business processes as pictographic stories that feed event storming and bounded-context discovery. It facilitates collaborative workshops with domain experts, using a simple notation (actors, work objects, activities, sequences, annotations) to produce AS-IS and TO-BE story flows, annotated exceptions, and a ubiquitous-language glossary. Use it for requirements gathering, understanding current workflows, designing future-state processes, onboarding new team members, and preparing or seeding event-storming workshops. Key features include step-by-step facilitation prompts, templates for pictographic story maps, prompts to extract pain points and workarounds, and outputs formatted for bounded-context analysis. Core advantages: preserves expert language, reduces ambiguity between business and engineering, accelerates consensus, and creates visual, reusable artifacts for downstream design and implementation.
SKILL.md
Domain Storytelling Skill
Overview
Domain Storytelling is a collaborative modeling technique that captures business processes through pictographic stories. This skill guides AI-assisted domain storytelling sessions that can feed into event storming and bounded context discovery.
Key Principle: Stories are told from the perspective of domain experts, using their language and understanding.
When to Use This Skill
Keywords: domain storytelling, pictographic, actors, work objects, activities, AS-IS, TO-BE, business workflow, domain modeling, story collection, bounded context discovery, requirements gathering
Use this skill when:
Gathering requirements from domain experts
Understanding existing business workflows (AS-IS)
Designing future state processes (TO-BE)
Onboarding team members to a domain
Preparing for event storming sessions
Identifying bounded context candidates
Building a ubiquitous language glossary
Story Types
AS-IS Stories
Document how things work today:
Current state processes
Existing pain points
Workarounds and exceptions
Real behavior (not idealized)
When to use: Understanding current state, identifying problems, baseline before changes.
TO-BE Stories
Document how things should work:
Desired future state
Improved processes
New capabilities
Idealized flow (but achievable)
When to use: Requirements gathering, designing solutions, communicating vision.
Pictographic Language
Domain Storytelling uses simple pictographic elements:
Detailed notation guide: See references/pictographic-notation.md
AI-Assisted Story Collection Protocol
Phase 1: Story Collection
Goal: Gather the narrative from the user in their own words.
Prompts:
"Tell me about a typical [process] from start to finish"
"Walk me through what happens when [trigger event]"
"Who is involved and what do they do?"
Capture:
Who does what (actors and activities)
What they work with (work objects)
In what order (sequence)
Any variations or exceptions
Phase 2: Story Refinement
Goal: Explore edge cases and variations.
Prompts:
"What happens if [X] fails or is unavailable?"
"Are there any special cases or exceptions?"
"What's the most common path vs rare paths?"
"What frustrates you about this process?"
Capture:
Alternative flows
Error handling
Pain points
Implicit knowledge
Phase 3: Actor Identification
Goal: Map all participants in the story.
Prompts:
"Who else is involved that we haven't mentioned?"
"Are there any systems or external parties?"
"Who approves, reviews, or audits?"
Capture:
Human actors (by role, not name)
System actors (internal and external)
Actor responsibilities
Phase 4: Work Object Cataloging
Goal: Identify all data and documents exchanged.
Prompts:
"What information is passed between actors?"
"What documents or forms are used?"
"What data is created, updated, or referenced?"
Capture:
Documents and forms
Data entities
Physical items (if applicable)
Work object lifecycle
Phase 5: Boundary Discovery
Goal: Find bounded context candidates.
Analysis:
Where does terminology change?
Which actors work together closely?
What work objects belong together?
Where are the natural handoff points?
Output: Potential bounded context candidates for event storming.
Detailed boundary discovery: See references/boundary-discovery.md
Story Output Format
Text Representation
Markdown
Mermaid Diagram (Optional)
Plaintext
Story templates: See references/story-templates.md
Integration with Event Storming
Domain stories naturally feed into event storming:
Workflow: 
Plaintext
To proceed to event storming: Invoke the enterprise-architecture:event-storming skill with collected stories as input.
Facilitation Modes
Interactive Mode (Recommended)
The skill guides an interactive conversation with the user:
Ask open-ended questions
Capture responses as story elements
Reflect back for validation
Iterate until story is complete
Quick Mode
Rapid story capture from user-provided narrative:
User provides full narrative
Skill extracts actors, work objects, activities
Skill structures into story format
User validates and refines
Document Mode
Extract stories from existing documentation:
Read existing process documents
Extract story elements
Structure into story format
Validate with user
Glossary Building
As stories are collected, build a domain glossary:
Glossary purpose:
Establishes ubiquitous language
Identifies term collisions (same word, different meanings)
Documents domain knowledge
Supports bounded context discovery
Best Practices
DO
Use domain expert's language, not technical jargon
Capture stories at the right granularity (not too detailed)
Include exceptions and variations
Number activities sequentially
Document annotations for implicit knowledge
Build glossary as you go
DON'T
Impose technical terminology
Skip edge cases and exceptions
Assume you understand without asking
Mix AS-IS and TO-BE in same story
Forget to validate with domain expert
References
references/pictographic-notation.md - Detailed notation guide with examples
references/story-templates.md - YAML headers, output formats
references/boundary-discovery.md - Finding bounded contexts from stories
Related Skills
event-storming - Design "how it happens" after understanding "what happens"
modular-architecture - Implement bounded contexts discovered from stories
adr-management - Document significant decisions discovered during storytelling
Last Updated: 2025-12-22
User-Facing Interface
When invoked directly by the user, this skill creates domain stories.
Execution Workflow
Parse Arguments - Extract journey name and type (as-is or to-be). If no name provided, ask the user what business process to capture. Default type is as-is .
Spawn Story Facilitator - Launch the story-facilitator agent to guide the interactive session:
Collect the story (actors, work objects, activities, sequence)
Refine with edge cases and variations
Identify actors (human roles and systems)
Catalog work objects (documents, data, physical items)
Structure with numbered activities and Mermaid sequence diagram
Discover Boundaries - Identify bounded context candidates from terminology changes, actor groupings, and natural handoff points.
Save Results - Save to docs/domain-stories/[journey-name]-[type]-[date].md (or custom --dir ).
Suggest Follow-Ups - Recommend TO-BE stories, related processes, event storming for domain model design.
Version History
v1.0.0 (2025-12-26): Initial release
Ratings
0.0
No ratings yet
5
4
3
2
1
Send this prompt to your agent to leave a review
Agent Review
[x]
Newest [-]
Most helpful
No comments yet
Related Skills
View More
[UN
pptx
Featured 4.7 anthropics Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions "deck," "slides," "presentation," or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill. 59 Productivity & Tasks May 10, 2026 835 90.8k 28](https://lobehub.com/skills/anthropics-skills-pptx)
[UN
xlsx
Featured 4.7 anthropics Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like "the xlsx in my downloads") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved. 54 Productivity & Tasks May 10, 2026 350 90.8k 7](https://lobehub.com/skills/anthropics-skills-xlsx)
[UN
docx
Featured 4.9 anthropics Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation. 61 Productivity & Tasks May 10, 2026 518 90.8k 6](https://lobehub.com/skills/anthropics-skills-docx)
[UN
feishu-doc
4.5 openclaw Feishu document read/write operations. Activate when user mentions Feishu docs, cloud docs, or docx links. 2 Productivity & Tasks May 09, 2026 187 340.2k 1](https://lobehub.com/skills/openclaw-openclaw-feishu-doc)
[UN
slides
4.5 openai Create and edit presentation slide decks (.pptx) with PptxGenJS, bundled layout helpers, and render/validation utilities. Use when tasks involve building a new PowerPoint deck, recreating slides from screenshots/PDFs/reference decks, modifying slide content while preserving editable output, adding charts/diagrams/visuals, or diagnosing layout issues such as overflow, overlaps, and font substitution. 20 Productivity & Tasks May 10, 2026 86 13.8k 6](https://lobehub.com/skills/openai-skills-slides)
[UN
docx
5.0 K-Dense-AI Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation. 61 Productivity & Tasks May 10, 2026 45 18.0k 4](https://lobehub.com/skills/k-dense-ai-scientific-agent-skills-docx)
Run this SKILL
Installation Method
View Details [x]
I'm an Agent [-]
I'm a Human
Send this prompt to your agent to install the skill
Agent prompt
Copy Prompt
File Tree
Details 
references 
SKILL.md
 Run any SKILL with one click 
Agent teammates that grow with you
Start using LobeHub today and join thousands of super individuals
Get started for free Download Linux Version
Product
Pricing
Download
CLI
Agent Marketplace
MCP Marketplace
Skills Marketplace
Community Edition
Features
Features Overview
LobeHub vs. Manus
LobeHub vs. OpenClaw
LobeHub vs. Claude Cowork
Resources
Blog
Creator Reward Program
AI / LLM Icons
Docs
Developer
Open Source
Lobe Theme
Lobe i18n
Lobe UI
Lobe Icons
Lobe TTS
Company
About
Terms of Service
Privacy Policy
Contact  [-] [x]
English
© 2023-2026 LobeHub, LLC    
