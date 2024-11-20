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
  pathPrefix: process.env.PATH_PREFIX || '/premiere-pro-uxp/',
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
            title: 'Premiere UXP API',
            //description: 'Premiere Pro specific UXP documentation',
            path: 'ppro_reference/'
          },
          {
            title: 'Common UXP API',
            // description: 'Cross-Application UXP documentation',
            path: 'uxp_reference/'
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
            path: '/introduction/essentials/prog_lang/'
          },
          {
            title: 'Developer Tools',
            path: '/introduction/essentials/dev_tools/'
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
            path: 'plugins/getting_started/'
          },
          {
            title: 'Concepts',
            path: 'plugins/concepts/',
            pages: [
              {
                title: 'Entry points',
                path: 'plugins/concepts/entry_points/'
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
                title: 'My First Tutorial',
                path: '/plugins/tutorials/my_first_tutorial/'
              },
              {
                title: 'My Second Tutorial',
                path: '/plugins/tutorials/my_second_tutorial/'
              },
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
                title: 'Concept One',
                path: 'resources/fundamentals/concept_1/'
              },
              {
                title: 'Concept Two',
                path: 'resources/fundamentals/concept_2/'
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
            pages: [
              {
                title: 'Premiere Pro Recipes',
                path: 'resources/recipes/ppro_recipes',
                pages: require('./reference_recipes_ppro.js'),
              },
              {
                title: 'UXP Recipes',
                path: 'resources/recipes/uxp_recipes',
                pages: require('./reference_recipes_uxp.js'),
              }

            ]
          },
        ]
      },
      {
        title: 'API Reference',
        path: '/ppro_reference',
        pages: require("./reference-ppro.js"),
      }
    ]
  },
  plugins: [`@adobe/gatsby-theme-aio`]
};
