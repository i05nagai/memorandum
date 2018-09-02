---
title: Site Reliability Engineering
---

## Site Reliability Engineering


* Monitoring
    * valid monitorin output
        * alerts
            * signify that a human needs to take action immediately in response to something that is either happening or about to happen, in order to improve the situation
        * tickets
            * Signify that a human needs to take action, but not immediately
            * The system cannot automatically handle the situation, but if a human takes action in a few days, no damage will result
        * logging
            * no one needs to look at this information, but it is recorded for diagnostic or forensic purposes
* Realiability
    * a function of Mean Time To Failure and Mean Time To Repair
    * thinking through and recording the best practices ahead of time in a "playbook" produces roughly a 3x improvement in MTTR as compared to the strategy "winging it"
    * on-call playbook
* Change management
    * SRE has found that roughly 70% of outages are due to chagnes in a live system
    * Implementing progressive rollouts
    * Quickly and accurately detecting problems
    * rolling back changes safely when problems arise
* Demand ForeCasting and Capacity Planning
    * capacity planning should take the follwoings into account
        * organic growth which stems from natural product adoption and usage by customers
        * inorganic growth whiche results from events like feature launches, marketing campaign, or other business-driven changes
    * steps in capacity planning
        * An accurate organic demand forecast, which extends beyond the lead time require for acquiring capacity
        * An accurate incorporation of inorganic demand soruces into the deamnd forecast
* Provisioning


## Reference
* [Google - Site Reliability Engineering](https://landing.google.com/sre/book/chapters/software-engineering-in-sre.html)
* [Googleのインフラ技術から考える理想のDevOps](https://www.slideshare.net/enakai/googledevops)
* [Google Cloud Platform Japan 公式ブログ: SLO、SLI、SLA について考える : CRE が現場で学んだこと](https://cloudplatform-jp.googleblog.com/2017/02/availability-part-deux-CRE-life-lessons.html)
