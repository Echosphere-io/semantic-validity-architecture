# The Architecture

**Six constraints. Three axes. One criterion for semantic validity.**

---

## The Core Claim

Any semantically complete claim must satisfy exactly six constraints. Not approximately. Not usually. Exactly six.

Fewer than six and the claim has gaps—places where it can fail without warning.

This isn't theory. It's geometry.

---

## The Six Constraints

| # | Constraint | Question | Function |
|---|------------|----------|----------|
| 1 | **Referential** | WHAT is being claimed? | Establishes determinate content |
| 2 | **Contextual** | Under what CONDITIONS? | Specifies scope and applicability |
| 3 | **Premissive** | On what GROUNDS? | Provides warrant and support |
| 4 | **Inferential** | WHY does this follow? | Shows logical connection |
| 5 | **Constraining** | What are the LIMITS? | Defines boundaries and exclusions |
| 6 | **Teleological** | What is this FOR? | Establishes purpose and relevance |

Every valid claim answers all six. Every invalid claim is missing at least one.

---

## Why Six?

Consider the simplest three-dimensional enclosure: a tetrahedron.

```
               ◆ (Purpose)
              /|\
             / | \
            /  |  \
           /   |   \
          /    |    \
    (Grounds) ◆─────◆ (Limits)
          \    |    /
           \   |   /
            \  |  /
             \ | /
              \|/
               ◆ (Subject)
```

- **4 vertices** — the components being related
- **6 edges** — the relations between them
- **4 faces** — the surfaces that enclose

Remove any edge and the structure collapses. It no longer bounds a volume. It's no longer closed.

Semantic validity works the same way. The six constraints are the six edges. Remove any one and meaning leaks out—the claim can be true in ways you didn't intend, false in ways you can't detect.

This isn't metaphor. It's the minimum structure for closure. Known for 2,400 years. Applied here.

---

## The Three Axes

Every claim exists in a three-dimensional space:

```
                    USER
                   (who's asking)
                      │
                      │
                      ▼
        SUBJECT ◄────►◄────► METHOD
      (what's claimed)      (how it's derived)
```

| Axis | What It Tracks | Why It Matters |
|------|----------------|----------------|
| **USER** | Who's asking, expertise level, intent | Same answer isn't right for everyone |
| **SUBJECT** | What's being discussed, certainty level | Different topics require different rigor |
| **METHOD** | Inference type, confidence warranted | Deduction ≠ speculation |

Current systems flatten this to one axis: input → output.

Valid systems track all three throughout processing.

---

## Constraint Specification

### Constraint 1: Referential (WHAT)

**Question:** Is the claim determinate? Can you point to what it's about?

**Passes when:**
- The subject is identifiable
- Terms are defined or definable
- Reference is stable (doesn't shift meaning)

**Fails when:**
- Subject is vague ("things," "stuff," "it")
- Terms are ambiguous without clarification
- Reference drifts across the conversation

**Implementation:** Entity tracking, term anchoring, reference resolution

---

### Constraint 2: Contextual (CONDITIONS)

**Question:** Under what circumstances does this hold?

**Passes when:**
- Scope is specified (always? sometimes? here?)
- Conditions are stated (if X, then Y)
- Exceptions are acknowledged

**Fails when:**
- Universal claims without warrant ("always," "never," "everyone")
- Conditions unstated or assumed
- Context-dependence hidden

**Implementation:** Scope tagging, conditional extraction, assumption surfacing

---

### Constraint 3: Premissive (GROUNDS)

**Question:** What supports this claim? Why believe it?

**Passes when:**
- Sources are cited or citable
- Reasoning chain is traceable
- Authority is appropriate to claim

**Fails when:**
- Asserted without support
- Grounds don't match claim type (opinion vs. fact)
- Circular reasoning

**Implementation:** Source tracking, warrant classification, evidence linking

---

### Constraint 4: Inferential (WHY)

**Question:** Does the conclusion follow from the premises?

**Passes when:**
- Logical connection is valid
- Inference type is appropriate
- Steps are traceable

**Fails when:**
- Non-sequitur (conclusion doesn't follow)
- Wrong inference type (treating correlation as causation)
- Missing steps

**Implementation:** Inference typing, validity checking, gap detection

---

### Constraint 5: Constraining (LIMITS)

**Question:** What does this NOT claim? Where does it stop?

**Passes when:**
- Boundaries are explicit
- Exclusions are stated
- Overclaiming is prevented

**Fails when:**
- Claim expands beyond warrant
- Limits unstated
- Edge cases ignored

**Implementation:** Boundary detection, negation handling, scope limiting

---

### Constraint 6: Teleological (PURPOSE)

**Question:** What is this claim FOR? Why does it matter?

**Passes when:**
- Purpose is clear
- Relevance is established
- Fit to user need is checked

**Fails when:**
- Pointless precision (correct but irrelevant)
- Purpose mismatch (answering the wrong question)
- Missing "so what?"

**Implementation:** Intent matching, relevance scoring, purpose alignment

---

## The Validation Process

```
┌─────────────────────────────────────────────────────┐
│                 GENERATED OUTPUT                    │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│              SIX-CONSTRAINT VALIDATOR               │
├─────────────────────────────────────────────────────┤
│  □ Referential — Is it determinate?                │
│  □ Contextual — Are conditions specified?           │
│  □ Premissive — Are grounds provided?               │
│  □ Inferential — Does it follow?                    │
│  □ Constraining — Are limits acknowledged?          │
│  □ Teleological — Is purpose clear?                 │
└───────────────────────┬─────────────────────────────┘
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
   ┌─────────────┐            ┌─────────────┐
   │   6/6 PASS  │            │  <6 FAIL    │
   │             │            │             │
   │   Output    │            │   Revise    │
   │   as valid  │            │   or refuse │
   └─────────────┘            └─────────────┘
```

Claims that fail any constraint have three options:
1. **Revise** — Fix the missing constraint
2. **Hedge** — Acknowledge the incompleteness explicitly
3. **Refuse** — Decline to output until constraint can be satisfied

Option 3 is a feature, not a failure. A system that refuses when it shouldn't answer is more trustworthy than one that always produces output.

---

## Inference Type Discrimination

Not all inferences are equal. The architecture tracks four types:

| Type | Operation | Confidence | Marker |
|------|-----------|------------|--------|
| **Deduction** | Necessary conclusion from premises | Certain (if valid) | "This follows necessarily..." |
| **Induction** | Generalization from instances | Probable | "Evidence suggests..." |
| **Abduction** | Inference to best explanation | Plausible | "The best explanation is..." |
| **Interpolation** | Pattern completion from structure | Recognition-dependent | "This appears consistent with..." |

Current systems conflate all four. They output "X is true" whether X was deduced, induced, guessed, or hallucinated.

The architecture requires tagging. Users know what kind of inference produced the claim.

---

## State Tracking

The system maintains explicit state across three axes:

```python
class SemanticState:
    # USER axis
    user_intent: Intent          # What do they want?
    user_expertise: Level        # What can they understand?
    user_mode: Mode              # Learning? Deciding? Exploring?
    
    # SUBJECT axis  
    domain: Domain               # What area?
    certainty: Certainty         # Settled? Contested? Unknown?
    key_terms: TermRegistry      # Anchored definitions
    
    # METHOD axis
    inference_type: InferenceType  # How was this derived?
    confidence: Confidence         # How sure should we be?
    limitations: Limitations       # What can't this method tell us?
```

State persists across turns. Drift is detected by comparing current usage against anchored terms.

---

## Closure Authority

Not every output should be finalized by the system. The architecture includes a closure registry:

| Output Type | Closure Authority |
|-------------|-------------------|
| Factual lookup | System closes |
| Calculation | System closes |
| Creative generation | System closes |
| Medical advice | Human review |
| Legal determination | Human closes |
| Ethical judgment | Human closes |
| Safety-critical | Human closes |
| Uncertainty | Explicit hedge |

The system routes outputs to appropriate closure. It doesn't decide what humans should decide.

---

## Implementation Layers

Six layers, building on each other:

| Layer | Function | Dependency |
|-------|----------|------------|
| **1. Validity Filter** | Check six constraints on output | Foundation |
| **2. State Tracking** | Maintain user/subject/method representation | Enables 3-5 |
| **3. Inference Typing** | Classify and tag inference type | Requires 2 |
| **4. Drift Detection** | Anchor terms, detect shift | Requires 2 |
| **5. Closure Routing** | Route to appropriate authority | Requires 2 |
| **6. Integration** | Cross-layer optimization | Requires 1-5 |

Layer 1 provides immediate value—it can be added as a post-processing filter without retraining.

Layers 2-5 require architectural integration but produce compounding improvement.

---

## What This Is Not

**This is not a complete AI system.** It's a validity layer—architecture that can be integrated with existing or future systems.

**This is not prompt engineering.** It's structural change to how outputs are generated and validated.

**This is not fine-tuning.** It's capability that must be built in, not trained in.

**This is not alignment.** It's a precondition for alignment—you can't align a system that doesn't know what it knows.

---

## What This Is

A criterion.

For the first time, you can ask: "Is this output semantically valid?"

And have a structural answer—not a probability, not a vibe, but a checklist of six constraints either satisfied or not.

Claims that pass are complete. Claims that fail are caught.

That's the architecture.

---

## What This Is For

Beyond the technical utility, this architecture serves a larger purpose.

We're building human-AI systems whether we have a framework for them or not. Floridi calls the emerging hybrid an "Inforg"—part information, part organism. But his version risks the human becoming a node in an information network.

The architecture keeps the hierarchy straight:
- **Human** as the end (whose improvement matters)
- **AI** as the means (whose validity matters)
- **Improvement** as the criterion (not mere information transfer)

The guitar doesn't make you a musician by giving you music. It makes you a musician by developing your capacity to make music. AI should work the same way—extending human capability while developing human capacity.

The six constraints ensure AI outputs are valid. The three-axis tracking ensures they serve the user's genuine needs. The closure authority ensures humans remain in charge.

This is the philosophy of human-AI combination that's been missing. The architecture implements it.

---

## Technical Integration

The architecture integrates at three points:

| Integration Point | Method | Impact |
|-------------------|--------|--------|
| **Post-generation** | Filter outputs before delivery | Catches invalid claims |
| **Context management** | Enrich input with state tracking | Enables calibration |
| **Training objective** | Add validity signal to loss function | Bakes in structure |

Post-generation filtering is fastest to implement. Training integration produces deepest improvement.

---

## Patent Coverage

Seven patent families protect this architecture:

| Family | Coverage |
|--------|----------|
| A | Tetrahedral validity structure |
| B | Form-preserving memory |
| C | Inference discrimination |
| D | Semantic state signaling |
| E | Constraint governance |
| F | Closure authority |
| G | Integrated system |

Provisionals filed. Full specifications available under NDA.

---

## Next Steps

1. **Review THE_PROOF.md** — See how this dissolves known problems
2. **Study THE_VOCABULARY.md** — Learn the precise terms
3. **Contact for integration** — The Themis Project (themis@echosphere.io)

---

```
Six constraints.
Three axes.
One criterion.

Valid or not. Now you can tell.
```
