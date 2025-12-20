---
title: system design
---

## system design


## Lifecycle

- Business Requirements
- System Requirements
    - https://www.perforce.com/blog/alm/how-write-software-requirements-specification-srs-document
- Design doc
- Implementation


## Sysem Requirements
Typoical TOC

- Introduction
    - Purpose, scope, definitions, acronyms, references
- Overall description
    - Product perspective (system context)
    - User classes & characteristics
    - Operating environment
    - Design & implementation constraints
    - Assumptions & dependencies
- System requirements
    - 3.1 Functional requirements (each uniquely numbered)
    - 3.2 Non-functional requirements (quality attributes, see §5)
    - 3.3 Interface requirements (UI, APIs, hardware I/O, comms)
- Traceability matrix (links requirements → use cases → tests)
- Appendices (glossary, analysis models, data dictionary)


| Good practice                                                                  | Why it matters                                                         |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Use “shall”** for mandatory behaviour, “should” for desirable.               | ISO 29148 mandates unambiguous modal verbs.                            |
| **One requirement = one sentence.**                                            | Easier to test and trace.                                              |
| **Make them SMART-T:** *Specific, Measurable, Achievable, Relevant, Testable.* | Prevents vague, un-verifiable text.                                    |
| **Quantify non-functionals.**                                                  | “The system shall display the dashboard in ≤ 2 s for 95 % of queries.” |
| **Avoid weasel words:** *fast, user-friendly, robust.*                         | They hide subjective interpretation.                                   |


- FR-025: “The system shall encrypt all data at rest using AES-256 with keys managed by AWS KMS.”
- NFR-011: “During peak load of 10,000 concurrent users, average response time for the /checkout API shall not exceed 750 ms.”

Non Functional Example

| Category                          | Typical metrics / examples                     |
| --------------------------------- | ---------------------------------------------- |
| **Performance & scalability**     | throughput, latency, max users                 |
| **Availability & reliability**    | uptime %, MTTR, redundancy level               |
| **Security & privacy**            | authN/Z, encryption, audit logging, GDPR       |
| **Usability & accessibility**     | WCAG level, task completion time               |
| **Maintainability & portability** | code standards, containerisation, supported OS |
| **Safety & regulatory**           | ISO 26262, IEC 62304, HIPAA, FedRAMP           |



## SLO
- https://alexewerlof.medium.com/calculating-composite-sla-d855eaf2c655
- https://learn.microsoft.com/en-us/answers/questions/122986/composite-slas


SLA with financial credit

- https://cloud.google.com/pubsub/sla?hl=en
    - secnario 1
        - uptime: `99% to < 99.95%`
        - credit: 10%
    - secnario 2
        - uptime: `95% to < 99%`
        - credit: 25%
    - secnario 3
        - uptime: `< 95%`
        - credit: 50%
    - calc
        - a1 := 0.5 / 0.95
        - a2 := 0.25 / (0.99 - 0.95)
        - a3 := 0.1 / (0.9995 - 0.99)
        - a4 := 0.15 / (1 - 0.9995)
        - E1 := a1 (0.95 ** 2) / 2
            - 0.2375
        - E2 := a2 (0.99 ** 2 - 0.95 ** 2) / 2
            - 0.2425
        - E3 := a3 (0.9995 ** 2 - 0.99 ** 2) / 2
            - 0.099475
        - E4 := a4 (1 ** 2 - 0.9995 ** 2) / 2
            - 0.1499625
        - E1 + E2 + E3 + E4 = 0.7294375
- https://aws.amazon.com/codeartifact/sla/
    - secnario 1
        - uptime: `99% to < 99.9%`
        - credit: 10%
    - secnario 2
        - uptime: `95% to < 99%`
        - credit: 25%
    - secnario 3
        - uptime: `< 95%`
        - credit: 100%
    - a1 := 0.1 / (0.999 - 0.99)
    - a2 := 0.9 / (0.99 - 0.95)
    - E1 := a1 * (0.999 ** 2 - 0.99 ** 2) / 2
    - E2 := a2 * (0.99 ** 2 - 0.95 ** 2) / 2
    - ans := E1 + E2 = 0.97245






## For Job interview
- [Top 10 System Design Interview Questions for Software Engineers](https://hackernoon.com/top-10-system-design-interview-questions-for-software-engineers-8561290f0444)
- [Grokking the System Design Interview](https://www.educative.io/collection/5668639101419520/5649050225344512)
    - https://www.educative.io/courses/grokking-the-system-design-interview


## Reference
