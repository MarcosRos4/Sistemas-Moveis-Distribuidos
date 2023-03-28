#url da api "https://qdjlfevwzqslxsmgrthu.supabase.co" 
#key da api "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFkamxmZXZ3enFzbHhzbWdydGh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAwMzA3MzAsImV4cCI6MTk5NTYwNjczMH0.bC9NnTX1jRB9h6FSOMq73gQVkGzvoaA3YxN4sVFV6wY"


from flask import Flask, jsonify, request
from supabase.client import create_client, Client


url: str = "https://qdjlfevwzqslxsmgrthu.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFkamxmZXZ3enFzbHhzbWdydGh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAwMzA3MzAsImV4cCI6MTk5NTYwNjczMH0.bC9NnTX1jRB9h6FSOMq73gQVkGzvoaA3YxN4sVFV6wY"
supabase: Client = create_client(url, key)

app = Flask(__name__)


#retornar informações da tabela vinho de um vinho específico: nome, safra, tipo, valor
@app.route('/vinhos/acessar-por-id/<vinho_id>',methods=['GET'])
def acessar_vinho_por_id(vinho_id):
    [vinho] = supabase.table('vinhos').select("*").eq("vinho_id",vinho_id).execute().data
    
    print(vinho, vinho_id)
    return jsonify(vinho)

# retornar informações da tabela vinhos de todos os vinhos: nome, safra, tipo, valor
@app.route('/vinhos/acessar-todos/',methods=['GET'])
def acessar_todos_vinhos():
    vinho = supabase.table('vinhos').select("*").execute().data
    return jsonify(vinho)

# deletar vinho baseado em seu vinho_id
@app.route('/vinhos/deletar-por-id/<vinho_id>',methods=['DELETE'])
def deletar_vinho_por_id(vinho_id):
    [vinho] = supabase.table('vinhos').delete().eq("vinho_id",vinho_id).execute().data
    return "Vinho:{} Vinho_Id:{} deletado".format(vinho["nome"], vinho["vinho_id"])

# atualizar vinho
@app.route('/vinhos/atualizar/<vinho_id>', methods=['PUT'])
def atualizar_vinho_por_id(vinho_id):
    infovinho= request.get_json()
    
    [vinho] =supabase.table("vinhos").update({"nome":infovinho["nome"],
                                    "safra": infovinho["safra"],
                                    "nome_fazenda":infovinho["nome_fazenda"],
                                    "tipo":infovinho["tipo"],
                                    "valor":infovinho["valor"]}).eq("vinho_id", vinho_id).execute().data

    return "Vinho:{} Vinho_Id:{} atualizado".format(vinho["nome"], vinho["vinho_id"])

# criar vinho
@app.route('/vinhos/criar',methods=['POST'])
def criar_vinho():
    infovinho= request.get_json()
    [vinho] =supabase.table("vinhos").insert({"nome":infovinho["nome"],
                                    "safra": infovinho["safra"],
                                    "nome_fazenda":infovinho["nome_fazenda"],
                                    "tipo":infovinho["tipo"],
                                    "valor":infovinho["valor"]}).execute().data

    return "vinho:{} vinho_Id: {} criado ".format(vinho["nome"], vinho["vinho_id"])

# retornar informações da tabela usuarios de um usuario especifico: nome, telefone, email, senha
@app.route('/usuarios/acessar-por-id/<user_id>',methods=['GET'])
def acessar_usuario_por_id(user_id):
    [user] = supabase.table('usuarios').select("*").eq("user_id",user_id).execute().data
    
    print(user, user_id)
    return jsonify(user)

# retornar informações da tabela usuarios de todos os usuarios: nome, telefone, email, senha
@app.route('/usuarios/acessar-todos',methods=['GET'])
def acessar_todos_usuarios():
    user = supabase.table('usuarios').select("*").execute().data

    return jsonify(user)

# deletar usuario baseado em seu user_id
@app.route('/usuarios/deletar-por-id/<user_id>',methods=['DELETE'])
def deletar_usuario_por_id(user_id):
    [user] = supabase.table('usuarios').delete().eq("user_id",user_id).execute().data
    
    
    return "User:{} User_Id:{} deleted".format(user["nome"], user["user_id"])

# atualizar usuario 
@app.route('/usuarios/atualizar/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    infousuario= request.get_json()
    print(user_id, infousuario)
    [user] =supabase.table("usuarios").update({"nome":infousuario["nome"],
                                    "telefone": infousuario["telefone"],
                                    "email":infousuario["email"],
                                    "senha":infousuario["senha"]}).eq("user_id", user_id).execute().data
    
    return "User:{} Id:{} updated".format(user["nome"], user["user_id"])

# criar usuario
@app.route('/usuarios/criar',methods=['POST'])
def create_user():
    infousuario= request.get_json()
    print(infousuario)
    print(infousuario["nome"])
    [user] =supabase.table("usuarios").insert({"nome":infousuario["nome"],
                                    "telefone": infousuario["telefone"],
                                    "email":infousuario["email"],
                                    "senha":infousuario["senha"]}).execute().data

    return "User:{} User_Id: {} created ".format(user["nome"], user["user_id"])

app.run(port=5000,host='localhost',debug=True)
