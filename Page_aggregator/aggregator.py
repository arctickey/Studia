from app import app,db
from app.models import Content


@app.shell_context_processor
def make_shell_context():
    return {'db': db,'Content':Content,'delete':Content.delete()}



if __name__ == "__main__":
    app.run()