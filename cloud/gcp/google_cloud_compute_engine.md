---
title: Google Cloud Compute Engine
---

## Google Cloud Compute Engine


## Preemptible VM Instaces
* [Preemptible VM Instances  |  Compute Engine Documentation  |  Google Cloud](https://cloud.google.com/compute/docs/instances/preemptible?hl=en_US&_ga=2.13732919.-1205531873.1513079066#preemptible_with_instance_groups)

* system eventでいつでも停止される
* system eventによる停止の確率は通常低いが、day to day, zone to zoneで違う
* 24 hoursで停止
* resourceに限りがあるので、常に利用可能なわけではない
* live migrate, maintenance eventでのautomatically restartはない
* Google Compute Engine SLAで保証されてない

Preemption process

1.`ACPI G2 Soft Off` signalが送信される
    * [Advanced Configuration and Power Interface - Wikipedia](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states)
    * [Creating and Starting a Preemptible VM Instance  |  Compute Engine Documentation  |  Google Cloud](https://cloud.google.com/compute/docs/instances/create-start-preemptible-instance#handle_preemption)
2. 30sec停止しない場合は、` ACPI G3 Mechanical Off` signalがOSに送られる
    * [Advanced Configuration and Power Interface - Wikipedia](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states)
3. TERMINATED stateに移行する

## Reference
