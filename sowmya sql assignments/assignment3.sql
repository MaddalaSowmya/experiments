/*Assignment 3: Explain the ACID properties of a transaction in your own words. 
Write SQL statements to simulate a transaction that includes locking and 
demonstrate different isolation levels to show concurrency control.*/

/*There are various types of locking systems but mainly two types of locks
are important:
1. shared lock (read-only) s-lock
They allow multiple transaction/users to a table simultaneously.
 */

start transaction;

 