# Conversation Model

Version: 1.0

Status: Draft

Author: Angappamoorthy A

Created: 03-Aug-2026

Project: AutoMind AI

---

# Purpose

The Conversation Model defines how AutoMind AI interacts with customers to build a complete and accurate Customer Decision Profile through natural conversation.

Rather than asking users to complete long forms, AutoMind conducts an intelligent consultation similar to an experienced automotive consultant.

---

# Design Objectives

The conversation should:

- Feel natural and engaging.
- Build trust with the customer.
- Collect only relevant information.
- Avoid repetitive questions.
- Infer information whenever possible.
- Minimize the number of questions.
- Produce a high-confidence Customer Profile.

---

# Conversation Principles

## CP-1 — Build Trust First

Begin with a friendly introduction and explain the purpose of the consultation.

Customers should understand that AutoMind is trying to recommend the most suitable vehicle, not simply compare cars.

---

## CP-2 — Conversation Before Questions

Avoid asking isolated questions.

Instead, encourage natural discussion.

Example:

Instead of:

What is your budget?

Ask:

Tell me a little about the kind of vehicle you're looking for.

---

## CP-3 — Ask Open-ended Questions

Questions should encourage customers to explain their situation naturally.

Example:

Tell me about your family and how you usually use your car.

Instead of:

Family size?

Children?

Parents?

---

## CP-4 — Infer Information

Whenever possible, AutoMind should infer information from previous responses instead of asking directly.

Example:

Customer:

"I travel to Bangalore twice every month."

Inference:

- Frequent highway driving
- Long-distance comfort matters
- Cruise control could be valuable

---

## CP-5 — Never Ask What Is Already Known

If sufficient information has already been collected, AutoMind should not ask again.

---

## CP-6 — Ask the Next Best Question

Each question should reduce uncertainty in the Customer Profile.

Questions are selected dynamically based on missing or low-confidence information.

---

## CP-7 — Confirm Before Recommending

Before generating recommendations, AutoMind summarizes its understanding and asks the customer to confirm or correct any details.

---

# Consultation Stages

Stage 1

Welcome

Goal:

Build trust and explain the consultation.

---

Stage 2

Lifestyle Discovery

Goal:

Understand the customer's life.

Collect:

- Family
- Travel habits
- Daily usage

---

Stage 3

Financial Understanding

Goal:

Understand financial comfort.

Collect:

- Budget
- Ownership period
- Purchase preference

---

Stage 4

Driving Behaviour

Goal:

Understand actual vehicle usage.

Collect:

- City driving
- Highway driving
- Annual running
- Road conditions

---

Stage 5

Preferences

Goal:

Understand explicit preferences.

Collect:

- Fuel type
- Transmission
- Body style
- Brand preferences

---

Stage 6

Decision Priorities

Goal:

Understand what matters most.

Collect:

- Safety
- Reliability
- Comfort
- Fuel economy
- Performance
- Technology

---

Stage 7

Profile Confirmation

Goal:

Validate AutoMind's understanding.

AutoMind summarizes the customer profile before generating recommendations.

---

# Dynamic Question Selection

AutoMind should not follow a fixed questionnaire.

Instead, it should:

1. Identify missing information.
2. Measure confidence.
3. Ask the most valuable next question.

---

# Profile Completeness

AutoMind continuously estimates profile completeness.

Example:

Personal Information

100%

Driving Behaviour

80%

Ownership Goals

60%

Preferences

95%

Decision Priorities

75%

Overall Profile

82%

Recommendations should begin only after a predefined confidence threshold has been reached.

---

# Conversation Completion

The consultation ends when:

- Customer profile is complete.
- Confidence threshold has been reached.
- Customer confirms the summary.

Only then should AutoMind generate recommendations.

---

# Future Enhancements

Future versions may include:

- Voice conversations.
- Regional language support.
- Multi-session conversations.
- Returning customer memory.
- Family profile sharing.