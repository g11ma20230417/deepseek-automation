#!/usr/bin/env python3
"""跨平台部署器"""

import os
import http.server
import socketserver
import threading
from pathlib import Path


class CrossPlatformDeployer:
    def __init__(self):
        self.server = None
        self.port = 8080

    def deploy(self, package_path, method='local'):
        try:
            if method == 'local':
                return self._start_local_server(package_path)
            return {'success': False, 'error': '未知部署方法'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def _start_local_server(self, package_path):
        package_name = Path(package_path).name
        os.chdir(str(Path(package_path).parent))

        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=str(Path(package_path).parent), **kwargs)

        self.server = socketserver.TCPServer(("0.0.0.0", self.port), Handler)
        
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()

        return {
            'success': True,
            'data': {
                'url': f"http://localhost:{self.port}/{package_name}",
                'port': self.port
            }
        }
