import tkinter as tk
from pywinauto.application import Application
import os

# Criando a janela principal
janela = tk.Tk()
janela.title('Menu Windows')  # Título da janela
janela.configure(bg='#0e0e7d')  # Cor de fundo da janela

def open_bloco():
    notepad_exe = r"C:\Windows\System32\notepad.exe"
    app = Application()
    app.start(notepad_exe)

def open_calculadora():
    calc_exe = r"C:\Windows\System32\calc.exe"
    app = Application()
    app.start(calc_exe)

def open_sobre():
    """Abre a janela 'Sobre o Sistema' do Windows."""
    os.system("control.exe /name Microsoft.System")

def painel_controle():
    control_panel_exe = r"C:\Windows\System32\control.exe"
    app = Application()
    app.start(control_panel_exe)

def open_eventos():
    """Abre o Visualizador de Eventos do Windows."""
    eventvwr_exe = r"C:\Windows\System32\eventvwr.exe"
    os.startfile(eventvwr_exe)

def open_cmd():
    """Abre o Prompt de Comando do Windows."""
    cmd_exe = r"C:\Windows\System32\cmd.exe"
    os.startfile(cmd_exe)

def open_windows_update():
    """Abre o Windows Update do Painel de Controle do Windows."""
    windows_update_url = "control.exe /name Microsoft.WindowsUpdate"
    os.system(windows_update_url)

def open_explorer():
    """Abre o Explorador de Arquivos do Windows."""
    explorer_exe = r"explorer.exe"
    os.startfile(explorer_exe)

def open_settings():
    """Abre as Configurações do Sistema do Windows."""
    sysdm_exe = r"C:\Windows\System32\sysdm.cpl"
    os.startfile(sysdm_exe)

def open_dispositivos():
    """Abre o Gerenciador de Dispositivos do Windows."""
    devmgmt_exe = r"C:\Windows\System32\devmgmt.msc"
    os.startfile(devmgmt_exe)

def open_seguranca():
    """Abre a Central de Segurança do Windows."""
    wscui_exe = r"C:\Windows\System32\wscui.cpl"
    os.startfile(wscui_exe)

def open_redes():
    """Abre as Configurações de Rede do Windows."""
    ncpa_cpl = r"C:\Windows\System32\ncpa.cpl"
    os.startfile(ncpa_cpl)

def open_servicos():
    """Abre a janela de Serviços do Windows."""
    services_msc = r"C:\Windows\System32\services.msc"
    os.startfile(services_msc)

def open_imagem():
    """Abre o Visualizador de Imagens do Windows."""
    photo_viewer_exe = r"C:\Program Files\Windows Photo Viewer\PhotoViewer.dll"
    os.startfile(photo_viewer_exe)

def agendar_tarefas():
    """Abre o Agendador de Tarefas do Windows."""
    taskschd_msc = r"C:\Windows\System32\taskschd.msc"
    os.startfile(taskschd_msc)

def open_gerenciador():
    """Abre o Gerenciador de Tarefas do Windows."""
    taskmgr_exe = r"C:\Windows\System32\taskmgr.exe"
    os.startfile(taskmgr_exe)

def open_energia():
    """Abre as Configurações de Energia do Windows."""
    power_settings_cpl = r"C:\Windows\System32\powercfg.cpl"
    os.startfile(power_settings_cpl)

def open_video():
    """Abre as Configurações de Vídeo do Windows."""
    display_settings_cpl = r"C:\Windows\System32\control.exe /name Microsoft.Display"
    os.system(display_settings_cpl)

def open_firewall():
    """Abre o Firewall do Windows."""
    firewall_settings_cpl = r"C:\Windows\System32\firewall.cpl"
    os.startfile(firewall_settings_cpl)

def open_limpeza():
    """Abre a Limpeza de Disco do Windows."""
    disk_cleanup_exe = r"C:\Windows\System32\cleanmgr.exe"
    os.startfile(disk_cleanup_exe)

def open_avancado():
    """Abre as Configurações de Sistema Avançadas do Windows."""
    advanced_system_settings_cpl = r"C:\Windows\System32\SystemPropertiesAdvanced.exe"
    os.startfile(advanced_system_settings_cpl)

def open_som():
    """Abre as Configurações de Som do Windows."""
    sound_settings_cpl = r"C:\Windows\System32\mmsys.cpl"
    os.startfile(sound_settings_cpl)

def open_usuario():
    """Abre as Configurações de Conta de Usuário do Windows."""
    user_account_settings_cpl = r"C:\Windows\System32\control.exe /name Microsoft.UserAccounts"
    os.system(user_account_settings_cpl)

def open_data_hora():
    """Abre as Configurações de Data e Hora do Windows."""
    date_time_settings_exe = r"C:\Windows\System32\control.exe /name Microsoft.DateAndTime"
    os.system(date_time_settings_exe)

def open_remoto():
    """Abre o Conexão de Área de Trabalho Remota do Windows."""
    remote_desktop_exe = r"C:\Windows\System32\mstsc.exe"
    os.startfile(remote_desktop_exe)

def open_tecladomouse():
    """Abre as Configurações de Teclado e Mouse do Windows."""
    keyboard_mouse_cpl = r"C:\Windows\System32\control.exe /name Microsoft.Mouse"
    os.system(keyboard_mouse_cpl)

def open_relatorio():
    """Abre o Visualizador de Relatórios de Confiabilidade do Windows."""
    perfmon_exe = r"C:\Windows\System32\perfmon.exe /rel"
    os.system(perfmon_exe)


# Definindo o tamanho da janela
largura = 1030  # Aumentei a largura para acomodar melhor os botões
altura = 810  # Aumentei a altura para acomodar melhor os botões
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f'{largura}x{altura}+{x}+{y}')

# Configurações do Label centralizado
texto_menu = tk.Label(janela, text='Menu Windows', font=(
    'Arial', 31), fg='white', bg='#0e0e7d')
# Definindo columnspan para centralizar horizontalmente
texto_menu.grid(column=0, row=0, columnspan=4, pady=43)

# Definindo a função para mudar o estilo do botão quando o mouse entra
def on_enter(event):
    event.widget.config(bg='#0303b5', fg='white', cursor='hand2')

# Definindo a função para restaurar o estilo original do botão quando o mouse sai
def on_leave(event):
    event.widget.config(bg='#0073CF', fg='white', cursor='')

# Lista de textos para os botões
botoes = [
    {'texto': 'Teclado/Mouse', 'funcao': open_tecladomouse},
    {'texto': 'Relatório', 'funcao': open_relatorio},
    {'texto': 'Painel', 'funcao': painel_controle},
    {'texto': 'Sistema', 'funcao': open_sobre},
    {'texto': 'Eventos', 'funcao': open_eventos},
    {'texto': 'Cmd', 'funcao': open_cmd},
    {'texto': 'Atualização', 'funcao': open_windows_update},
    {'texto': 'Explorador', 'funcao': open_explorer},
    {'texto': 'Propriedades', 'funcao': open_settings},
    {'texto': 'Dispositivos', 'funcao': open_dispositivos},
    {'texto': 'Segurança', 'funcao': open_seguranca},
    {'texto': 'Redes', 'funcao': open_redes},
    {'texto': 'Serviços', 'funcao': open_servicos},
    {'texto': 'Agendador ', 'funcao': agendar_tarefas},
    {'texto': 'Gerenciar', 'funcao': open_gerenciador},
    {'texto': 'Energia', 'funcao': open_energia},
    {'texto': 'Tela', 'funcao': open_video},
    {'texto': 'Firewall', 'funcao': open_firewall},
    {'texto': 'Limpeza', 'funcao': open_limpeza},
    {'texto': 'Avançado', 'funcao': open_avancado},
    {'texto': 'Som', 'funcao': open_som},
    {'texto': 'Usuário', 'funcao': open_usuario},
    {'texto': 'Data/Hora', 'funcao': open_data_hora},
    {'texto': 'Remoto', 'funcao': open_remoto}
]

# Criando os botões dinamicamente
num_colunas = 4
botao_width = 12  # Largura padrão do botão
botao_height = -70  # Altura padrão do botão
fonte = ('Arial', 14)  # Fonte dos botões

for i, botao in enumerate(botoes):
    # Calculando linha e coluna para cada botão
    linha = i // num_colunas + 1
    coluna = i % num_colunas
    btn = tk.Button(
        janela, text=botao['texto'], 
        bg='#0073CF', fg='white',  # Configuração de cores
        font=fonte, padx=12, pady=11,
        width=botao_width, height=botao_height,  # Definindo largura e altura
        command=botao['funcao'],
        borderwidth=0  # Remover a borda do botão
    )
    btn.grid(column=coluna, row=linha, padx=48, pady=25)
    # Adicionando eventos de hover aos botões
    btn.bind('<Enter>', on_enter)
    btn.bind('<Leave>', on_leave)

# Iniciar o loop principal da janela
janela.mainloop()
