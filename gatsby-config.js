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
  pathPrefix: process.env.PATH_PREFIX || "/premiere-pro/uxp/",
  siteMetadata: {
    githubIssue: {
      removeLogIssue: true,
    },
    versions: [],
    pages: [
      {
        title: "UXP for Premiere Pro",
        description: "Introduction to the Premiere Pro UXP API",
        path: "index.md",
      },
      {
        title: "Introduction",
        path: "introduction",
      },
      {
        title: "Plugins",
        path: "plugins/",
      },
      {
        title: "Resources",
        path: "resources/",
      },
      {
        title: "References",
        menu: [
          {
            title: "What's New?",
            path: "changelog/",
          },
          {
            title: "Premiere API",
            //description: 'Premiere Pro specific UXP documentation',
            path: "ppro_reference/",
          },
          {
            title: "UXP API",
            path: "uxp-api/",
          },
        ],
      },
    ],
    subPages: [
      {
        title: "Overview",
        path: "introduction/",
      },
      {
        title: "Essentials",
        header: true,
        path: "introduction/essentials/tech-stack/",
        pages: [
          {
            title: "Developer Tools",
            path: "/introduction/essentials/dev-tools/",
          },
          {
            title: "Tech Stack Foundations",
            path: "/introduction/essentials/tech-stack/",
          },
        ],
      },
      {
        title: "Plugins",
        path: "plugins/",
        header: true,
        pages: [
          {
            title: "Getting Started",
            path: "plugins/",
          },
          {
            title: "Concepts",
            path: "plugins/concepts/",
            pages: [
              {
                title: "Entrypoints",
                path: "plugins/concepts/entrypoints/",
              },
              {
                title: "Manifest",
                path: "plugins/concepts/manifest/",
              },
            ],
          },
          {
            title: "Tutorials",
            path: "plugins/tutorials/",
            pages: [
              {
                title: "UDT Plugin development",
                path: "/plugins/tutorials/udt-deep-dive/index.md",
                pages: [
                  {
                    title: "Overview",
                    path: "/plugins/tutorials/udt-deep-dive/index.md",
                  },
                  {
                    title: "The Playground",
                    path: "/plugins/tutorials/udt-deep-dive/playground.md",
                  },
                  {
                    title: "Plugin Management",
                    path: "/plugins/tutorials/udt-deep-dive/plugin-management/",
                  },
                  {
                    title: "Plugin Workflows",
                    path: "/plugins/tutorials/udt-deep-dive/plugin-workflows/",
                  },
                ],
              },
              {
                title: "Add Commands",
                path: "/plugins/tutorials/add-commands/",
              },
              {
                title: "Add Lifecycle Hooks",
                path: "/plugins/tutorials/add-lifecycle-hooks/",
              },
              {
                title: "Inter-plugin communication",
                path: "/plugins/tutorials/inter-plugin-comm/",
              },
              {
                title: "Modularizing code",
                path: "/plugins/tutorials/importing-modules/",
              },
            ],
          },
          {
            title: "Advanced Topics",
            path: "plugins/advanced/",
          },
        ],
      },
      {
        title: "Resources",
        path: "resources/",
        header: true,
        pages: [
          {
            title: "Overview",
            path: "resources/",
          },
          {
            title: "Fundamentals",
            path: "resources/fundamentals/apis/",
            header: true,
            pages: [
              {
                title: "APIs",
                path: "/resources/fundamentals/apis/",
              },
              {
                title: "DOM APIs",
                path: "/resources/fundamentals/dom-apis/",
              },
              {
                title: "User Interface",
                path: "/resources/fundamentals/creating-ui/",
              },
              {
                title: "Nomenclature",
                path: "/resources/fundamentals/nomenclature/",
              },
            ],
          },
          {
            title: "Starters & Samples",
            path: "resources/starters-samples/",
          },
          {
            title: "Share & Distribute",
            path: "resources/distribution/overview/",
            pages: [
              {
                title: "Overview",
                path: "/resources/distribution/overview/",
              },
              {
                title: "Package a plugin",
                path: "/resources/distribution/package/",
              },
              {
                title: "Install a plugin",
                path: "/resources/distribution/install/",
              },
              {
                title: "Adobe Marketplace",
                path: "/resources/distribution/adobe-marketplace/",
                pages: [
                  {
                    title: "Overview",
                    path: "/resources/distribution/adobe-marketplace/",
                  },
                  {
                    title: "Create a Listing",
                    path: "/resources/distribution/listing/",
                  },
                  {
                    title: "Review process",
                    path: "/resources/distribution/review/",
                  },
                ],
              },
              {
                title: "Independent Distribution",
                path: "/resources/distribution/independent-distribution/",
              },
              {
                title: "Enterprise Distribution",
                path: "/resources/distribution/enterprise-distribution/",
              },
            ],
          },
          {
            title: "Recipes",
            path: "resources/recipes/",
            pages: require("./reference-recipes.js"),
          },
          {
            title: "FAQ",
            path: "resources/faq/",
          },
        ],
      },
      {
        title: "Premiere Pro DOM API Reference",
        path: "/ppro_reference",
        pages: require("./reference-ppro.js"),
      },
      {
        title: "UXP API References",
        path: "uxp-api/",
        pages: [
          {
            title: "JavaScript Reference",
            path: "/uxp-api/reference-js/",
            pages: require("./reference-js.js"),
          },
          {
            title: "CSS Reference",
            path: "/uxp-api/reference-css/",
            pages: require("./reference-css.js"),
          },
          {
            title: "HTML Reference",
            path: "/uxp-api/reference-html/",
            pages: require("./reference-html.js"),
          },
          {
            title: "Spectrum UXP Reference",
            path: "/uxp-api/reference-spectrum/",
            pages: require("./reference-spectrum.js"),
          },
          {
            title: "Known Issues",
            path: "/uxp-api/known-issues/",
          },
        ],
      },
    ],
  },
  plugins: [`@adobe/gatsby-theme-aio`],
};
