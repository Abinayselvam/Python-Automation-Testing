from Day04_API_Automation.framework.base_api import BaseAPI


class ChatClient(BaseAPI):

    def create_chat(self, payload):

        return self.post(
            "/api/chats",
            payload
        )

    def get_chat(self, chat_id):

        return self.get(
            f"/api/chats/{chat_id}"
        )

    def delete_chat(self, chat_id):

        return self.delete(
            f"/api/chats/{chat_id}"
        )