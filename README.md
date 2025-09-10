# vue-project

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Architecture Overview

```text
index.html
  └─ loads /src/main.ts
       └─ createApp(App.vue)
            ├─ install Pinia (stores/)
            ├─ install Router (src/router/index.ts)
            └─ mount #app

App.vue
  └─ &lt;RouterView/&gt;
       ├─ HomeView.vue
       ├─ AboutView.vue ── uses components/VueDirective.vue
       ├─ HistoryView.vue ── uses components/ReactivityCom.vue
       └─ ContactView.vue

components/
  ├─ TheWelcome.vue + icons/
  ├─ HelloWorld.vue
  └─ TestingMustache.vue

stores/
  └─ counter.ts (Pinia store: count, doubleCount, increment)

build & tooling
  ├─ Vite (vite.config.ts) + alias @ -&gt; src
  ├─ TypeScript (tsconfig.*)
  ├─ ESLint/Prettier/Oxlint (eslint.config.ts, .prettierrc.json)
  ├─ CI: CircleCI (.circleci/config.yml) builds and scans Dockerfile
  └─ Docker: Node builder -&gt; Nginx serving dist/
```
