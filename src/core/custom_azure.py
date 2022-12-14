from storages.backends.azure_storage import AzureStorage


class AzureStaticStorage(AzureStorage):
    account_name = 'zemastroragev100'  # Must be replaced by your storage_account_name
    # Must be replaced by your <storage_account_key>
    account_key = 'AFsY2hZVbyYBKisEkRL+toNNJ7yBOzoJ/cruOxurFHnU84vE+Cmloq9S2ZkCxYaxrM5QemPsUiX5+ASt4WEg8w=='
    azure_container = 'zemacontainer'
    expiration_secs = None
