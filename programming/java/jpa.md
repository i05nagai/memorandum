---
title: JPA
---

## JPA

## Entity

- `@Entity`
- `@Temporal`
- `@Transient`
- `@Table`
- `@Column`
- `@Id`
- `@Enumerated`


## Associations
- https://www.baeldung.com/jpa-hibernate-associations

- Undirect Associations
    - `@ManyToOne`
    - `@OneToMany`
    - `@OneToOne`
    - `@ManyToMany`
- `@JoinColumn`

#### One to Many

```
@Entity
public class Department {
 
    @Id
    private Long id;
 
    @OneToMany
    @JoinColumn(name = "department_id")
    private List<Employee> employees;
}

@Entity
public class Employee {
 
    @Id
    private Long id;
}
```

- Department
    - id
- Employee
    - id
    - department_id

#### Many to One

```
@Entity
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    @ManyToOne
    @JoinColumn(name = "school_id")
    private School school;
}

@Entity
public class School {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
}
```

- Student
    - id
    - name
    - school_id
- School
    - id
    - name

#### Many to Many
https://www.baeldung.com/jpa-many-to-many

```
    @ManyToMany(cascade = CascadeType.ALL)
    @JoinTable(
            name = "orders_items",
            joinColumns = @JoinColumn(name = "order_id"),
            inverseJoinColumns = @JoinColumn(name = "item_id"))
```


## JPA Mysql
- https://vladmihalcea.com/why-should-not-use-the-auto-jpa-generationtype-with-mysql-and-hibernate/

- On Hibernate6
    - Use `@GeneratedValue(strategy = GenerationType.Identity)`

## Reference
- https://www.baeldung.com/jpa-entities
