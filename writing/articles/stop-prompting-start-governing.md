# Stop Prompting. Start Governing.

| | |
|---|---|
| **Author** | [@0xloria](https://x.com/0xloria) |
| **Published** | 2026-06-10 |

Everywhere I look, the AI chatter is about how fast a prompt can spin up an app. Speed was never the hard part.

So I stopped chasing it. Instead I'm building environments. Specifications. Memory. Specialization. Review gates. Feedback loops.

The real question isn't "How do I get Claude to write code?"

It's "How do I build a software organization made of agents?"

## 🔧 The fundamental mistake

Open Claude Code and start prompting.

Build me auth. Add a dashboard. Fix this bug.

The results are often impressive. They're rarely consistent.

Why? Claude is missing the thing that matters most. Context.

It doesn't know your architecture. Your business rules. Your security requirements. Your deployment strategy. Your coding standards.

Not unless you teach it.

That leads to the core principle of agentic development:

*An agent can only obey constraints that exist.*

Undocumented requirements don't exist.
Undocumented architecture doesn't exist.
Undocumented security policy doesn't exist.

The agent can only reason over what it can see.

## 🐛 Most bugs are communication failures

Software engineering has always been compression.

Requirements compress into architecture. Architecture into code. Code into tests and deployment.

Most bugs aren't coding failures. They're losses somewhere in that chain.

Claude works the same way.

Better information in, better output out. The prompt isn't the lever. The information architecture is.

## 📄 Four documents before any code

A repo built for agents starts with four files:

```
├─ README.md
├─ CLAUDE.md
├─ docs/SRS.md — requirements
└─ docs/SDD.md — design
```

Yes, two of those acronyms smell like an old CS classroom. That's the point.

We stopped writing specs because they were expensive and went stale fast. Agents changed the math.

A spec is now the cheapest file in the repo. It's also the only one read in full before every task. We're writing things down again because the documents finally do work.

The **SRS** says what to build. Business rules. User stories. Acceptance criteria. Plus the requirements nobody states until they're violated:

- Accounts lock after 5 failed attempts
- Login p95 under 200ms at 10,000 users
- JWTs expire in 15 minutes
- Passwords hashed with Argon2

The **SDD** says how and why. The architecture. The tech choices. The options you already rejected.

An agent proposes MongoDB. Your SDD explains why you picked Postgres. That argument is already over. You don't re-fight it every session.

The **README** says how to run it. Setup. Tests. Deployment. Humans read it. Agents read it. New hires of both kinds read it.

**CLAUDE.md** says how we work here. This one needs its own section.

## 🧠 CLAUDE.md is institutional memory

Most people treat CLAUDE.md as documentation. It isn't.

It's the knowledge that normally lives in the project manager's heads. Written down. Visible to every agent on every task.

A real one looks like this:

**Architecture** — Business logic lives in the service layer. Controllers translate HTTP and nothing else. All DB access goes through repositories.

**Security** — user_id comes from the JWT, never the client. Never log request bodies, auth payloads leak that way. Validate all input at the boundary.

**Testing** — No tests, no review. Integration tests run against real Postgres, not mocks. Mocked databases hide the bugs we actually ship.

**Forbidden** — No business logic in React components. No PRs over 500 lines.

Notice the pattern. Every rule carries a reason.

An agent that knows only *what* will lawyer the letter of the rule. An agent that knows *why* generalizes to the cases you didn't write down.

And notice what we're doing. We're not prompting anymore.

We're governing.

## 🏭 One craftsman vs. the pin factory

Most people use Claude like a single hire asked to do everything. Build it. Test it. Secure it. Architect it. Document it. Ship it.

Nobody staffs a real team that way.

Adam Smith called this out in 1776. One worker making whole pins produces a handful a day. Ten workers, each owning one step -> [draw, straighten, cut, sharpen, head] -> produce tens of thousands.

The workers didn't get smarter. The work got divided.

Specialized agents win for the same reason. Smaller context. One job. A clear definition of done.

The **implementation** agent builds features and fixes bugs.

The **testing** agent writes the tests and hunts edge cases.

The **security** agent checks the OWASP Top 10, auth flows, and secrets.

One job means sharp output:

> ⚠ HIGH RISK: user_id supplied by the client. Privilege escalation risk. Derive it from the JWT instead.

But none of them work alone. Every agent reads the same CLAUDE.md.

That shared memory is the difference. It turns five agents into one organization, not five freelancers.

## 🛠 Skills teach thinking. MCP gives hands.

People mix these up. They're different layers.

A **skill** is reusable expertise. Write your security checklist once: auth, authorization, input, secrets, dependencies. Every future review inherits it.

**MCP** is access. Without it, Claude can only reason about your systems. With it, Claude can read the database, pull the ticket, check the logs, query the API.

The agent stops watching your org and starts working in it.

## ⚙️ Harness engineering: the factory around the worker

Most AI talk is about the model. The real gains come from the system around it.

The model is the worker. The harness is the factory.

The harness decides which agent runs. What context it gets? What tools it can touch? What checks fire? What needs a human?

A mature workflow looks like CI/CD with judgment gates:

```
Feature request
↓
Spec + design doc  ·  human reviewed
↓
Implementation agent
↓
Testing agent
↓
Security agent
↓
Human approval
↓
Merge
✅
```

Failures loop back. Success moves forward.

Note where architecture review sits. At the design doc, before any code exists. The point where changing your mind is still cheap.

Every stage runs the same triad. The agent acts. The human verifies. The harness enforces.

Quality stops being a function of the prompt. It becomes a function of the harness.

## 📦 Small batches beat one-shot generation

Most failures come from oversized requests.

✗ Bad: "Build a trading platform."
✓ Good: schema → auth → accounts → orders → matching engine → reporting

Same reason small PRs beat big ones. Tighter reasoning. Easier review. Lower risk. Faster feedback.

## 📈 The bottleneck moves. It doesn't disappear.

People assume AI shrinks the value of software engineering. The opposite is true.

As code gets cheap, everything around it gets expensive. Requirements. Architecture. Security. Review. Systems thinking.

The Industrial Revolution wasn't powered by better craftsmen. It was powered by better systems.

*Old world: the engineer writes code.*
*New world: the engineer designs the organization that writes it.*

The question is no longer "Can the AI write code?"
It's "Can the system reliably produce software?"

The teams that answer first get a compounding edge. And it all rests on one line:

*An agent can only obey constraints that exist.*

That's why specs matter. Why architecture matters. Why memory matters. Why review matters.

And why engineering discipline matters more in the age of AI, not less.

**Code is becoming abundant. Judgment is becoming scarce.**

I'm documenting the shift from writing code to designing the systems that write it. Follow along if you're building in the same direction.

— [@0xloria](https://x.com/0xloria)
