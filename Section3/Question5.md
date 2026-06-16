The Databricks CLI can be installed and configured in a WSL environment. Once authenticated, it allows us to create a cluster configuration file and provision Databricks clusters directly from the command line.

**Install Databricks CLI in the WSL environment.**

pip install databricks-cli

---------------------------------------------------

**Verify the installation**

databricks --version

---------------------------------------------------

**Configure the Databricks workspace URL and Personal Access Token (PAT).**

databricks configure --token

---------------------------------------------------

**Define the cluster configuration (JSON)
adjust the cloud specific node_type_id and spark version as per our cloud provider**

{
  "cluster_name": "dev-cluster",
  "spark_version": "14.3.x-scala2.12",
  "node_type_id": "Standard_DS3_v2",
  "num_workers": 2,
  "autotermination_minutes": 30
}

---------------------------------------------------

**Create a Databricks cluster using the configuration file.**

databricks clusters create --json-file cluster.json

---------------------------------------------------

**Verify that the cluster was created successfully.**

databricks clusters list
