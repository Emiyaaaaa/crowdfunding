import BaseHTTPServer,os

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    # Page = '''\
    # <html>
    # <body>
    # <table>
    # <tr>  <td>Header</td>         <td>Value</td>          </tr>
    # <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    # <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    # <tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
    # <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    # <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    # </table>
    # </body>
    # </html>
    # '''
    Error_Page = """\
            <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            </body>
            </html>
            """



    # def do_GET(self):
    #     page = self.create_page()
    #     self.send_page(page)

    # def create_page(self):
    #     values = {
    #         'date_time': self.date_time_string(),
    #         'client_host': self.client_address[0],
    #         'client_port': self.client_address[1],
    #         'command': self.command,
    #         'path': self.path
    #     }
    #     page = self.Page.format(**values)
    #     return page

    # def send_page(self, page):
    #     self.send_response(200)
    #     self.send_header("Content-type", "text/html")
    #     self.send_header("Content-Length", str(len(page)))
    #     self.end_headers()
    #     self.wfile.write(page)

    def do_GET(self):
        try:

            # Figure out what exactly is being requested.
            self.full_path = os.getcwd() + self.path

            # Figure out how to handle it.
            for case in self.Cases:
                handler = case()
                if handler.test(self):
                    handler.act(self)
                    break

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)



if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()