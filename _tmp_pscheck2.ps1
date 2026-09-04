$ids = 45572,43944,41008
foreach ($id in $ids) {
  $p = Get-CimInstance Win32_Process -Filter "ProcessId=$id" -ErrorAction SilentlyContinue
  if ($p) {
    $cl = if ($p.CommandLine) { $p.CommandLine.Substring(0,[Math]::Min(200,$p.CommandLine.Length)) } else { "(empty)" }
    Write-Output ("PID {0} | {1} | PPID {2} | {3}" -f $p.ProcessId, $p.Name, $p.ParentProcessId, $cl)
  } else { Write-Output "PID $id (exited)" }
}
Write-Output "--- powershell children of codex in last 26h ---"
Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object { $_.CreationDate -gt (Get-Date).AddHours(-26) } |
  ForEach-Object {
    $parent = Get-CimInstance Win32_Process -Filter "ProcessId=$($_.ParentProcessId)" -ErrorAction SilentlyContinue
    $pn = if ($parent) { $parent.Name } else { "exited" }
    Write-Output ("pwsh PID {0} | start {1} | parent {2} ({3})" -f $_.ProcessId, $_.CreationDate, $_.ParentProcessId, $pn)
  }
