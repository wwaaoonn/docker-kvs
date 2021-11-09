import flask, os, signal, sys

PORT = int(os.environ['PORT'])

def handle_signal(signal_number, stack_frame):
    print(f'graceful shutdown. sig number:{signal_number}')
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)

app = flask.Flask('app server')

@app.route('/api/v1/hello')
def index():
    return 'Hello stopsignal'

app.run(debug=True, host='0.0.0.0', port=PORT)
