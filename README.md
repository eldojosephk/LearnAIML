# LearnAIML
Initial repo with AI ML projects
Below is a **step-by-step, keyboard-level guide** to build the **ApolloScan AG-UI + Next.js demo** **using VS Code and GitHub Copilot**, written exactly the way an **expert AI engineer / full-stack developer** would execute it.

This guide assumes:

* You are using **VS Code**
* You have **GitHub Copilot enabled**
* You want **Copilot to generate code safely**, not “hallucinate architecture”
* You want to end with a **GitHub Template repo + runnable Next.js demo**

---

# 🚀 Step-by-Step: Build ApolloScan AG-UI with VS Code + GitHub Copilot

---

## PHASE 0 — One-time setup (10 minutes)

### 0.1 Install prerequisites

* **Node.js 20+**
* **VS Code**
* **GitHub Copilot extension**
* (Optional) **GitHub CLI (`gh`)**

---

### 0.2 VS Code settings (important)

Open **VS Code → Settings → JSON** and ensure:

```json
{
  "editor.inlineSuggest.enabled": true,
  "github.copilot.enable": {
    "*": true
  },
  "editor.suggest.preview": true
}
```

This ensures Copilot suggestions appear inline and aggressively.

---

## PHASE 1 — Create the repo skeleton (NO Copilot yet)

### 1.1 Create folder

```bash
mkdir apolloscan-agui-template
cd apolloscan-agui-template
code .
```

---

### 1.2 Create folders manually (critical for Copilot accuracy)

In VS Code Explorer:

```
.github/workflows
.github
.template
docs
backend/events
backend/agents
backend/audit
backend/stream
ui/components
ui/hooks
ui/copilot
demo/server
demo/ui/app
demo/ui/components
demo/ui/hooks
demo/ui/styles
scripts
```

👉 **Do this manually**
Copilot performs much better when structure exists.

---

## PHASE 2 — Architecture lock (Copilot reads this)

### 2.1 Create `docs/ARCHITECTURE.md`

Paste this **yourself** (do not ask Copilot):

```md
ApolloScan AG-UI Architecture (LOCKED)

Rules:
1. Event-driven AG-UI architecture.
2. Immutable, append-only events.
3. UI is read-only by default.
4. Human actions are explicit + audit-logged.
5. CopilotKit is assistive only.
6. No UI-triggered backend mutations.
7. No score without reasoning + evidence.
```

💡 Copilot will now respect these constraints.

---

## PHASE 3 — Event contract (FIRST Copilot use)

### 3.1 Create `backend/events/aguiEvents.ts`

At the **top of the empty file**, type this prompt comment:

```ts
// Generate the canonical AG-UI event contract for ApolloScan.
// Requirements:
// - Versioned schema
// - Ordered events (sequenceNo)
// - Tamper-evident (prevHash, signature)
// - Include agent, finding, human action, audit events
// - No UI logic
```

👉 **Pause. Let Copilot generate.**
👉 Accept the suggestion.
👉 Manually compare with the “final contract” you already have (you now know what “good” looks like).

✔ Save file.

---

### 3.2 Create `backend/events/aguiEvent.schema.json`

Prompt at top:

```json
// Create JSON Schema for AG-UI events matching aguiEvents.ts.
// Enforce schemaVersion and required governance fields.
// Disallow additional properties.
```

Accept → save.

---

## PHASE 4 — Audit chain (Copilot with guardrails)

### 4.1 Create `backend/audit/auditLogger.ts`

Prompt:

```ts
// Implement an append-only, tamper-evident audit logger.
// Use chained hashes (prevHash → hash).
// Dev-friendly file storage, production-ready design.
```

Accept → save.

---

## PHASE 5 — CI + governance (Copilot shines here)

### 5.1 Create `.github/workflows/ci.yml`

Prompt:

```yaml
# Create a strict CI pipeline for an AG-UI repo.
// Requirements:
// - Node 20
// - lint + test
// - validate AG-UI schema
// - block UI mutation calls (POST/PUT/DELETE)
```

Accept → save.

---

### 5.2 Create `.github/copilot-instructions.md`

Paste **manually** (important):

```md
Copilot rules:
- Follow docs/ARCHITECTURE.md
- Do not introduce UI-triggered backend mutations
- Do not invent policy logic
- CopilotKit is assistive only
```

---

## PHASE 6 — AG-UI frontend (Copilot is now very effective)

### 6.1 Create `ui/hooks/useAgentEvents.ts`

Prompt:

```ts
// Create a resilient React hook to subscribe to AG-UI events via WebSocket.
// Requirements:
// - append-only events
// - reconnection with backoff
// - bounded memory
```

Accept → save.

---

### 6.2 Create `ui/components/AgentTimeline.tsx`

Prompt:

```tsx
// Read-only AG-UI component.
// Render agent progress strictly from AG-UI events.
// No user actions.
```

Accept → save.

---

### 6.3 Create `ui/components/ScoreCard.tsx`

Prompt:

```tsx
// Render readiness score.
// Only display score if reasoning + evidence events exist.
```

Accept → save.

---

## PHASE 7 — Next.js demo app (Copilot accelerates)

### 7.1 Create `demo/server/mockEventServer.ts`

Prompt:

```ts
// Create a mock AG-UI WebSocket server.
// Emit ordered, versioned demo events for a scan session.
```

Accept → save.

---

### 7.2 Create `demo/ui/package.json`

Paste manually (don’t prompt Copilot):

```json
{
  "private": true,
  "scripts": { "dev": "next dev" },
  "dependencies": {
    "next": "14.1.0",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  }
}
```

---

### 7.3 Create `demo/ui/app/layout.tsx`

Prompt:

```tsx
// Next.js App Router layout for AG-UI demo.
// Simple, professional layout.
```

Accept → save.

---

### 7.4 Create pages

* `demo/ui/app/page.tsx` → prompt: “Landing page with links”
* `demo/ui/app/leadership/page.tsx` → prompt: “Single-page executive AG-UI view”
* `demo/ui/app/scan/page.tsx` → prompt: “AG-UI scan timeline view”

Accept each.

---

## PHASE 8 — Run locally (confidence check)

### 8.1 Start mock server

```bash
cd demo/server
ts-node mockEventServer.ts
```

### 8.2 Start Next.js

```bash
cd demo/ui
npm install
npm run dev
```

Open: [http://localhost:3000](http://localhost:3000)

✔ You should see agent events streaming
✔ No UI mutations
✔ Leadership view is one screen

---

## PHASE 9 — GitHub check-in (with Copilot off)

```bash
git init
git add .
git commit -m "ApolloScan AG-UI template with Next.js demo"
```

Create GitHub repo → push → enable **Template repository**.

---

## 🧠 Expert rules while using Copilot

| Rule                    | Why                   |
| ----------------------- | --------------------- |
| One file = one prompt   | Avoids hallucinations |
| Architecture first      | Copilot obeys context |
| Never prompt for policy | Humans own governance |
| Review every suggestion | Copilot is junior     |
| CI enforces truth       | Humans make mistakes  |

---

## Final mental model

> **Copilot writes code.
> You design governance.
> AG-UI enforces trust.**

---

If you want, next I can:

* Add **CopilotKit explain panel** step-by-step
* Create **VS Code tasks.json** for one-click run
* Add **debug profiles** for WS + Next.js
* Provide a **15-minute internal workshop script**

Just tell me the next step.
