#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Detectum-OSINT PowerShell Utility - Advanced OSINT Investigation Tool
    
.DESCRIPTION
    A powerful PowerShell wrapper for Detectum-OSINT, providing enhanced features
    and better error handling for Windows users.
    
    Developed by Vishal Coodye for Detectum Cybersecurity, Republic of Mauritius
    
.PARAMETER Username
    The username to investigate across multiple platforms
    
.PARAMETER OutputFile
    Optional output file path to save results
    
.PARAMETER OutputFormat
    Output format: json or txt (default: json)
    
.PARAMETER Sites
    Specific sites to check (comma-separated)
    
.PARAMETER Verbose
    Enable verbose output
    
.EXAMPLE
    .\detectum-osint.ps1 -Username "john_doe"
    
.EXAMPLE
    .\detectum-osint.ps1 -Username "jane_smith" -OutputFile "results.txt" -OutputFormat txt
    
.EXAMPLE
    .\detectum-osint.ps1 -Username "test_user" -Sites "Facebook,Twitter,Instagram"
    
.NOTES
    Requires Python 3.10+ and Detectum-OSINT dependencies
    Run with: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Username,
    
    [Parameter(Mandatory=$false)]
    [string]$OutputFile,
    
    [Parameter(Mandatory=$false)]
    [ValidateSet("json", "txt")]
    [string]$OutputFormat = "json",
    
    [Parameter(Mandatory=$false)]
    [string]$Sites,
    
    [Parameter(Mandatory=$false)]
    [switch]$Verbose
)

# Set error action preference
$ErrorActionPreference = "Stop"

# Function to display banner
function Show-Banner {
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "   DETECTUM-OSINT - PowerShell Utility" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "   Developed by Vishal Coodye" -ForegroundColor Yellow
    Write-Host "   Detectum Cybersecurity, Republic of Mauritius" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
}

# Function to check Python installation
function Test-PythonInstallation {
    try {
        $pythonVersion = python --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
            return $true
        }
    }
    catch {
        Write-Host "❌ Python not found or not in PATH" -ForegroundColor Red
        Write-Host "Please install Python 3.10+ from https://www.python.org/downloads/" -ForegroundColor Yellow
        return $false
    }
    return $false
}

# Function to check Detectum-OSINT installation
function Test-DetectumOSINTInstallation {
    $scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
    $mainScript = Join-Path $scriptPath "detectum_osint.py"
    
    if (Test-Path $mainScript) {
        Write-Host "✅ Detectum-OSINT found: $mainScript" -ForegroundColor Green
        return $true
    }
    else {
        Write-Host "❌ Detectum-OSINT not found in current directory" -ForegroundColor Red
        Write-Host "Please ensure detectum_osint.py is in the same directory" -ForegroundColor Yellow
        return $false
    }
}

# Function to build command arguments
function Build-CommandArguments {
    $args = @($Username)
    
    if ($Sites) {
        $args += "-s"
        $args += $Sites.Split(",") | ForEach-Object { $_.Trim() }
    }
    
    if ($OutputFormat) {
        $args += "-o"
        $args += $OutputFormat
    }
    
    if ($OutputFile) {
        $args += "-f"
        $args += $OutputFile
    }
    
    if ($Verbose) {
        $args += "-v"
    }
    
    return $args
}

# Function to run investigation
function Start-Investigation {
    param([string[]]$Arguments)
    
    $scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
    $mainScript = Join-Path $scriptPath "detectum_osint.py"
    
    Write-Host "🚀 Starting investigation..." -ForegroundColor Green
    Write-Host "Command: python $mainScript $($Arguments -join ' ')" -ForegroundColor Gray
    Write-Host ""
    
    try {
        & python $mainScript @Arguments
        $exitCode = $LASTEXITCODE
        
        if ($exitCode -eq 0) {
            Write-Host ""
            Write-Host "✅ Investigation completed successfully!" -ForegroundColor Green
        }
        else {
            Write-Host ""
            Write-Host "⚠️  Investigation completed with exit code: $exitCode" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host ""
        Write-Host "❌ Investigation failed: $($_.Exception.Message)" -ForegroundColor Red
        throw
    }
}

# Main execution
try {
    # Display banner
    Show-Banner
    
    # Check prerequisites
    Write-Host "🔍 Checking prerequisites..." -ForegroundColor Blue
    
    if (-not (Test-PythonInstallation)) {
        exit 1
    }
    
    if (-not (Test-DetectumOSINTInstallation)) {
        exit 1
    }
    
    Write-Host ""
    Write-Host "✅ All prerequisites met!" -ForegroundColor Green
    Write-Host ""
    
    # Display investigation details
    Write-Host "📋 Investigation Details:" -ForegroundColor Cyan
    Write-Host "   Username: $Username" -ForegroundColor White
    Write-Host "   Output Format: $OutputFormat" -ForegroundColor White
    
    if ($Sites) {
        Write-Host "   Sites: $Sites" -ForegroundColor White
    }
    else {
        Write-Host "   Sites: All available platforms" -ForegroundColor White
    }
    
    if ($OutputFile) {
        Write-Host "   Output File: $OutputFile" -ForegroundColor White
    }
    
    Write-Host ""
    
    # Build and execute command
    $arguments = Build-CommandArguments
    Start-Investigation -Arguments $arguments
    
    # Final summary
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Investigation Summary" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Username investigated: $Username" -ForegroundColor White
    Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor White
    Write-Host "========================================" -ForegroundColor Cyan
    
    if ($OutputFile) {
        Write-Host ""
        Write-Host "📄 Results saved to: $OutputFile" -ForegroundColor Green
    }
}
catch {
    Write-Host ""
    Write-Host "❌ Error occurred: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Stack trace: $($_.ScriptStackTrace)" -ForegroundColor Red
    exit 1
}
finally {
    Write-Host ""
    Write-Host "Press any key to exit..." -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
