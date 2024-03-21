import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/')
def receive_get_request(name, message):
    """
    Handle GET request and return a greeting message with provided 'name' and 'message'.
    """
    greeting = f'Hello {name}! {message}'

    return PlainTextResponse(content=greeting, status_code=200)


def main():
    """
    Main function to run the application. It starts the FastAPI server.
    """
    uvicorn.run(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    print('Starting the service...')
    main()