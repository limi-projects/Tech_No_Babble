# Flowcharts
In flowcharts, features are catgorised as nodes (e.g. boxes) or egdes (e.g. arrows).
Flowchart orintations are declared using TD (top-down), TB (top-bottom), BT (Bottom-top), RL (Right-Left), LR (Left-Right)

---
```mermaid
---
title: Flowchart Title
---
flowchart TD
    NODE1 --> NODE2
```
---

## Box Types
```mermaid

flowchart TD
  NODE[Rectangle] --> NODE(Rounded Edges)
  NODE([Stadium])
  NODE[[Subroutine]]
  NODE[(Database)]
  NODE((Circle))
```

```mermaid
flowchart LR
  A e1@==> B
  e1@{ animate: true }
```
