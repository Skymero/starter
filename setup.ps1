# Check if the virtual environment directory exists
if (Test-Path -Path "venv") {
    Write-Output "Activating existing virtual environment..."
    .\venv\Scripts\Activate.ps1
} else {
    Write-Output "Creating a new virtual environment..."
    python3.10 -m venv venv
    .\venv\Scripts\Activate.ps1
    Write-Output "Virtual environment created and activated."
}

# Install dependencies from requirements.txt if it exists
if (Test-Path -Path "requirements.txt") {
    Write-Output "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Output "No requirements.txt found. Skipping dependency installation."
}
