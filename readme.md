## python3 -m venv venv
§       aqswdefrgtp-[=Analogy 
python3 -m venv venv          # "Make me my own toy box!"
source venv/bin/activate      # "I'm playing with MY toys now"
pip install fastapi           # "Put this toy in MY box"
deactivate                    # "I'm done, putting toys away"

# java equivalent 
# Create a new Maven/Gradle project
mvn archetype:generate       # Creates project structure

# Dependencies in pom.xml are project-specific
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>

# Maven downloads dependencies to project's local scope
mvn clean install

# this is ur swagger ui 
http://127.0.0.1:8000/docs

# what is fast api -- fast api is a framework to write apis in python

# what is poetry 
Poetry is a modern dependency management and packaging tool for Python — 
think of it as the “Maven + virtualenv + pip + versioning + packaging” all in one.
It handles everything needed to build, run, and distribute a clean, production-grade Python project.

| Task                    | In Java                           | In Python (Old Way)                         | With Poetry                        |
| ----------------------- | --------------------------------- | ------------------------------------------- | ---------------------------------- |
| Manage dependencies     | Maven (`pom.xml`)                 | `requirements.txt` + `venv` + `pip install` | `pyproject.toml`                   |
| Isolate environments    | JVM handles dependencies globally | Manual virtualenv creation                  | Poetry auto-manages isolated venvs |
| Build / package project | `mvn package`, `jar`, `install`   | Custom scripts                              | `poetry build` / `poetry publish`  |
| Version / metadata      | Maven coordinates                 | `setup.py`, `setup.cfg`                     | Automatically tracked              |
| Run scripts             | `java -jar ...`                   | `python main.py`                            | `poetry run python main.py`        |




