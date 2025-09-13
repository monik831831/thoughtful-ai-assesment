# thoughtful-ai-assesment Package Sorting Function

# Overview
This project implements a Python function that simulates how a robotic arm classifies and dispatches packages in an automated warehouse.  
The function determines whether a package is STANDARD, SPECIAL, or REJECTED based on its dimensions and mass.

---

## Rules

A package is considered:

- Bulky if:
  - Volume (`width × height × length`) is ≥ 1,000,000 cm³, or
  - Any single dimension is ≥ 150 cm  
- Heavy if:
  - Mass is ≥ 20 kg

### Dispatch Stacks
- STANDARD → Neither bulky nor heavy  
- SPECIAL → Either bulky or heavy (but not both)  
- REJECTED → Both bulky and heavy  

---

## Installation & Setup
Clone the repository and navigate into it:

```bash
git clone https://github.com/your-username/package-sorter.git
cd package-sorter
