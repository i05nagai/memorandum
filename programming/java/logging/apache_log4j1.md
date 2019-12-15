---
title: Apache Log4j
---

## Apache Log4j


## Configuration

Default initialization process


- Setting the log4j.defaultInitOverride system property to any other value then "false" will cause log4j to skip the default initialization procedure (this procedure).
- Set the resource string variable to the value of the `log4j.configuration` system property. The preferred way to specify the default initialization file is through the `log4j.configuration` system property. In case the system property log4j.configuration is not defined, then set the string variable resource to its default value `log4j.properties`.
- Attempt to convert the resource variable to a URL.
- If the resource variable cannot be converted to a URL, for example due to a `MalformedURLException`, then search for the resource from the classpath by calling `org.apache.log4j.helpers.Loader.getResource(resource, Logger.class)` which returns a URL. Note that the string `log4j.properties` constitutes a malformed URL.
    - See `Loader.getResource(java.lang.String)` for the list of searched locations.
- If no URL could not be found, abort default initialization. Otherwise, configure log4j from the URL.
    - The PropertyConfigurator will be used to parse the URL to configure log4j unless the URL ends with the ".xml" extension, in which case the DOMConfigurator will be used. You can optionaly specify a custom configurator. The value of the `log4j.configuratorClass` system property is taken as the fully qualified class name of your custom configurator. The custom configurator you specify must implement the Configurator interface.


```
-Dlog4j.configuration=foobar.lcf
```

## Reference
- [Apache log4j 1\.2 \- Short introduction to log4j](https://logging.apache.org/log4j/1.2/manual.html)
