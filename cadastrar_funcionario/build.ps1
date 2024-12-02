$exclude = @("venv", "cadastro_funcinoario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "cadastro_funcinoario.zip" -Force