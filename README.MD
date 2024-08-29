The purpose of this repo is to show my capabilities in developping a test automation framework from scratch using python and playwright. The idea is also to enhance my skills, get feedbacks thus continue to learn and apply those learnings.

The SUT (system under test) used is : https://www.saucedemo.com/

## Framework organisation description

4 Layers of the framework :

- scenario written in gherkin composed of steps (**features** folder). They are the end 2 end tests (feature level)

  - step implementation that calls one or more functionnal actions (no technical pw stuff here). A given set a precondition and assert that precondition is ok. A when, do an action without asserting anything. A Then just do an assertion, no action in here. (**feature/steps** folder)

    - Action & Assertion classes : high level classes and methods that uses page object classes to do functional user stuff. (**actions** folder)

      - page object classes : low level interaction with the UI. knows how to locate elements and interact with them. PW is here. (**page_objects** folder)

- component test : purpose of those tests is to regression check one page at a time, meaning, output from that page and inputs to that page should be mocked. They can be run very early (by developers in local env and against front end build on CI) to give early feedback. They are short, fast and covers all interactions that a user do on a page.
They can be positif or negative. (**component_tests** folder). Using pytest to write them. They use actions classes to interact with the UI. This mutualizes the effort for building POM and Actions classes.

- Should also have something like Acceptance tests that are automation of user story's acceptance criteria(s) (Behavior Driven Development)

## Prerequisites

- Python 3.10
- a virtual env manager

## Install

1. Clone the repository
2. Create and activate a virtual env
3. Install required packages

```bash
    pip install .
```
4. Define env variables

Just copy the .env_sample, rename it to .env. it contains one env variable :

- BASE_URL : url to sauce demo labs web site

## Run tests

End to end tests :

```bash
    behave
```

Component tests

```bash
    pytest --headed --full-page-screenshot --base-url https://www.saucedemo.com C:/playwright-test/component_tests --no-header --no-summary -q in C:\playwright-test\component_tests
```