# Define the subnet to scan
$subnet = "10.0.0."

# Define the addresses to exclude (modify this as needed)
$exclude = @("10.0.0.3", "10.0.0.4")

# Loop through the range of IP addresses
1..254 | ForEach-Object {
    $ip = $subnet + $_
    if ($exclude -notcontains $ip) {
        if (Test-Connection -ComputerName $ip -Count 2 -Quiet) {
            Write-Host "$ip is up"
        } else {
            Write-Host "$ip is down"
        }
    }
}
