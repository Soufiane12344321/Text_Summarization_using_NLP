from pathlib import Path
import os

def create_project_structure():
    project_name = "text_summarization"
    
    # List of directories to create
    directories = [
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "src/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb",
        "templates/index.html",
        "test/test_app.py"
    ]
    
    for filepath in directories:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        
        if filedir:
            os.makedirs(filedir, exist_ok=True)
            
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                pass

if __name__ == "__main__":
    create_project_structure()