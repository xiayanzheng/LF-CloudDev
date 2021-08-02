from azure.storage.blob import ContainerClient as cc


class Upload:

    def __init__(self):
        self.sas = ""
        self.container = None

    def create_cc(self):
        self.container = cc.from_container_url(self.sas)
        print("Blob Container Client Created")

    def list_c_b(self):
        blobs_list = self.container.list_blobs()
        print("[Start]List of blob in Container")
        for blob in blobs_list:
            print(blob.name + '\n')
        print("[End]List of blob in Container")

    def upload_file(self):
        file = "SampleSourceRMM.txt"
        file_name = "SampleSourceRMM.txt"
        print("[Start]Upload File {}".format(file_name))
        with open(file, "rb") as data:
            blob_client = self.container.upload_blob(name=file_name, data=data)
        properties = blob_client.get_blob_properties()
        print("[End]Upload File {}".format(file_name))


up = Upload()
up.create_cc()
up.upload_file()
