# Adobe I/O Documentation Template

This is a site template built with the [Adobe I/O Theme](https://github.com/adobe/aio-theme).

View the [demo](https://adobedocs.github.io/dev-site-documentation-template/) running on Github Pages.  

## Where to ask for help

The slack channel #adobeio-onsite-onboarding is our main point of contact for help. Feel free to join the channel and ask any questions.

## How to develop

For local development, simply use :

```shell
$ yarn install
$ yarn dev
```

## How to make changes to UXP API reference

1. Update the version of `uxp-documentation` in `package.json`.
2. `$ yarn install`
3. `$ yarn prepare-uxp`
4. `$ yarn dev`
5. Bump the version in `package.json` before checking in the files.
