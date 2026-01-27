# The Vocabulary

**Terms for implementing and discussing semantic validity**

---

## Why This Matters

Precise vocabulary enables precise implementation. These terms have specific meanings in this architecture. Using them consistently prevents confusion.

This isn't jargon for its own sake. Each term names something you need to build or check.

---

## Core Architecture Terms

### The Three Axes

Every claim exists in three-dimensional semantic space:

```
                    USER
                      │
                      │
        SUBJECT ◄─────┼─────► METHOD
```

**User**
: Who is asking, their expertise level, their intent. The same answer isn't right for everyone. A medical professional asking about drug interactions needs different depth than a curious layperson.

**Subject**
: What is being discussed, its certainty level, its domain. Some things are settled science; some are active debate; some are unknown. The system should know which.

**Method**
: How the claim was derived, what inference type was used, what confidence is warranted. Deduction from premises differs from pattern-matching against training data.

**Three-axis tracking**
: Maintaining explicit representation of User, Subject, and Method throughout processing. Current systems flatten to one axis (input → output). Valid systems track all three.

---

### The Six Constraints

Every valid claim satisfies six constraints:

**Referential (WHAT)**
: The claim has determinate content. You can point to what it's about. Fails when subject is vague, ambiguous, or shifts meaning.

**Contextual (CONDITIONS)**
: Scope and applicability are specified. The claim states when and where it holds. Fails when universalizing without warrant ("always," "never," "everyone").

**Premissive (GROUNDS)**
: Support is provided. The claim rests on something—evidence, reasoning, authority appropriate to the claim type. Fails when asserted without warrant.

**Inferential (WHY)**
: The conclusion follows from the premises. The logical connection is valid. Fails on non-sequiturs, gaps in reasoning, wrong inference type.

**Constraining (LIMITS)**
: Boundaries are explicit. The claim says what it does NOT cover. Fails when overclaiming, ignoring edge cases, or unstated assumptions.

**Teleological (PURPOSE)**
: Purpose is clear. The claim matters for a reason; it connects to user need. Fails on pointless precision or purpose mismatch.

**Closure**
: When all six constraints are satisfied. The claim is semantically complete. Before closure, gaps exist where the claim can fail silently.

**Incomplete**
: Missing one or more constraints. Most outputs from current systems are incomplete—they satisfy some constraints by accident, not design.

---

### Validity Terms

**Valid**
: Satisfies all six constraints. The claim is structurally complete. Note: valid ≠ true. A valid claim can be false if premises are wrong. But validity is checkable; truth often isn't.

**Invalid**
: Missing constraints. The claim has structural gaps. Invalid claims should be revised, hedged, or refused—not output as if complete.

**Validation**
: The process of checking constraints. A validator examines each constraint and reports pass/fail.

**Revision**
: Fixing an invalid claim by supplying missing constraints. The system attempts to complete the claim before output.

**Refusal**
: Declining to output when constraints cannot be satisfied. Refusal is a capability, not a failure. A system that refuses appropriately is more trustworthy than one that always outputs.

---

### Inference Types

**Deduction**
: Necessary conclusion from premises. If premises are true and form is valid, conclusion must be true. Highest confidence when applicable. Marker: "This follows necessarily..."

**Induction**
: Generalization from instances. More evidence = higher confidence, but never certainty. Marker: "Evidence suggests..." or "In N cases observed..."

**Abduction**
: Inference to best explanation. Selects most plausible explanation from alternatives. Lower confidence; flag as reasoned guess. Marker: "The best explanation appears to be..."

**Interpolation**
: Pattern completion from structural similarity. The system recognizes a familiar structure and projects missing elements. Confidence depends on structural match. Marker: "This appears consistent with..."

**Inference discrimination**
: Tagging outputs with their inference type. Users can then calibrate trust appropriately. Current systems conflate all types.

---

### State Terms

**Semantic state**
: Explicit representation of User, Subject, and Method maintained across turns. Includes established facts, key term definitions, acknowledged constraints, open questions.

**Term anchoring**
: Recording a term's meaning when first established. Later uses are checked against the anchor. Prevents drift.

**Drift**
: When meaning shifts from anchored definition without explicit acknowledgment. Detected by comparing current usage against anchor.

**Drift detection**
: Checking for semantic drift and flagging before it compounds. The system asks for clarification rather than silently shifting meaning.

---

### Closure Authority Terms

**Closure authority**
: Who or what has the right to finalize a claim. Not all claims should be finalized by the system.

**System closes**
: The system can finalize this output. Appropriate for factual lookups, calculations, creative generation.

**Human review**
: The system outputs but flags for human verification. Appropriate for medical, legal, financial information.

**Human closes**
: The system presents options but does not conclude. Human makes final determination. Appropriate for value judgments, life decisions, ethical questions.

**Routing**
: Directing outputs to appropriate closure authority based on claim type.

---

## Implementation Terms

**Validator**
: Component that checks the six constraints on outputs. Can be post-generation (filter) or integrated (during generation).

**State tracker**
: Component that maintains semantic state across turns. Updates on input, checks output against established state.

**Inference tagger**
: Component that classifies inference type and attaches appropriate confidence markers.

**Drift detector**
: Component that maintains term anchors and checks for deviation.

**Closure router**
: Component that classifies output type and routes to appropriate authority.

**Validity layer**
: The integrated system of validator, state tracker, inference tagger, drift detector, and closure router.

---

## Failure Mode Terms

**Hallucination**
: Confident assertion without grounds. Maps to missing Premissive and Inferential constraints.

**Semantic drift**
: Undetected meaning shift. Maps to missing Referential tracking.

**Groundless confidence**
: Certainty without warrant. Maps to missing Premissive and Constraining constraints.

**Calibration failure**
: Stated confidence ≠ actual accuracy. Maps to missing inference discrimination.

**Inappropriate closure**
: System decides what humans should decide. Maps to missing closure routing.

**Context degradation**
: Coherence dissolves over long conversations. Maps to missing semantic state tracking.

---

## Historical Terms

These terms come from the logical tradition that first identified the six-constraint structure. You don't need the history to implement the architecture, but you may encounter these terms in the full documentation.

**Telos** (Greek: τέλος)
: Purpose, goal, end. What something is FOR. The sixth constraint (Teleological) is named for this.

**Form**
: Structure that makes something what it is. The validity architecture is a form—a structure that makes claims valid.

**Hylomorphism**
: The view that things have both structure (form) and substrate (matter). In this context: outputs have both content (matter) and validity structure (form).

**Phronesis** (Greek: φρόνησις)
: Practical wisdom—knowing what to do in particular situations. What the architecture aims to support in AI systems.

---

## Quick Reference

| Term | One-Line Definition |
|------|---------------------|
| User | Who's asking, expertise, intent |
| Subject | What's discussed, certainty level |
| Method | How derived, inference type |
| Referential | WHAT—determinate content |
| Contextual | CONDITIONS—scope specified |
| Premissive | GROUNDS—support provided |
| Inferential | WHY—conclusion follows |
| Constraining | LIMITS—boundaries explicit |
| Teleological | PURPOSE—relevance clear |
| Valid | All six constraints satisfied |
| Closure | Semantic completeness |
| Refusal | Declining when constraints unsatisfiable |
| Hallucination | Assertion without grounds |
| Drift | Undetected meaning shift |

---

## Usage

When building:
- Check outputs against the six constraints
- Track state explicitly
- Tag inference types
- Route closure appropriately

When discussing:
- Use terms precisely
- Distinguish constraint types
- Name failure modes by their constraint mapping

When evaluating:
- Count which constraints are checked
- Identify which failures are caught
- Measure improvement against baseline

---

## The Purpose of Precision

Why does precise vocabulary matter?

Because we're building human-AI systems that need a framework. And frameworks require shared language.

The hierarchy is:
- **Human** as the end (whose improvement matters)
- **AI** as the means (whose validity matters)
- **Improvement** as the criterion (not mere capability)

Every term in this vocabulary serves that hierarchy. "Closure" means the human can trust the output. "Refusal" means the system protects the human from bad information. "Calibration" means the human can make decisions with accurate confidence estimates.

The guitar doesn't make you a musician by transferring music. It develops your capacity to make music.

AI with valid outputs doesn't make you knowledgeable by transferring information. It develops your capacity to understand.

Precise vocabulary enables precise implementation. Precise implementation enables genuine improvement.

---

```
Vocabulary is infrastructure.

Use these terms precisely and implementation follows.
```
