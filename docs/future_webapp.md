# Future Webapp Idea

This repo may later grow into a math learning webapp.

## Product Concept

Students receive structured lesson material, complete tasks, receive automated assessment, and can ask for agent-guided corrections and explanations through an API call.

## Learning Flow

1. Student opens a lesson.
2. Student reads concept material and worked examples.
3. Student completes exercises.
4. The app checks objective answers automatically where possible.
5. For conceptual answers or mistakes, the app sends context to an agent.
6. The agent responds with hints, corrections, and targeted follow-up practice.
7. The student progress model updates mastery for the relevant skills.

## Future Components

- Lesson authoring format
- Exercise bank with metadata
- Student answer capture
- Automatic grading for numeric and symbolic tasks
- Agent feedback API
- Mastery tracking by concept
- Notebook-to-web content export
- Teacher/admin review tools

## Design Principle

The agent should not simply give answers. It should diagnose the student model, explain the specific misconception, and give the smallest helpful hint before escalating to a full solution.

