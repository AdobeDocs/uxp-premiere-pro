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
        path: 'introduction/index.md'
      },
      {    
        title: 'References',
        menu: [
          {
            title: 'What\'s New?',
            path: 'changelog/index.md'
          },
          {
            title: 'Premiere UXP API',
            //description: 'Premiere Pro specific UXP documentation',
            path: 'ppro_reference/index.md'
          },
          {
            title: 'Common UXP API',
            // description: 'Cross-Application UXP documentation',
            path: 'uxp_reference/index.md'
          },
        ]
      },
      {
        title: 'Support',
        path: 'support/index.md'
      }
    ],
    subPages: [
      {
        title: 'Essentials',
        header: true,
        pages: [
          {
            title: 'Programming languages',
            path: '/introduction/essentials/prog_lang/'
          },
          {
            title: 'Developer Tools',
            path: '/introduction/essentials/dev-tools/'
          }
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
