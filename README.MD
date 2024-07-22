
Mandatory env variables to define:

You have to add a .env (used by dotenv python module) file with following variables :

- BASE_URL : url to sauce demo labs web site

4 Layers of the framework :

- scenario written in gherkin composed of steps 
  - step implementation that calls one or more functionnal actions (no technical pw stuff here). A given set a precondition and assert that precondition is ok. A when, do an action without asserting anything. A Then just do an assertion, no action in here.
    - Action & Assertion classes : high level classes and methods that uses page object classes to do functional user stuff
      - page object classes : low level interaction with the UI. knows how to locate elements and interact with them. PW is here
