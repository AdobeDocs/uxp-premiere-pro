/*
 * Copyright 2020 Adobe. All rights reserved.
 * This file is licensed to you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License. You may obtain a copy
 * of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
 * OF ANY KIND, either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 */

module.exports = {
  pathPrefix: process.env.PATH_PREFIX || '/premiere-pro/uxp/',
  siteMetadata: {
    githubIssue: {
      removeLogIssue: true,
    },
    versions: [


    ],
    pages: [
      {
        title: 'UXP for Premiere Pro',
        description: 'Introduction to the Premiere Pro UXP API',
        path: 'index.md'
      },
      {
        title: 'Introduction',
        path: 'introduction/'
      },
      {
        title: 'Plugins',
        path: 'plugins/'
      },
      {
        title: 'Resources',
        path: 'resources/'
      },
      {
        title: 'References',
        menu: [
          {
            title: 'What\'s New?',
            path: 'changelog/'
          },
          {
            title: 'Premiere API',
            //description: 'Premiere Pro specific UXP documentation',
            path: 'ppro_reference/'
          },
          {
            title: 'UXP API',
            path: 'reference/uxp-api/'
          },
        ]
      },
      {
        title: 'Support',
        path: 'support/'
      }
    ],
    subPages: [
      {
        title: 'Essentials',
        header: true,
        path: 'introduction/',
        pages: [
          {
            title: 'Programming languages',
            path: '/introduction/essentials/tech-stack/'
          },
          {
            title: 'Developer Tools',
            path: '/introduction/essentials/dev-tools/'
          }
        ]
      },
      {
        title: 'Plugins',
        path: 'plugins/',
        header: true,
        pages: [
          {
            title: 'Getting Started',
            path: 'plugins/getting-started/'
          },
          {
            title: 'Concepts',
            path: 'plugins/concepts/',
            pages: [
              {
                title: 'Entry points',
                path: 'plugins/concepts/entry-points/'
              },
              {
                title: 'Manifest',
                path: 'plugins/concepts/manifest/',
              },
            ]
          },
          {
            title: 'Tutorials',
            path: 'plugins/tutorials/',
            pages: [
              {
                title: "Developing plugins with UDT",
                path: "/plugins/tutorials/udt-deep-dive/",
                pages: [
                  {
                    title: 'Plugin Management',
                    path: '/plugins/tutorials/udt-deep-dive/plugin-management/'
                  },
                  {
                    title: 'Plugin Workflows',
                    path: '/plugins/tutorials/udt-deep-dive/plugin-workflows/'
                  },
                  {
                    title: 'Working with React',
                    path: '/plugins/tutorials/udt-deep-dive/working-with-react/'
                  },
                ],
              },
              {
                title: 'Adding command entrypoints',
                path: '/plugins/tutorials/adding-command-entrypoints/'
              },
              {
                title: "Lifecycle hooks",
                path: "/plugins/tutorials/plugin-lifecycle-hooks/"
              },
              {
                title: "Communicate with other plugins",
                path: "/plugins/tutorials/inter-plugin-comm/"
              },
              {
                title: "Modularizing code",
                path: "/plugins/tutorials/importing-modules/"
              }
            ]
          },
          {
            title: 'Advanced Topics',
            path: 'plugins/advanced/'
          },
        ]
      },
      {
        title: "Resources",
        path: "resources/",
        header: true,
        pages: [
          {
            title: 'Fundamentals',
            path: 'resources/fundamentals/',
            header: true,
            pages: [
              {
                title: 'APIs',
                path: '/resources/fundamentals/apis/'
              },
              {
                title: "Create UI",
                path: "/resources/fundamentals/create-ui/"
              },
            ]
          },
          {
            title: 'Migration guides',
            path: 'resources/migration_guides/',
            pages: [
              {
                title: 'ExtendScript',
                path: 'resources/migration_guides/extendscript/'
              },
              {
                title: 'CEP',
                path: 'resources/migration_guides/cep/'
              }
            ]
          },
          {
            title: 'Starters & Samples',
            path: 'resources/starters_samples/',
          },
          {
            title: 'Recipes',
            path: 'resources/recipes/',
            pages: require("./reference-recipes.js"),
          },
        ]
      },
      {
        title: 'Premiere Pro DOM API Reference',
        path: '/ppro_reference',
        pages: require("./reference-ppro.js"),
      },
      {
        title: 'UXP API Referencee',
        path: 'reference/uxp-api/',
        pages: [{
          title: "JavaScript Reference",
          path: "/reference/uxp-api/reference-js/",
          pages: require("./reference-js.js"),
        },
        {
          title: "CSS Reference",
          path: "/reference/uxp-api/reference-css/",
          pages: require("./reference-css.js"),
        },
        {
          title: "HTML Reference",
          path: "/reference//uxp-api//reference-html/",
          pages: require("./reference-html.js"),
        },
        {
          title: "Spectrum UXP Reference",
          path: "/reference//uxp-api/reference-spectrum/",
          pages: require("./reference-spectrum.js"),
        },
        {
          title: "Known Issues",
          path: "/reference/uxp-api/known-issues/",
        }]
      }
    ]
  },
  plugins: [`@adobe/gatsby-theme-aio`]
};
