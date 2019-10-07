---
title: Apache log4j
---

## Apache log4j


### Configuration with properties
* [Log4j – Configuring Log4j 2 - Apache Log4j 2](https://logging.apache.org/log4j/2.x/manual/configuration.html)

- Through a configuration file written in XML, JSON, or YAML.
- Programmatically, by creating a ConfigurationFactory and Configuration implementation.
- Programmatically, by calling the APIs exposed in the Configuration interface to add components to the default configuration.
- Programmatically, by calling methods on the internal Logger class.

Automatic configuration

- Log4j will inspect the "log4j.configurationFile" system property and, if set, will attempt to load the configuration using the ConfigurationFactory that matches the file extension.
- If no system property is set the YAML ConfigurationFactory will look for log4j2-test.yaml or log4j2-test.yml in the classpath.
- If no such file is found the JSON ConfigurationFactory will look for log4j2-test.json or log4j2-test.jsn in the classpath.
- If no such file is found the XML ConfigurationFactory will look for log4j2-test.xml in the classpath.
- If a test file cannot be located the YAML ConfigurationFactory will look for log4j2.yaml or log4j2.yml on the classpath.
- If a YAML file cannot be located the JSON ConfigurationFactory will look for log4j2.json or log4j2.jsn on the classpath.
- If a JSON file cannot be located the XML ConfigurationFactory will try to locate log4j2.xml on the classpath.
- If no configuration file could be located the DefaultConfiguration will be used. This will cause logging output to go to the console.

## Reference
* [Log4j – Apache Log4j 2 - Apache Log4j 2](https://logging.apache.org/log4j/2.x/)
