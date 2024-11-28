from .conexao_supabase import pesquisar_usuario

def confirmar_usuario_qr(ra):
    usuario = pesquisar_usuario(ra)
        
    if usuario:
        usuario = {"RA": usuario["usu_ra"], "NOME": usuario["usu_nome"]}
        return usuario
    else:
        return None