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
* Job and Data Organization
    * A backend in Asia contacting a Bigtable in the USA adds a significant amount of latency, so we replicate the Bigtable in each region
    * Bigtable replication
        * it provides a resilience should a Bigtable server fail
        * it lowers data-access latency
* Risk
    * The cost of redundant machine/compute resources
    * The opportunity cost
        * the cost borne by an organization when it allocates engineering resources to build systems or features that diminish risk instead of features that are directly visible to or usable by endusers. These engineers no longer work on new features and products for end users
    * unplanned downtime
        * the most straight forward way of representing risk tolerance is in terms of the acceptable level of unplanned downtime
        * availability = uptime / (uptime + downtime)
            * a system with an availability target of 99.99% can be down for up to 52.56 minutes in a year
            * at Google, service is properly distributed, so the systems is always up
        * availability = successful requests/(total requests)
            * a system that serves 2.5M requests in a day with a daily availability target of 99.99% can serve up to 250 errors and still hit its target for that given day
* target level of availability
    * what level of service will the users expect?
    * does this service tie directly to revenue?
    * Is this a paid service, or is it free?
    * If there are competitors in the marketplace, what level of service do those competitors provide?
    * Is this service targeted at consumers, or at enterprises?
* cost
    * If we were to build and operate these systems at one more nine of availability, what would our incremental increase in revenue be?
    * Does this additional revenue offset the cost of eaching that level of reliability?
* Error budget
    * motivation
        * product development performance is evaluated on product velocity
        * SRE performance is evaluated on reliability of a service
    * common tension
        * software fault tolerance
        * testing
        * push frequency
        * canary duration and size
    * practice
        * Product management defines an SLO, which sets an expectation of how much uptime the service should have per quarter
        * The actual uptime is measured by a neutral third party: our monitoring system
        * the difference between these two numbers is the budget of how much unreliability is remaining for the quarter
        * As long as the uptime measured is above the SLO -- in other words, as long as there is error budget remaining -- new releases can be pushed
* SLIs
    * examples
    * user-facing serving systems
        * availability
            * could we respond to the request?
        * latency
            * how long did it take to respond?
        * throughput
            * how many requests could be handled?
    * storage systems
    * big data systems
        * end-to-end latency
            * how long does it take the data to progress from ingestion to completion?
        * throughput
            * how muc hdata is being processed?
    * all systems
        * correctness
* Toil
* Monitoring
    * 4 Golden signals
        * Latency
            * the time it takes to service a request
            * It's important to distinguish between the latency of successful requests and the latency of failed requests
        * Traffic
            * A measure of how much demand is placed on your system, measured in a high-level system-specific metric
            * For web service
                * HTTP requests per second
            * For an audio streaming system
                * network I/O rate
                * concurrent sessions
            * For key value storage system
                * transactions
                * retrievals per second
        * Errors
            * the rate of requests that fail
                * fail explicitly (e.g. HTTP 500s)
                * fail implicitly (for example, an HTTP 200 sucess response but couples with the wrong content)
                * fail by policy
                    * if you committed to one-second responsee times, any request over one second is an error
        * Saturaiton
            * How full your service is
            * Note that many systems degrade in performance before they achieve 100% utilization
    * worrying about your tail
        * Consider tail
            * mean CPU usage of your nodes
            * the mean fullness of your database
            * the mean latency
    * Choosing an appropriate resolution for measurements
    * As simple as possible
        * Like all software systems, monitoring can become so complex that its fragile, complicated to change , and a maintenace burden
    * questions
        * Does this rule detect an otherwise undetected condition that is urgent, actionable and actively or imminently user-visible?
        * Will I ever be able to ignore this alert, knowing it's benign? When and why will I be able to ignore this alert, and how can I avoid this cenario?
        * Does this alert definitely indicate that users are being negatively affected? Are there detectable cares in which users aren't bein negatively impacted, such as drained traffic or test deployments, that should be filtered out?
        * Can I take action in respomse tp this alert? Is that action urgent, or could it wait until mornign? Could the action be safely autmated? Will that action be a long term fix, or just a short-term workaround?
        * Are other people getting paged for this issue, therefore rendering at least one of the pages unnecessary?
    * fundamental philosophy on pages and pagers
        * Every time the pager goes off, I should be able to react with a sense of urgency
        * Every page should be actionable
        * Every page response should require intelligence. If a page merely metrits a robotic reponse, it shouldn't be a page
        * Pages should be about a novel problem or an event that hasn't been seen before
* Automation
    * the Use cases for automation
        * automation is "metasoftware" -- software to act on software
        * User account creation
        * Cluster turnup and turndown for service
        * Software or hardware installation preparation and decommisiooning
        * Rollouts of new software versions
        * runtime configuration changes
        * A special case of runtime config changes; changes to your dependencies



## Reference
* [Google - Site Reliability Engineering](https://landing.google.com/sre/book/chapters/software-engineering-in-sre.html)
* [Googleのインフラ技術から考える理想のDevOps](https://www.slideshare.net/enakai/googledevops)
* [Google Cloud Platform Japan 公式ブログ: SLO、SLI、SLA について考える : CRE が現場で学んだこと](https://cloudplatform-jp.googleblog.com/2017/02/availability-part-deux-CRE-life-lessons.html)
