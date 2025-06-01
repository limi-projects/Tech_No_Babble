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
  A--> B[Rectangle]
  B--> C(Rounded Edges)
  C--> D([Stadium])
  D--> E[[Subroutine]]
  E--> F[(Database)]
  F--> G((Circle))
```

## Mind Maps
```mermaid
mindmap
      root(Candidate Material))
        Photovoltage
            Defects
            Polarons
            Dielectric Properties
            Electrode-Electrolyte Interactions
            Material-Material Interactions
        Band Gap
            Eigenvalues
            Phonons 
        Band Alignment
            Ionisation Potential
            Electron Affinity
        Corrosion Resistance
            Side Reactions
            Electrolyte pH
        Catalytic Activity
            Rate Constants
            Activation Enthalpy
        Catalytic Selectivity
            Side Reaction Enthalpies
```
