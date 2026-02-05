Intelligent Systems with LangChain and LangGraph
Free book
<br>
<H1><b>Contacts</b></H1>
<h2><b>email: alexciambrone@gmail.com</b></h2>
<br>
<h2><b>linkedin: https://www.linkedin.com/in/alessandrociambrone/</b></h2>

# About this book

Large language models are now good enough to be useful in real products — and still unreliable enough to be dangerous if you treat them like normal software components. They can write fluent answers, follow instructions (mostly), and adapt to many tasks. They can also hallucinate, miss constraints, break output formats, and confidently do the wrong thing at the worst possible moment.

If you’ve built anything beyond a toy demo, you’ve already felt the tension: the model is powerful, but the system around it is where success or failure is decided.

This book is about that surrounding system. It treats LLMs as one component inside an application: a decision-and-generation engine that needs scaffolding. That scaffolding includes retrieval, tools, state, control flow, error handling, and evaluation. The goal isn’t clever prompts. The goal is intelligent systems that are debuggable, auditable, and maintainable — systems you can run in production without relying on hope as an engineering strategy.

## What this book focuses on

The practical focus is the Lang ecosystem:

- **LangChain** for composing model calls, retrieval, prompts, tools, and parsing into repeatable pipelines.
- **LangGraph** for turning those pipelines into explicit, stateful workflows with branching, loops, concurrency, checkpoints, and human-in-the-loop steps.
- **LangSmith** for tracing, datasets, evaluation, and monitoring — so behavior becomes something you can measure and improve, not something you argue about after an incident.

You can build LLM applications without these libraries. You can also build a distributed system without a framework — people do. The point of Lang is to make the “boring but critical” parts easier: standard interfaces, composable components, visible execution, and the feedback loop that turns experiments into engineering.

## The scenarios you’ll see throughout

To keep the material grounded, the examples aren’t random one-off demos. They’re reframed into a small set of realistic scenarios that show up repeatedly:

- A **customer support assistant** that answers from policy and knowledge bases, follows escalation rules, and stays within safe boundaries.
- An **e-commerce assistant** that handles product search, recommendations, and order-related workflows.
- A **trading and market analysis assistant** that turns noisy market and news inputs into structured analysis and explanations.

These scenarios are chosen because they force the issues that matter: context limits, retrieval quality, tool reliability, state management, and evaluation. When you see the same domains across chapters, it’s not for storytelling flair — it’s to show how the same primitives (retrievers, graphs, checkpoints, evaluators) compose into larger systems over time.

## How the book progresses

The book starts with foundations: what models are, where they fail, and why failures are predictable enough to engineer around. It then moves from “single-call prompts” into real application design: context construction, retrieval patterns, output parsing, and defensive techniques that keep systems stable under messy inputs and partial failures.

From there, it introduces the shift from **chains to graphs**. Once you need branching, loops, retries, parallel work, or human approval, straight-line workflows become fragile and hard to reason about. LangGraph makes control flow explicit and makes state and persistence first-class, so long-running workflows remain manageable.

## Two threads that run through everything

**Agentic does not mean uncontrolled.**  
An agent is best understood as a goal-directed control loop with an LLM in the decision seat. That loop is only safe when you define what the system can observe, what tools it can use, what it should remember, and what stops it. You’re not replacing software engineering with vibes — you’re choosing where to put the model and how tightly to constrain it.

**Context limits are real engineering constraints.**  
Long documents, long conversations, and long-running jobs don’t fit neatly into one prompt. This book treats “short-context strategies” as engineering patterns, not tricks: trimming, summarization, map–reduce workflows, and graph-shaped pipelines for long documents and video-like inputs. These strategies are expensive in different ways — tokens, latency, complexity — so we focus on trade-offs and on keeping intermediate artifacts visible so failures can be traced.

## Evaluation and governance are part of the build

Evaluation isn’t an afterthought. Once you can trace runs, promote edge cases into datasets, and run evaluations when you change prompts, retrieval, tools, or models, quality becomes something you can iterate on systematically.

That discipline matters because LLM systems drift: providers change models, your data changes, and user behavior changes. If you don’t measure, you will eventually ship a regression with a smile.

## Who this is for

This is a practical book for working engineers. You don’t need to be a machine learning researcher. You do need the willingness to treat LLM behavior as something to constrain, observe, and test — like any other component that can fail.

If you approach the material with that mindset, you’ll come away with reusable patterns for building agent-based systems that can survive contact with reality.

