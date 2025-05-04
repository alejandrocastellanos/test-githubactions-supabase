import os
import random
import string
import uuid
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")


if __name__ == "__main__":
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=10))
    email = f"{random_letters}@example.com"
    user_id = str(uuid.uuid4())
    data = {"id": user_id, "email": email}
    try:
        response = supabase.table("users").insert(data).execute()

        if response.data[0].get('id'):
            print("User added successfully:", response.data[0].get('id'))
    except Exception as e:
        print("Failed to add user:", e)
