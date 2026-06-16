4 - Scheduling and notification 

**Schedule the notebook to run daily** 

1- Navigate to workflows in Databricks
2- Click create job
3- Provide a name for the job
4- Add a task and select the notebook from the previous tasks
5 - Config a job cluster  / select an existing 
6- pass the required notebook parameters (if needed ) start_date, end_date & env.
7- Navigate to Schedule > Schedule Triggered
8- Configure the schedule to run daily at the desired time.
9 - Save the job

**Setting up the notification system**

1- Open the job that we have created earlier above 
2- Navigate > Job Notifications Section
3- Click Edit Notification -> Click Add Notification -> Select Destination as Email address.
4- Type the email to receive notification.
5- Select select from the options ( to get notification on successful execution).
6 - Click save.
