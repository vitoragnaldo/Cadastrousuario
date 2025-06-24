# cadastro_usuario_rich.py

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
import re

console = Console()
usuarios = {}


def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def validar_senha(senha):
    return len(senha) >= 6


def cadastrar_usuario():
    console.print(
        Panel("[bold cyan]Cadastro de Usuário[/bold cyan]", expand=False))
    nome = Prompt.ask("Digite o nome do usuário")
    while True:
        email = Prompt.ask("Digite o e-mail")
        if not validar_email(email):
            console.print("[red]E-mail inválido. Tente novamente.[/red]")
        elif email in usuarios:
            console.print("[red]E-mail já cadastrado. Tente outro.[/red]")
        else:
            break
    while True:
        senha = Prompt.ask(
            "Digite a senha (mínimo 6 caracteres)", password=True)
        if not validar_senha(senha):
            console.print("[red]Senha muito curta. Tente novamente.[/red]")
        else:
            break
    usuarios[email] = {"nome": nome, "senha": senha}
    console.print("[green]Usuário cadastrado com sucesso![/green]")


def listar_usuarios():
    if not usuarios:
        console.print("[yellow]Nenhum usuário cadastrado.[/yellow]")
        return
    table = Table(title="Usuários Cadastrados")
    table.add_column("Nome", style="cyan")
    table.add_column("E-mail", style="magenta")
    for email, dados in usuarios.items():
        table.add_row(dados["nome"], email)
    console.print(table)


def menu():
    while True:
        console.print(Panel(
            "[bold blue]Menu de Cadastro[/bold blue]\n1 - Cadastrar usuário\n2 - Listar usuários\n3 - Sair", expand=False))
        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            console.print("[bold green]Saindo...[/bold green]")
            break


if __name__ == "__main__":
    menu()
