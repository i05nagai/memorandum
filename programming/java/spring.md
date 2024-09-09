---
title: Spring
---

## Spring


## Database initializationo
https://docs.spring.io/spring-boot/how-to/data-initialization.html

- By default, SQL database initialization is only performed when using an embedded in-memory database. To always initialize an SQL database, irrespective of its type, set `spring.sql.init.mode` to `always`.

#### @CustomAccessDeniedHandler

#### @WebFilter


#### @ResponseStatus


#### @RequestMapping


#### @RequiredArgsConstructor


## Fallback
- Exception Handling in Spring MVC https://spring.io/blog/2013/11/01/exception-handling-in-spring-mvc

#### @ControllerAdvice
Global Exception Handling.

#### @ExceptionHandler
You can add extra (@ExceptionHandler) methods to any controller to specifically handle exceptions thrown by request handling (@RequestMapping) methods in the same controller. 

#### class ResponseEntityExceptionHandler
A convenient base class for @ControllerAdvice classes that wish to provide centralized exception handling across all @RequestMapping methods through @ExceptionHandler methods.


## Rest
- https://spring.io/guides/tutorials/rest

## gRPC
- https://www.baeldung.com/spring-boot-grpc


## Test
- https://spring.io/guides/gs/testing-web
- https://docs.spring.io/spring-boot/docs/2.0.4.RELEASE/reference/html/boot-features-testing.html

## Configuration
- path: `src/resources/application.yml`
- https://docs.spring.io/spring-boot/appendix/application-properties/index.html

## Reference
- [spring\-projects/spring\-framework: Spring Framework](https://github.com/spring-projects/spring-framework)
