# RidesApp-Web
_Welcome to the Tap App! The purpose of this application is to help people arrange rides easier to any event. This code base consists of the REST API which will be used by the mobile application and the ui of the web application. For more information, please visit our [Notion Page](https://dylanwong.notion.site/TapRide-0f8f6dca71ac447fa6b77a3388544f0a)!_

* [Required Dependencies](#required-dependencies)
* [Getting Started](#getting-started)
* [UI](#ui)

---

## Required Dependencies
* [Docker](https://docs.docker.com/get-docker/)
* An Integrated Development Environment (IDE) such as [Visual Studio Code](https://code.visualstudio.com/download) or [Sublime](https://www.sublimetext.com/3)

---

## Getting Started
_Steps to get the local development environment running on your machine:_
1. Create a `.env.dev` file in `api/env/`, copy the contents of `.env.example` into it. Ask any member of the team for the values of the secrets.
2. Start the docker containers in dev mode by running the following command in the root directory:

    ```bash
    docker-compose --env-file ./api/env/.env.dev up
    ```
    * If this is the first time spinning up the containers, it may take a few minutes to download all the requirements.
    * Sometimes, docker-compose won't build something because it thinks an image is up to date. To force a build, either delete the images or add `--build api` after the command.
3. Access the frontend by going to localhost:3000.
4. To run a psql shell instance, get into the api shell:
    ```bash
    docker exec -it ridesapp-web_db_1 bash
    ```
    Connect to the database we defined in the `docker-compose.yml` on the "host" named `db`:
    ```bash
    psql -h db -d postgres -U servant
    ```

---

## UI
_Everything related to the front end of the web application, from file structure to testing._
### File Architecture
The `front` folder holds everything front end related. Inside the `src` directory, components are layed out in a tree structure— with each folder holding components for that page. The exception to this is the `common` folder, which holds components that show on all / more than one page. Examples of this include the header, user tag, etc. Within these folders components may be grouped more depending on a nested components relation to the folder its in. If a component is exclusively used by another, it should be grouped with that other component.

### Testing
Jest is used to test this application and as always all new code should strive for 100% code coverage. Every component should have a testing file associated, ending with `.test.js`.
