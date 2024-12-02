"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    #----------------------------------------------------------------------------
    # Implement here your logic...
    # Bot procura por Remote Desktop
    bot.execute("C:\windows\system32\mstsc")
    if not bot.find( "conectar_volvo", matching=0.97, waiting_time=10000):
        not_found("conectar_volvo")
    bot.click()

    if not bot.find( "ok_volvo", matching=0.97, waiting_time=10000):
        not_found("ok_volvo")
    bot.click()
    
    # Encontrando o active directory
    bot.type_windows()
    bot.kb_type("usuário", 10)
    bot.enter()
    bot.wait(3000)

    if not bot.find( "crmsc.ad_folder", matching=0.97, waiting_time=10000):
        not_found("crmsc.ad_folder")
    bot.click()
    
    if not bot.find( "CRMSC_folder", matching=0.97, waiting_time=10000):
        not_found("CRMSC_folder")
    bot.click(clicks = 2)
    
    if not bot.find( "Usuários_folder", matching=0.97, waiting_time=10000):
        not_found("Usuários_folder")
    bot.click(clicks = 2)
    
    # Encontrando o setor
    setor = input("Selecione o setor que deseja inserir o novo funcionário:")
    match setor:
        case "Sindicância":
            if not bot.find( "open_sindicancia", matching=0.97, waiting_time=10000):
                not_found("open_sindicancia")
            bot.click(clicks = 2)
            
            if not bot.find( "user_sindicancia", matching=0.97, waiting_time=10000):
                not_found("user_sindicancia")
            bot.click(clicks = 2)
            
            copiar = input("Qual o funcionário que deseja copiar os acessos windows:")
            if not bot.find_text( "find_name_copy", threshold=230, waiting_time=10000):
                not_found("find_name_copy")
            
                
        
            
    #     case "Pessoa Jurídica":

    #     case "Codame":

    # Setores a selecionar:
    # 1 - Sindicância
    # 2 - Assessoria de Imprensa
    # 3 - Assessoria Jurídica (Administrativa)
    # 4 - Assessoria Jurídica (Corregedoria)
    # 5 - CODAME
    # 6 - Conselheiros
    # 7 - Contabilidade
    # 8 - Controladoria
    # 9 - Corregedoria
    # 10 - Delegacias
    # 11
    # 12
    # 13
    # 14
    # 15
    # 16
    # 17
    # 18
    # 19
    # 20
    # 21
    # 22
    # 23
    # 24
    # 25
    # 26
    # 27
    # 28
    # 29
    # 30
    
    
    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def abrir_active_directory(label):
    bot = DesktopBot()
    if (not bot.find( label)):
        if not bot.find( "open_active_directory", matching=0.97, waiting_time=10000):
            not_found("open_active_directory")
        bot.click()
        print("cheguei até aqui")
    else:
        print("cheguei")
        

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()








