# todo-api
a demo repo for creating a to-do api using Azure functions


### prerequisites
        azure account and valid subscription
        az cli installed
        git installed

### Deployment steps

1. define some variables

```bash
# General variables
randomIdentifier=$RANDOM
location="eastus"
resourceGroup="todo-api-rg"

# CosmosDB variables
account="todo-account-cosmos-$randomIdentifier" #needs to be lower case
database="todo-db-sql-cosmos"
container="todo"
partitionKey="/id"

# function app variables
storage="todosa$randomIdentifier"
functionApp="todo-serverless-function-$randomIdentifier"
skuStorage="Standard_LRS"
```

2. change the active subscription using the subscription ID
```bash
az account set --subscription $subsciprtion_id
```

3. Create a resource group
```bash
echo "Creating $resourceGroup in $location..."
az group create --name $resourceGroup --location "$location"
```

4. Create a Cosmos account for SQL API, database and container
```bash
echo "Creating $account"
az cosmosdb create --name $account --resource-group $resourceGroup --locations regionName="$location"

# Create a SQL API database
echo "Creating $database"
az cosmosdb sql database create --account-name $account --resource-group $resourceGroup --name $database

# Create a SQL API container
echo "Creating $container"
az cosmosdb sql container create --account-name $account --resource-group $resourceGroup --database-name $database --name $container --partition-key-path $partitionKey
```

5. create Function App where we will deploy our functions
```bash
# a storage account is needed for function apps
echo "Creating $storage"
az storage account create --name $storage --location "$location" --resource-group $resourceGroup --sku $skuStorage

# Create a serverless function app in the resource group.
echo "Creating $functionApp"
az functionapp create --name $functionApp --storage-account $storage --consumption-plan-location "$location" --resource-group $resourceGroup --os-type Linux --functions-version 3 --runtime python --runtime-version 3.8
```
