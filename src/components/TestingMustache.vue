<template>
  <h1>{{ job.position }}</h1>
  <button @click="increase()">Increase</button>
  <p>My Salary Now has {{ job.salary }}</p>
  <p v-html="content"></p>
  <img :src="source" />
</template>

<script lang="ts">

export default {
  data() {
    return {
      name: 'nak',
      age: 20,
      job: {
        position: 'devOps',
        salary: 2000,
      },
      content: '<strong>Strong Text</strong>',
      source: 'https://blog.openreplay.com/images/directives-in-vue/images/hero.png',
    }
  },
  methods: {
    increase() {
      this.job.salary += 500
    },
  },
}
</script>
