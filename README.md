# Adobe I/O Documentation Template

This is a site template built with the [Adobe I/O Theme](https://github.com/adobe/aio-theme).

View the [demo](https://adobedocs.github.io/dev-site-documentation-template/) running on Github Pages.  

## Where to ask for help

The slack channel #adobeio-onsite-onboarding is our main point of contact for help. Feel free to join the channel and ask any questions.

## How to develop

Additional details on EDS-required server setup can be found on the [`adp-devsite-utils`](https://github.com/AdobeDocs/adp-devsite-utils) repo. All three of these servers must be running simultaneously in order for the documentation to be accessible locally.

1. Clone, install, and run the **Content** server (you are here):
    ```sh
    $ git clone https://github.com/AdobeDocs/uxp-premiere-pro
    $ cd uxp-premiere-pro
    $ yarn install
    $ yarn dev
    ```

1. Clone, install, and run the **Code** server ([adp-devsite](https://github.com/AdobeDocs/adp-devsite)):
    ```sh
    $ git clone https://github.com/AdobeDocs/adp-devsite
    $ cd adp-devsite
    $ npm install
    $ npm run dev
    ```

1. Clone, install, and run the **Runtime** connector server ([devsite-runtime-connector](https://github.com/aemsites/devsite-runtime-connector)):
    ```sh
    $ git clone https://github.com/aemsites/devsite-runtime-connector
    $ cd devsite-runtime-connector
    $ npm install
    $ npm run dev
    ```

## How to make changes to UXP API reference

1. Update the version of `uxp-documentation` in `package.json`.
2. `$ yarn install`
3. `$ yarn prepare-uxp`
4. `$ yarn dev`
5. Bump the version in `package.json` before checking in the files.
