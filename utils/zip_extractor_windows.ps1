[Environment]::CurrentDirectory = (Get-Location -PSProvider FileSystem).ProviderPath
Add-Type -Assembly System.IO.Compression.FileSystem
$compressionLevel = [System.IO.Compression.CompressionLevel]::Optimal
[System.IO.Compression.ZipFile]::CreateFromDirectory(".\dist", "extractor-windows.zip" , $compressionLevel, $false)
