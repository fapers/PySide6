# Orientações

## Criando um novo repositório local via linha de comandos
echo "# PySide6" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/fapers/PySide6.git

git push -u origin main


## push um repositório existente via linha de comandos

git remote add origin https://github.com/fapers/PySide6.git

git branch -M main

git push -u origin main

## Outras dicas

<ul>
    <li>Para iniciar um git vazio: $ git init</li>
    <li>Para clonar o repositório git: $ git clone </li>
    <li>Para informações do repositório git: $ git status </li>
    <li>Para adicionar arquivos: $ git add .</li>
    <li>Para configurar o email do repositório atual: $ git config --global user.email "you@example.com"</li>
    <li>Para configurar o nome do usuário: $ git config --global user.name "your Name"</li>
    <li>Para commit use: $ git commit -m "mensagem informativa"</li>
    <li>Para atualizar repositório remoto github: $ git push </li>
    <li>Se erro repositório local desatualizado use: $ git pull </li>
<ul>