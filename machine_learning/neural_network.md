---
title: Neural Network
---

## Neural Network


## Examples
* $$(x_{1}, x_{2}) \in \{0, 1\}$$,

AND

$h_{\mathrm{AND}}(x) = \sum_{i=0}^{2} x_{i} \theta_{\mathrm{AND}} $,


| $x_{1}$   | $x_{2}$   | outputs                           |
| --------- | --------- | ---------------------             |
| 0         | 0         | $-30 + 20 \times 0 + 20 \times 0$ |
| 0         | 1         | $-30 + 20 \times 0 + 20 \times 1$ |
| 1         | 0         | $-30 + 20 \times 1 + 20 \times 0$ |
| 1         | 1         | $-30 + 20 \times 1 + 20 \times 1$ |

OR

$h_{\mathrm{OR}}(x) = \sum_{i=0}^{2} x_{i} \theta_{\mathrm{OR}} $,

| $x_{1}$   | $x_{2}$   | outputs                           |
| --------- | --------- | ---------------------             |
| 0         | 0         | $-10 + 20 \times 0 + 20 \times 0$ |
| 0         | 1         | $-10 + 20 \times 0 + 20 \times 1$ |
| 1         | 0         | $-10 + 20 \times 1 + 20 \times 0$ |
| 1         | 1         | $-10 + 20 \times 1 + 20 \times 1$ |


NOR

$h_{\mathrm{NOR}}(x) = \sum_{i=0}^{2} x_{i} \theta_{\mathrm{NOR}} $,

| $x_{1}$   | $x_{2}$   | outputs                          |
| --------- | --------- | ---------------------            |
| 0         | 0         | $10 - 20 \times 0 - 20 \times 0$ |
| 0         | 1         | $10 - 20 \times 0 - 20 \times 1$ |
| 1         | 0         | $10 - 20 \times 1 - 20 \times 0$ |
| 1         | 1         | $10 - 20 \times 1 - 20 \times 1$ |

XOR = ($x_{1}$ AND $x_{2}$) OR ((NOT $x_{0}$) AND (NOT $x_{1}$))

##
