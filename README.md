# Byte in Space 🐶🚀💫

## Equipe 🧑‍💻
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gustavocharamba">
        <img src="https://avatars.githubusercontent.com/gustavocharamba" width="100px;" alt="Gustavo Charamba"/><br />
        <sub><b>Gustavo Charamba</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lgss0">
        <img src="https://avatars.githubusercontent.com/lgss0" width="100px;" alt="lgss0"/><br />
        <sub><b>lgss0</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SmouraCodeX">
        <img src="https://avatars.githubusercontent.com/SmouraCodeX" width="100px;" alt="SmouraCodeX"/><br />
        <sub><b>SmouraCodeX</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lebb8">
        <img src="https://avatars.githubusercontent.com/lebb8" width="100px;" alt="lebb8"/><br />
        <sub><b>lebb8</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/luizmiguelbarbosa">
        <img src="https://avatars.githubusercontent.com/luizmiguelbarbosa" width="100px;" alt="Luiz Miguel Barbosa"/><br />
        <sub><b>Luiz Miguel Barbosa</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/miqueias-santos">
        <img src="https://avatars.githubusercontent.com/miqueias-santos" width="100px;" alt="Luiz Miguel Barbosa"/><br />
        <sub><b>Miqueuias Santos</b></sub>
  </tr>
</table>

## Instalando o jogo ⚙️🛠️

Clone o repositório
```bash
git clone https://github.com/luizmiguelbarbosa/byte_in_space.git
```
No PowerShell, execute:
```bash
Set-ExecutionPolicy RemoteSigned -Scope Process
& byte_in_space/venv/Scripts/Activate.ps1
```
```bash
cd byte_in_space
```
```bash
pip install -r requirements.txt
```
## Estruturas de Pastas 📂
Arquitetura de Pastas do Projeto
### entites
Classes das entidades do jogo. Ex: `Player`, `Inimigos` e `Coletáveis`
```bash
├── entities
│   ├── coletavel.py
│   ├── eventos.py
│   ├── inimigo.py
│   ├── nave.py
│   ├── render.py
│   └── update.py
```
### assets
Arquivos de assets do jogo. Ex: `Imagens`, `Músicas` e `Vídeos`
```bash
├── assets
│   ├── imagens
│   │   ├── cenario1.png
│   │   ├── circuito.png
│   │   ├── computador.png
│   │   ├── dados.png
│   │   ├── icone_janela.png
│   │   ├── imagem_menu.png
│   │   ├── sprite_inimigo.png
│   │   └── sprite_nave.png
│   ├── musicas
│   │   ├── musica_jogo.mp3
│   │   ├── musica_start.mp3
│   │   └── tiro.mp3
│   └── videos
│       └── cutscene1.mp4
```
## Capturas de Tela 🎮📸
<p align="center">
  <img src="assets/caputuras/1.png" alt="Captura 1" width="300">
  <img src="assets/caputuras/2.png" alt="Captura 2" width="300">
  <img src="assets/caputuras/3.png" alt="Captura 3" width="300">
</p>

## Bibliotecas Utilizadas
```bash
pygame 2.6.1
openCV2 4.12.0
```
## Divisão de Tarefas do Projeto 🌌

<div style="background-image: url('https://www.transparenttextures.com/patterns/stardust.png'); background-color: #000; padding: 15px; border-radius: 10px;">

<table style="width: 100%; border-collapse: collapse; color: white;">
  <tr>
    <th style="border: 1px solid white; padding: 8px;">Time</th>
    <th style="border: 1px solid white; padding: 8px;">Tarefas</th>
  </tr>
  <tr>
    <td style="border: 1px solid white; padding: 8px;"><a href="https://github.com/gustavocharamba?tab=overview&from=2025-08-01&to=2025-08-11" style="color: #FFD700;">Gustavo Charamba</a></td>
    <td style="border: 1px solid white; padding: 8px;">Desenvolveu estados de controle do jogo e lógica envolvendo itens e inventário</td>
  </tr>
  <tr>
    <td style="border: 1px solid white; padding: 8px;"><a href="https://github.com/lgss0" style="color: #FFD700;">lgss0</a></td>
    <td style="border: 1px solid white; padding: 8px;">Desenvolveu todas as responsividades do jogo</td>
  </tr>
  <tr>
    <td style="border: 1px solid white; padding: 8px;"><a href="https://github.com/SmouraCodeX" style="color: #FFD700;">SmouraCodeX</a></td>
    <td style="border: 1px solid white; padding: 8px;">Desenvolveu telas iniciais, créditos, game over e mecânica de tiros com o mouse</td>
  </tr>
  <tr>
    <td style="border: 1px solid white; padding: 8px;"><a href="https://github.com/lebb8" style="color: #FFD700;">lebb8</a></td>
    <td style="border: 1px solid white; padding: 8px;">Desenvolveu colisões entre todos os objetos do projeto</td>
  </tr>
  <tr>
    <td style="border: 1px solid white; padding: 8px;"><a href="https://github.com/luizmiguelbarbosa" style="color: #FFD700;">luizmiguelbarbosa</a></td>
    <td style="border: 1px solid white; padding: 8px;">Principal code reviewer, desenvolveu a classe base de entidades e movimentação do player</td>
  </tr>
  <tr>
    <td style="border: 1px solid white; padding: 8px;"><a href="https://github.com/miqueias-santos" style="color: #FFD700;">miqueias-santos</a></td>
    <td style="border: 1px solid white; padding: 8px;">Auxiliou no design e contribuiu para otimizações de desempenho do projeto</td>
  </tr>
</table>

</div>


