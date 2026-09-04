Get-CimInstance Win32_Process -Filter "Name='codex.exe'" |
  ForEach-Object {
    $cl = if ($_.CommandLine) { $_.CommandLine.Substring(0,[Math]::Min(260,$_.CommandLine.Length)) } else { "(empty)" }
    Write-Output ("PID {0} | start {1} | PPID {2}" -f $_.ProcessId, $_.CreationDate, $_.ParentProcessId)
    Write-Output ("    {0}" -f $cl)
  }
