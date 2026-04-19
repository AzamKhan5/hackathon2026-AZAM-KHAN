# ⚠️ Failure Modes & Handling

---

## 1. Tool Timeout / Failure

### Scenario
A tool (e.g. `get_order`) fails due to timeout.

### Handling
- `safe_call()` catches exception
- Logs failure
- Returns `None`
- Agent continues with fallback logic

### Outcome
System does NOT crash.

---

## 2. Missing Order ID

### Scenario
Customer does not provide order ID.

### Handling
- Agent attempts extraction
- If missing → asks for clarification

### Outcome
Customer prompted for required info.

---

## 3. Knowledge Base Failure

### Scenario
`search_knowledge_base` returns `None`.

### Handling
- Fallback to rule-based reasoning
- Avoid `.lower()` crash via safe checks

### Outcome
Agent still resolves ticket.

---

## 4. Invalid / Fraud Request

### Scenario
Customer claims premium privileges falsely.

### Handling
- Verify via `get_customer`
- Compare with policy

### Outcome
Request declined + flagged.

---

## 5. Refund Eligibility Failure

### Scenario
Refund check fails or returns false.

### Handling
- Do NOT issue refund
- Send explanation message

### Outcome
Safe financial operation.

---
