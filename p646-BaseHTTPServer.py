from BaseHTTPServer import BaseHTTPRequestHandler
import cgi


class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' %str(self.client_address))
        self.wfile.write('User-agent: %s\n'%str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n'%self.path)
        self.wfile.write('Form data:\n')

        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write(
                    '\tUploaded %s as "%s" (%d bytes)\n'%(field, field_item.filename, file_len))
            else:
                self.wfile.write('\t%s=%s\n'%(field, form[field].value))
        return


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), PostHandler)
    print('Starting server as 8000')
    server.serve_forever()

# curl http://localhost:8080/ -F name=wujimaster -F foo=bar

