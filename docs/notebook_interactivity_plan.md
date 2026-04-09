# Notebook Interactivity Plan

## Purpose

Add lightweight interactivity to lesson notebooks so students can answer practice questions and receive immediate checkpoint-style feedback without leaving the notebook.

The goal is to preserve the current lesson structure:

1. Explanation
2. Worked example
3. Practice
4. Feedback

But replace passive practice prompts with interactive answer widgets and guided checks.

## Why This Approach

The notebooks should feel closer to a guided tutor than a static handout, while staying simple enough to author and maintain inside the repository.

We are intentionally not building a full grading platform inside notebooks. The notebook layer should stay focused on:

- local practice
- instant feedback
- clear hints
- reusable lesson patterns

## Chosen Tools

- `Jupyter`: notebook runtime
- `ipywidgets`: input widgets, buttons, feedback output
- `Python`: exercise helper logic
- `sympy`: later support for symbolic math equivalence checks
- `ast.literal_eval`: safe parsing for vector and matrix-style answers

## Scope

### Phase 1

Build a reusable widget helper and convert one notebook into a working prototype.

Deliverables:

- reusable notebook exercise helper module
- one prototype notebook using the helper
- documented notebook authoring pattern

### Phase 2

Expand helpers for additional answer types and convert more notebooks.

Potential additions:

- symbolic answer checking
- tolerance-based numeric checking
- multiple choice
- hint and solution reveal widgets
- progress summary inside a notebook

### Out of Scope For Now

- secure answer hiding
- server-side grading
- user accounts
- cross-notebook progress persistence
- browser extension or Jupyter plugin automation

These belong in the future webapp, not the notebook layer.

## Functional Specs

### Student Experience

Each interactive exercise should provide:

- the prompt
- one clear input control
- a `Check Answer` button
- immediate feedback after clicking
- a hint on incorrect answers when available

### Author Experience

Authors should be able to define an exercise with a small amount of code:

- prompt
- expected answer
- optional hint
- optional success message

Notebook authors should not have to rebuild widget logic for each lesson.

Lesson-specific checkpoint definitions should live in a separate Python module whenever possible so the notebook itself stays clean and does not visibly expose expected answers during normal lesson use.

### Feedback Rules

- correct answer: short positive confirmation
- incorrect answer: encouraging correction message
- parse failure: tell the student how to format the answer

### Initial Supported Exercise Types

1. Numeric input
2. Vector input entered as a Python-style list, for example `[2, 3]`
3. Fixed-choice classification using a dropdown

## Technical Specs

## Helper Module

Create a reusable helper module at:

`notebooks/_helpers/exercises.py`

Initial API:

- `numeric_question(...)`
- `vector_question(...)`
- `dropdown_question(...)`

Each helper should return a widget container ready for display.

## Notebook Pattern

Each interactive notebook section should follow this structure:

1. Markdown explanation
2. One setup code cell that imports helper functions and lesson checkpoint modules
3. One short render cell that displays the checkpoint widgets

Preferred pattern:

- generic widget logic in `notebooks/_helpers/exercises.py`
- lesson-specific checkpoint definitions in a lesson module next to the notebook
- notebook code limited to imports and a short render call

## Expected Behaviors

- clicking `Check Answer` must not require running a separate checker cell
- feedback should appear in the same output area as the widget
- repeated attempts should replace old feedback instead of stacking noise

## Risks And Constraints

- answers are not truly hidden because notebook files are readable
- widget behavior depends on Jupyter support in the notebook environment
- some notebook renderers are weaker than Jupyter Lab for `ipywidgets`

Mitigation:

- target Jupyter Lab and VS Code notebook support first
- keep fallbacks simple
- avoid custom front-end extensions

## Authoring Checklist

- lesson goals are stated clearly
- each practice prompt has one expected answer format
- hint text is specific and useful
- widget labels are short and readable
- answer parser matches the requested format
- feedback tone is supportive

## Implementation Checklist

- create interactivity plan doc
- update repository docs to mention notebook interactivity
- add reusable widget helper module
- move lesson-specific checkpoint definitions out of the notebook
- prototype the helper in the first linear algebra notebook
- verify imports and notebook JSON validity

## Validation Checklist

- helper imports correctly inside the notebook
- `Check Answer` button triggers feedback
- numeric exercise accepts correct values
- vector exercise parses list input correctly
- dropdown exercise reports correct classification
- notebook still opens as valid JSON

## Next Expansion Ideas

- symbolic algebra checks with `sympy`
- tolerance checks for decimals
- optional hint button
- optional show-solution button
- shared notebook style guide for all future lessons
