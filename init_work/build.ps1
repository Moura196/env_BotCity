$exclude = @("venv", "init_work.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "init_work.zip" -Force