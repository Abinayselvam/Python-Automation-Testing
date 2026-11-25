from Day04_API_Automation.framework.base_api import BaseAPI


class NotebookClient(BaseAPI):

    def create_notebook(self, payload):
        return self.post("/api/notebooks", payload)

    def get_notebook(self, notebook_id):
        return self.get(f"/api/notebooks/{notebook_id}")

    def update_notebook(self, notebook_id, payload):
        return self.patch(
            f"/api/notebooks/{notebook_id}",
            payload
        )

    def delete_notebook(self, notebook_id):
        return self.delete(f"/api/notebooks/{notebook_id}")