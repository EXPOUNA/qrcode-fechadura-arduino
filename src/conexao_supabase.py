from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL, SUPABASE_KEY  = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def pesquisar_usuario(uuid):
    try:
        response = supabase.table("Usuarios_UNA").select("*").eq("id", uuid).execute()
        if response.data:
            return response.data[0]
        else:
            return None
    except Exception as e:
        print(f"conexao_supabase - Ocorreu um erro: {e}")
        return None