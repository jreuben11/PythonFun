import nox

@nox.session(python=["3.11.2"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")