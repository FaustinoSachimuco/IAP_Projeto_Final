#!/bin/bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python_script="$script_dir/get_html.py"

if [ -f "$python_script" ]; then
  python "$python_script"
  echo "Python Script $python_script started"

  cd "$script_dir"
  git add .
  commit_message="Auto commit at $(date +'%Y-%m-%d')"
  git commit -m "$commit_message"
  git push origin main
  echo "Files html pushed to Github"

else
  echo "Error: Python Script not found at $python_script"
fi 
