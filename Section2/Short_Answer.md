Section 2 - Q1

**Describe the different cluster modes available in Databricks.**

Databricks provides several cluster modes depending on the workload:

**1. All-Purpose Clusters**

* Used for interactive development and data exploration.
* Shared by multiple users.
* These are manually started and Stopped by the user and this is why they are more expensive

**2. Job Clusters**

* Created automatically when a job starts and terminated after completion.
* More cost-effective than all-purpose clusters.
* They offer isolation as a decidated cluster is spun up for a job

**3. High-Concurrency Clusters**

* Designed to support multiple concurrent users.

**4. Single Node Clusters**

* Runs Spark on a single machine.
* Useful for lightweight development, testing, and learning purposes.

-------------------------------------------------------------------------------------------------------
**Q2** 

**Explain the concept of cluster autoscaling in Databricks.**

Cluster autoscaling automatically adjust the number of worker/executor nodes.
When workload increases, Databricks adds workers to improve processing performance. When workload decreases, unnecessary workers are removed to reduce infrastructure costs.

-------------------------------------------------------------------------------------------------------
**Q3**
**What are the advantages of using Delta Lake over Parquet or ORC formats?**

Delta lake extends parquet by adding reliablity, governance and transaction capabilities.

advantages include : 
* ACID Transaction
* Schema enforcement
* Time Travel
* Data versioning
* Lakehouse Architecture becomes possible.
-------------------------------------------------------------------------------------------------------
**Q4**
**How would you handle large datasets that do not fit into memory? Discuss both storage and processing considerations.**

Large datasets should be handled using distributed storage and distributed processing techniques.

**Storage Considerations**

* Store data in Delta Lake format.
* Partition data appropriately.
* Use cloud storage such as S3, ADLS, or GCS.
* Compress files using Parquet

**Processing Considerations**

* Use Spark’s distributed execution engine.
* Filter data as early as possible.
* Enable autoscaling clusters.

-------------------------------------------------------------------------------------------------------

**Q5**

**Provide a scenario where Delta Lake’s time travel feature would be particularly useful.**

A Common scenario is accidental data corruption or incorrect updates
suppose a datapipeline mistakenly overwrites customer records. Using Delta Lake Time Travel, we can access a previous table version and restore the data.

eg - 

SELECT *
FROM customers VERSION AS OF 10;

-------------------------------------------------------------------------------------------------------

**Q6**
**How would you ensure compliance with data privacy regulations using Databricks?**

Compliance with data privacy regulations can be achieved in Databricks using governance, security, and auditing features.

The key practice that should be followed are : 
* Implementing Role-Based Access Control
* Using Unity Catalog
* Encrypting data at rest and in transit.
* Make sure to audit any changes
* Least Privilege Access
* 
-------------------------------------------------------------------------------------------------------

**Q7**
**Explain the difference between a Job Cluster and an All-Purpose Cluster. Under what circumstances would you choose one over the other?**

**All-Purpose Cluster.**

**Uses :** 
* Interactive Development
* Data Exploration
* Testing

**Characteristics :**

* Shared by Users
* Runs Continously
* Higher operational Cost

**Jobs Cluster**

**Used for:**

* Scheduled jobs
* ETL pipelines
* Production workloads

**Characteristics:**

* Created automatically when a job starts
* Terminated after completion
* Better resource isolation
* Lower cost

Use All-Purpose Clusters during development and debugging.
Use Job Clusters for automated production workloads where cost efficiency and reliability are important.

-------------------------------------------------------------------------------------------------------

**Q8**

**What are the advantages and disadvantages of Serverless Clusters, and in what scenarios are they most effectively used?**

**Advantages**

* No cluster management required.
* Faster startup times.
* Automatic scaling.
* Reduced operational overhead.
* Better user experience for analytics workloads.

**Disadvantages**

* Less control over infrastructure configuration.
* Limited customization compared to traditional clusters.
* Potentially higher cost for certain long-running workloads.

**Best Use Cases**

* Databricks SQL workloads
* Interactive analytics
* Teams wanting simplified operations

-------------------------------------------------------------------------------------------------------

**Q9**
**How does Databricks handle version control for notebooks and other code artifacts? Discuss available options and best practices.**

Databricks supports version control through Databricks Repos, which integrates with Git providers such as:

* GitHub
* Azure DevOps
* Bitbucket

**Best practices include:**

* Maintaining separate branches for development and production.
* Using pull requests and code reviews.
* Storing notebooks and source code in repositories.
* Avoiding direct changes in production.

**Benefits:**

* Change tracking
* Collaboration
* Rollback capability
* Better code quality

demostration : 
main
|
|--develop
|--feature/customer-ingestion
|--feature/schema-validation

-------------------------------------------------------------------------------------------------------

**Q10**
**Describe the role of Databricks Repos in collaborative development. How do they differ from traditional Git repositories?**

Databricks Repos enables developers to integrate Databricks with version control systems such as GitHub, Azure DevOps, and Bitbucket.

It allows teams to:

* Collaborate on notebooks and code
* Track code changes
* Create branches
* Perform code reviews

Difference :

**Databricks Repos :**
* Integrated directly into Databricks Workspace
* Allows editing notebooks inside Databricks
* Syncs notebooks and code with Git providers

**Traditional Git Repos :**
* External version control system
* Usually managed through IDEs like VS Code
* Stores source code and version history


-------------------------------------------------------------------------------------------------------

**Q11**
**What are Databricks Widgets and how can they be used to make notebooks more interactive? Provide an example use case.**

Databricks Widgets provide a way to create interactive input controls within notebooks. They allow users to pass parameters without modifying code.

**Use Case**

A use case that i can provide is like a sales reporting notebook that gives the user to select:

*Country
*Date Range
*or Product Category

OR

A use case where the user chooses the environment type to change the configuration dynamically.

eg : evn will be having options like dev, prod.

-------------------------------------------------------------------------------------------------------
**Q12**

**Discuss the importance of monitoring and alerting in Databricks. What tools and features are available for tracking performance and identifying issues?**

Monitoring and alerting are important to ensure reliability, performance and cost optimization
The areas to monitor are : Job Failures, Cluster Utilizationa nd metrics, Pipeline execution time, performance of the query

Databricks provide 
* Cluster Metrics
* Audit Logs
* Jobs History
* Notficationa and Alerts

 -------------------------------------------------------------------------------------------------------
 **Q13**
**What is Databricks Assistant and how can it help You?**
 Databricks Assistant is the AI powered coding assistant (Genie AI) that is now integrated to the databricks platform

 It helps me in :
 * Genrating Code
 * Reviewing code
 * Debug and explain errors
 * Write SQL queries
 * imporve the productivty

 -------------------------------------------------------------------------------------------------------

**Q14**

**How does the Databricks Assistant learn or adapt to a user’s workspace context?**

The Databricks assistant uses the workspace content to provide suggestion based on the factors like :
* Notebook content
* Schemas of tables
* SQL Queries
* Errors

 -------------------------------------------------------------------------------------------------------
**Q15**

**Compare Databricks Assistant and GitHub Copilot.**

Both the Databricks assistant and Github copilot are AI powered assistants they help to imporve productivity but mainly focus in different uses:

For databricks i can say is, : 
* It is integrated to the platform
* It has more context awareness
* It has stronger spark knowledge
* It has context based stronger SQL knowledge
* it is limited to databricks platform

For Github Copilot :
* It is not integrated to the platform
* It has less context awareness
* It has weaker spark knowledge compared to databricks assistant
* It is not limited to databricks platform only

-------------------------------------------------------------------------------------------------------

**Q16**
**What is the purpose of MLflow in a Databricks environment?**

MLflow helps us keep track of machine learning experiments in Databricks. 
We can log parameters and metrics, compare different model runs, version models, and deploy the best model to production in an organized way.

-------------------------------------------------------------------------------------------------------
**Q17**

**Describe one way that databricks simplifies machine learning workflows**

Databricks simplifies machine learning by integrating MLflow, which helps track experiments, log metrics and parameters, manage model versions, and deploy models. 
Having everything in one place makes it easier to collaborate and manage the entire ML workflow.

-------------------------------------------------------------------------------------------------------
**Q18**

What is databricks Feature Store and why is it useful

Databricks Feature Store is a central place to store and manage machine learning features.

It is useful in several ways like : 

* Reuse features across multiple models
* Maintain consistency between training and inference data
* Improve collaboration between Data Engineers and Data Scientists

-------------------------------------------------------------------------------------------------------

**Q19**

**How can a user register and deploy a model in databricks**

A user can register and deploy a machine learning model in Databricks using MLflow and the Model Registry.
Step 1: Train the Model
Step 2: Log the Model with MLflow
Step 3: Register the Model
Step 4: Validate and Promote - Staging and Prod
Step 5: Deploy the Model

-------------------------------------------------------------------------------------------------------
**Q20**
**What is one key advantage of using notebooks in Databricks for machine learning development?**

One of the key advantages of Databricks notebooks is that they provide a collaborative and interactive environment for machine learning development. Teams can write and run code, explore data, visualize results, and document their work in the same notebook. This makes it easier to collaborate, experiment, and build models more efficiently.
