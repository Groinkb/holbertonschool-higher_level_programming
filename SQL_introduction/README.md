SQL technique: functions
Sometimes, the information that we need is not actually stored in the database, but has to be computed in some way from the stored data. In our order entry example, there are two derived attributes (/subtotal in OrderLines and /total in Orders) that are part of the class diagram but not part of the relation scheme. We can compute these by using SQL functions in the SELECT statement.

There are many, many functions in any implementation of SQL—far more than we can show here. Unfortunately, many of the functions are defined quite differently in different database packages, so you should always consult a reference manual for your specific software.
