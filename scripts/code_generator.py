#!/usr/bin/env python3
"""代码生成器"""

import re
import zipfile
from datetime import datetime
from pathlib import Path


class CodeGenerator:
    def __init__(self):
        self.output_dir = Path("./output")
        self.output_dir.mkdir(exist_ok=True)

    def extract_code(self, text):
        pattern = r'```(\w+)?\n(.*?)```'
        matches = re.findall(pattern, text, re.DOTALL)
        code_blocks = []
        for lang, code in matches:
            code_blocks.append({'language': lang or 'txt', 'code': code.strip()})
        return code_blocks

    def create_package(self, task, response):
        try:
            code_blocks = self.extract_code(response)
            
            if not code_blocks:
                output_file = self.output_dir / f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(response)
                return True, str(output_file)

            project_name = f"project_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            project_dir = self.output_dir / project_name
            project_dir.mkdir(exist_ok=True)

            ext_map = {'python': 'py', 'javascript': 'js', 'typescript': 'ts', 
                       'html': 'html', 'css': 'css', 'java': 'java', 'cpp': 'cpp'}

            for i, block in enumerate(code_blocks):
                ext = ext_map.get(block['language'], 'txt')
                filepath = project_dir / f"code_{i+1}.{ext}"
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(block['code'])

            with open(project_dir / "README.md", 'w', encoding='utf-8') as f:
                f.write(f"# {project_name}\n\n## 任务\n{task}\n\n## 生成时间\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

            zip_path = self.output_dir / f"{project_name}.zip"
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                for file in project_dir.rglob('*'):
                    if file.is_file():
                        zf.write(file, file.relative_to(project_dir))

            return True, str(zip_path)

        except Exception as e:
            return False, str(e)
