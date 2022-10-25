# todo-api
a demo repo for creating a to-do api using Azure functions

Let's first create our database where we will store all TODO tasks

prerequisites
python
git

# define some variables
randomIdentifier=$RANDOM
location="eastus"
resourceGroup="todo-api-rg"
account="todo-account-cosmos-$randomIdentifier" #needs to be lower case
database="todo-db-sql-cosmos"
container="todo"
partitionKey="/id"

# function app variables
storage="todosa$randomIdentifier"
functionApp="todo-serverless-function-$randomIdentifier"
skuStorage="Standard_LRS"

# change the active subscription using the subscription ID
az account set --subscription $subsciprtion_id

# Create a resource group
echo "Creating $resourceGroup in $location..."
az group create --name $resourceGroup --location "$location"

# Create a Cosmos account for SQL API
echo "Creating $account"
az cosmosdb create --name $account --resource-group $resourceGroup --locations regionName="$location"

# Create a SQL API database
echo "Creating $database"
az cosmosdb sql database create --account-name $account --resource-group $resourceGroup --name $database

# Create a SQL API container
echo "Creating $container"
az cosmosdb sql container create --account-name $account --resource-group $resourceGroup --database-name $database --name $container --partition-key-path $partitionKey


# Let's create our Function App where we will deploy our functions
# Create an Azure storage account in the resource group.
echo "Creating $storage"
az storage account create --name $storage --location "$location" --resource-group $resourceGroup --sku $skuStorage

# Create a serverless function app in the resource group.
echo "Creating $functionApp"
az functionapp create --name $functionApp --storage-account $storage --consumption-plan-location "$location" --resource-group $resourceGroup --os-type Linux --functions-version 3 --runtime python --runtime-version 3.8