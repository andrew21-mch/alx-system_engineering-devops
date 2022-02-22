This postmortem examines the root cause and resolution of an issue that I faced during a report card management system project (6 weeks project)

Issue Summary
For a report card management system, we had a case of ranking, which was really a pain in the neck, we had already deployed this application hoping to update that issue withing the nearest future, but after the first term, it was a necessity which need urgent attention. This application was built in laravel and few of us knew laravel. so it really demanded alot of time and concentration. because of how urgent it was, we had to come up with the a fast way to implement a solution the the urgent problem, below was how we fixed it.
Timeline (all in PST)
- 1:00 pm: Creating of Average table
- 1:30 pm: Establishing a relationship between the average table and the results table and run some test
- 2:00 pm: Using laravel, try implementing some data read operations to see the outcome and continue doing until the desired result is out.
- 2:30 pm: Query the results table in relation to the student and average table to get student rank. make sure it works.
- 3:00 pm: using Laravel, implement this queries and test to make sure it works, now implement the functions to get student average plus class based on the class
- 3:30 pm: Student Ranking fully working
Root Cause
- There was no table to store student average. because of this, there was not way to easily query information from the database except having to run data multiple Queries on the database which will make the application slower
Also there existed no relationship between the average class, the student table and the results table. this is a clear indication that trying to run any relational database query will only be a waste of time.
Correct and Preventative Measures
In the future, it would have been faster to resolve this issue had we enabled updating the relationship structure of the database.
Corrective Measures
- Create a one to one relationship between student and average and a one to many relationship between the average and results table
- each time you insert a mark into the result table, update the average table by querying the marks and doing all appropriate calculation, next update the result table with the average id
- To calculate the rank, you might want to query all the averages related to the students class and then do some sorting then find the position of the students average, that will be the position of the student in that class.
sometimes, when you encounter a problem during development, you need to have a calm head and discuss with team to bring out the best solution.
Hope it was helpful
