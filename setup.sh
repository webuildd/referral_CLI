#!/bin/bash

echo "🔧 Setting up Referral Email CLI Tool..."

# Step 1: Create virtual environment
if [ ! -d "venv" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv venv
else
  echo "✅ Virtual environment already exists."
fi

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install jinja2 pyyaml

# Step 4: Show directory structure hint
echo "Make sure you have the following structure:"
echo "├── main.py"
echo "├── config.yaml"
echo "├── templates/referral_email.txt.j2"
echo "├── data/employees.csv"
echo "├── utils/*.py"
echo "└── sent_log.csv (auto-created)"

# Step 5: Run the CLI tool
echo "🚀 Running the CLI tool..."
python main.py --config config.yaml

# Optional: Deactivate venv after execution
# deactivate
