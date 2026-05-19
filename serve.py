#!/usr/bin/env python3
"""Local dev server that mirrors GitHub Pages clean-URL behaviour.

GitHub Pages serves /about as about.html. Plain `python -m http.server`
doesn't. Use this instead while previewing locally.

    python3 serve.py [port]    # default port 8000
"""
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class CleanURLHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?', 1)[0].split('#', 1)[0]
        # / → /index.html (already default)
        # /experts → /experts.html if /experts.html exists and /experts (dir) doesn't
        if path != '/' and not path.endswith('/') and '.' not in path.rsplit('/', 1)[-1]:
            html_candidate = Path('.' + path + '.html')
            dir_candidate = Path('.' + path)
            if html_candidate.is_file() and not dir_candidate.is_dir():
                self.path = path + '.html' + self.path[len(path):]
        return super().do_GET()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = HTTPServer(('localhost', port), CleanURLHandler)
    print(f'Serving at http://localhost:{port}/')
    print('Clean URLs handled: /about -> about.html, /experts -> experts.html, etc.')
    print('Ctrl-C to stop.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')


if __name__ == '__main__':
    main()
