# Zap dos cria

# Legendas:
# pubsub é o tunel de mensagens (é por causa dele que o chat funcinoa)
# def é definir alguma coisa
# os {} serve para criar um dicionario no python, ajuda na hora de pegar coisas específicas
# "f" é para formatação de algum texto
# pagina.update() serve pra sempre atualizar quando algo no código acontecer    

import flet as ft

def main(pagina):
    texto = ft.Text("Zap dos cria", size=28, color=ft.colors.INDIGO_ACCENT)

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    # A mensagem que você entrou no chat
    def enviar_mensagem_tunel(mensagem):

        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # Adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else: 
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat",
                                         size = 12, italic = True, color = ft.colors.GREEN_ACCENT ))
                                 
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):

        # A cada mensagem que você envia (aparece para todo mundo)
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})

        # Limpar o campo de mensagem
        campo_mensagem.value = ""

        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):

        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        
        pagina.add(chat)
        
        # Fechar o popup
        popup.open = False
        # Remover o botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # Criar o campo de mensagem do usuário
        # Criar o botão de enviar mensagem do usuário
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()
    # Popup para entrar no chat
    popup = ft.AlertDialog(
        open = False,
        modal = True, 
        title = ft.Text("Ó o Zap dos Cria"), 
        content = nome_usuario, 
        actions = [ft.ElevatedButton("Entrar", on_click=entrar_popup)]
    )

    def entrar_chat(evento):

       pagina.dialog = popup
       popup.open = True
       pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)
    # Botão de iniciar o chat
    pagina.add(texto)
    pagina.add(botao_iniciar)
    

ft.app(target=main, view=ft.WEB_BROWSER)