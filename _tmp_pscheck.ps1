Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Select-Object ProcessId, CreationDate, @{n='Cmd';e={$_.CommandLine.Substring(0,[Math]::Min(160,$_.CommandLine.Length))}} |
  Sort-Object CreationDate | Format-Table -AutoSize | Out-String -Width 240
