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

    # Implement here your logic...
    bot.browse("https://api.crmsc.org.br/aplicacoes/#/login")

    if not bot.find( "acessarCentral", matching=0.97, waiting_time=30000):
        not_found("acessarCentral")
    bot.click()
    
    if not bot.find( "interact", matching=0.97, waiting_time=30000):
        not_found("interact")
    bot.click()
    
    if not bot.find( "usuarioInteract", matching=0.97, waiting_time=30000):
        not_found("usuarioInteract")
    bot.click_relative(20, 35)    
    
    if not bot.find( "userName", matching=0.97, waiting_time=30000):
        not_found("userName")
    bot.click()

    if not bot.find( "ramalNum", matching=0.97, waiting_time=30000):
        not_found("ramalNum")
    bot.click_relative(104, 34)
    bot.kb_type("5009")
    
    if not bot.find( "entrarInteract", matching=0.97, waiting_time=30000):
        not_found("entrarInteract")
    bot.click()
    
    if not bot.find( "senhaInteract", matching=0.97, waiting_time=30000):
        not_found("senhaInteract")
    bot.click_relative(59, 10)
    bot.kb_type("Aa123456")
    
    if not bot.find( "ok", matching=0.97, waiting_time=30000):
        not_found("ok")
    bot.click()
    
    if not bot.find( "permitir", matching=0.97, waiting_time=30000):
        not_found("permitir")
    bot.wait(3000)
    bot.click()
    
    if not bot.find( "inoperante", matching=0.97, waiting_time=30000):
        not_found("inoperante")
    bot.click()
    
    if not bot.find( "operando", matching=0.97, waiting_time=30000):
        not_found("operando")
    bot.click()
    
    if not bot.find( "minimizar", matching=0.97, waiting_time=30000):
        not_found("minimizar")
    bot.click_relative(-11, -30)
    
    if not bot.find( "fecharLoginInteract", matching=0.97, waiting_time=30000):
        not_found("fecharLoginInteract")
    bot.click_relative(60, 3)
    
    if not bot.find( "una", matching=0.97, waiting_time=30000):
        not_found("una")
    bot.click()
    
    if not bot.find( "usuarioUNA", matching=0.97, waiting_time=30000):
        not_found("usuarioUNA")
    bot.click()
    
    if not bot.find( "selecionarUsuario", matching=0.97, waiting_time=30000):
        not_found("selecionarUsuario")
    bot.click()
    
    if not bot.find( "entrar", matching=0.97, waiting_time=30000):
        not_found("entrar")
    bot.click()
    
    if not bot.find( "permitir", matching=0.97, waiting_time=30000):
        not_found("permitir")
    bot.click()
    
    if not bot.find( "voltarCentralAplicacoes", matching=0.97, waiting_time=30000):
        not_found("voltarCentralAplicacoes")
    bot.click()
    
    if not bot.find( "clicarPagina", matching=0.97, waiting_time=30000):
        not_found("clicarPagina")
    bot.click()
    bot.scroll_down(200)

    if not bot.find( "itManager", matching=0.97, waiting_time=30000):
        not_found("itManager")
    bot.click()
    
    if not bot.find( "deVoltaCentralAplicacoes", matching=0.97, waiting_time=30000):
        not_found("deVoltaCentralAplicacoes")
    bot.click()

    if not bot.find( "verItManager", matching=0.97, waiting_time=30000):
        not_found("verItManager")
    bot.click_relative(-49, 34)
    bot.scroll_down(10)

    if not bot.find( "zimbra", matching=0.97, waiting_time=30000):
        not_found("zimbra")
    bot.click()
    
    if not bot.find( "login", matching=0.97, waiting_time=30000):
        not_found("login")
    bot.click()   
    
    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()






