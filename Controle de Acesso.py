# Dicionário de permissões por nível de acesso
permissoes = {
    1: "Estagiário: Acesso somente leitura a áreas de treinamento e documentos básicos.",
    2: "Júnior: Acesso de edição a projetos internos e desenvolvimento básico.",
    3: "Pleno: Acesso completo a desenvolvimento e QA (qualidade).",
    4: "Sênior: Acesso total a produção e permissões administrativas limitadas.",
    5: "Manager: Acesso completo a todos os dados e configurações da empresa."
}

# Áreas disponíveis por nível de acesso
areas = {
    1: ["Treinamento", "Documentos básicos"],
    2: ["Projetos Internos", "Desenvolvimento Básico"],
    3: ["Desenvolvimento Completo", "Qualidade (QA)"],
    4: ["Produção", "Administração Limitada"],
    5: ["Todos os dados", "Configurações da empresa"]
}

# Salário por nível de acesso
salario_por_nivel = {
    1: 100,   # Estagiário
    2: 200,   # Júnior
    3: 300,   # Pleno
    4: 400,   # Sênior
    5: 500    # Manager
}

# Lista de usuários cadastrados
usuarios = [
    {"nome": "admin", "senha": "1234", "nivel": 5}  # Usuário inicial para poder cadastrar outros
]

# Função para encontrar um usuário pelo nome
def encontrar_usuario(nome):
    for usuario in usuarios:
        if usuario["nome"] == nome:
            return usuario
    return None

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuario_logado):
    if usuario_logado["nivel"] < 4:
        print("Permissão negada! Somente usuários Sênior ou Manager podem cadastrar novos usuários.\n")
        return

    nome = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")
    nivel = int(input("Digite o nível de acesso (1-Estagiário, 2-Júnior, 3-Pleno, 4-Sênior, 5-Manager): "))

    if nivel in permissoes:
        novo_usuario = {"nome": nome, "senha": senha, "nivel": nivel}
        usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso!\n")
    else:
        print("Nível de acesso inválido. Tente novamente.\n")

# Função para consultar informações de um usuário
def consultar_usuario():
    nome_consulta = input("Digite o nome do usuário para consulta: ")
    usuario = encontrar_usuario(nome_consulta)
    
    if usuario:
        nivel = usuario["nivel"]
        print(f"Nome: {usuario['nome']}")
        print(f"Nível de acesso: {nivel} - {permissoes[nivel]}")
    else:
        print("Usuário não encontrado.\n")

# Função para exibir áreas de acesso de acordo com o nível
def escolher_area_acesso(usuario_logado):
    nivel = usuario_logado["nivel"]
    print("\nÁreas disponíveis para seu nível de acesso:")
    for i, area in enumerate(areas[nivel], start=1):
        print(f"{i}. {area}")
    opcao = int(input("Escolha uma área para acessar (número): "))
    
    if 1 <= opcao <= len(areas[nivel]):
        print(f"Você entrou na área: {areas[nivel][opcao - 1]}")
    else:
        print("Opção inválida. Tente novamente.\n")

# Função de trabalho para gerar dinheiro baseado no nível de acesso
def trabalho(usuario_logado):
    nivel = usuario_logado["nivel"]
    salario = salario_por_nivel.get(nivel, 0)
    print(f"Você trabalhou e ganhou R${salario}. Nível de acesso: {nivel} - {permissoes[nivel]}\n")

# Função para realizar o login
def login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    usuario = encontrar_usuario(nome)
    
    if usuario and usuario["senha"] == senha:
        print(f"Bem-vindo, {usuario['nome']}! Nível de acesso: {usuario['nivel']} - {permissoes[usuario['nivel']]}")
        return usuario
    else:
        print("Usuário ou senha incorretos.\n")
        return None

# Função principal do sistema
def sistema():
    usuario_logado = None
    while True:
        # Se o usuário não estiver logado, pede login
        if not usuario_logado:
            print("=== Login no Sistema ===")
            usuario_logado = login()
            if not usuario_logado:
                continue  # Continua pedindo login se falhar

        # Menu principal após login
        print("\n1. Escolher área de acesso")
        print("2. Trabalhar")  # Nova opção de trabalho

        # Exibe a opção de cadastrar usuário apenas para níveis >= 4 (Sênior e Manager)
        if usuario_logado["nivel"] >= 4:
            print("3. Cadastrar usuário")
        
        # Exibe a opção de consultar usuário para todos os níveis
        print("4. Consultar usuário")
        
        print("5. Deslogar")
        print("6. Sair do sistema")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            escolher_area_acesso(usuario_logado)
        elif opcao == '2':
            trabalho(usuario_logado)
        elif opcao == '3' and usuario_logado["nivel"] >= 4:
            cadastrar_usuario(usuario_logado)
        elif opcao == '4':
            consultar_usuario()
        elif opcao == '5':
            print("Deslogando...\n")
            usuario_logado = None
        elif opcao == '6':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciar o sistema
sistema()