---
title: jmeter
---

## jmeter


```
brew install jmeter
```


- Thread Group
    - The Thread Group tells JMeter the number of users you want to simulate

## CLI
- `-n`
    - This specifies JMeter is to run in cli mode
- `-t [name of JMX file that contains the Test Plan]`
- `-l [name of JTL file to log sample results to]`
- `-j [name of JMeter run log file]`
- `-r`
    - Run the test in the servers specified by the JMeter property "remote_hosts"
- `-R [list of remote servers]`
    - Run the test in the specified remote servers
- `-g [path to CSV file]`
    - generate report dashboard only
- `-e`
    - generate report dashboard after load test
- `-o`
    - output folder where to generate the report dashboard after load test.
    - Folder must not exist or be empty The script also lets you specify the optional firewall/proxy server information:
- `-H [proxy server hostname or ip address]`
- `-P [proxy server port]`


## Create a scenario
Run GUI

- https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Sampler
    - JSR223 Sample is recoommend for performance
- http://jmeter.apache.org/usermanual/build-web-test-plan.html

## Reference
https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Sampler
