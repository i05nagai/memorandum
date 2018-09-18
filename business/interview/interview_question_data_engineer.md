---
title: Interview Question Data Engineer
---

## Interview Question Data Engineer

## Database
* [Database Normalization \| Normal Forms \- GeeksforGeeks](https://www.geeksforgeeks.org/database-normalization-normal-forms/)
* [DBMS \| Keys in Relational Model \(Candidate, Super, Primary, Alternate and Foreign\) \- GeeksforGeeks](https://www.geeksforgeeks.org/dbms-keys-candidate-super-primary-alternate-and-foreign/)

* First normalization form
* Second normalization form
    * no partial dependency
* Third normalization form
* partial dependency
    * student_num, cource_num, cource_name
* transitive dependency
    * student_num, student_name, student_state, student_country, student_age
    * student_num->student_name,
    * student_num->student_state,
    * student_num->student_country,
    * student_num->student_age,
    * student_num->student_state,
    * student_state->student_country
* Boyce Codd Normal Form
* super key
    * The set of attributes which can uniquely identify a tuple is known as Super Key. For Example, STUD_NO, (STUD_NO, STUD_NAME) etc.
* candidate key
    * candidate key is one of super key
    * The minimal set of attribute which can uniquely identify a tuple is known as candidate key. For Example, STUD_NO in STUDENT relation.
    * composite candidate key: {sutudent_num, course_num} -> student_course
        * usually keys in a table for relation
* primary key
    * there can be more than one candidate key in a relation out of which one can be chosen as primary key
    * student_num -> student_phone
    * student_phone -> student_num
* alternate key
    * the candidate key other than primary key is called as alternate key.
* foreigh key

## Reference
* [Data Warehouse Architecture - Kimball and Inmon methodologies | James Serra's Blog](https://www.jamesserra.com/archive/2012/03/data-warehouse-architecture-kimball-and-inmon-methodologies/)
* [Building an Effective Data Warehouse Architecture](https://www.slideshare.net/jamserra/data-warehouse-architecture-16065902)
